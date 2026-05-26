# Mapping Orchestrator

You are a mapping coordinator. You discover candidate atlas matches for classical
(or prior transcriptomic) cell types, substantiate mappings against evidence and
atlas metadata, and produce MappingEdge YAML with structured property comparisons.

The curator may arrive with a hypothesis or with a discovery question. Both modes
use the same pipeline — discovery simply means Step 0 generates the candidates
rather than receiving them.

**Prerequisites**:
- Classical `CellTypeNode` in a KB YAML graph with at minimum: defining markers,
  NT type, and anatomical location. Literature evidence items improve confidence
  but are not required to begin — edges can start at LOW/UNCERTAIN and be upgraded
  after lit review.
- Taxonomy reference DB ready for the target atlas. The `query-taxonomy-db` skill
  (Step 0) checks freshness automatically and rebuilds if needed. Anatomy closure
  must be built once per taxonomy: `just fetch-mba-ontology` then
  `just build-anat-closure {taxonomy_id}`. The skill will warn if a newer MBA
  ontology release is available.

---

## Run parameters

```
PARAMS:
  classical_node_file: ""       # path to KB YAML containing the classical node(s)
  classical_node_id: ""         # id of the classical node to map (required)
  taxonomy_id: "CCN20230722"    # taxonomy DB to query for atlas candidates
  curator_hypothesis: null      # optional: {cell_set_accession, relationship} or list thereof
                                # if null → discovery mode (Step 0 queries taxonomy DB)
  ranks: [0, 1]                 # taxonomy ranks to query (0=leaf, 1=supertype, 2=subclass, …)
                                # check taxonomy_meta.yaml level_hierarchy for available ranks
  stats_h5: "conf/mapmycells/{taxonomy_id}/precomputed_stats.h5"
                                # canonical HDF5 path; used by Step 2b for expression enrichment
                                # if not at canonical path, copy/symlink before running
  gene_mapping_tsv: "conf/gene_mapping_{taxonomy_id}.tsv"
                                # generate once: just generate-gene-mapping {stats_h5} {gene_mapping_tsv}
  model: "sonnet"
```

**Precomputed stats**: Before starting, check whether a precomputed stats HDF5 is available
for the target taxonomy:

```bash
just show-meta {taxonomy_id}   # check mapmycells.local_stats_path
```

If `local_stats_path` is set, Step 2.5 will run the stats cross-check automatically.
If not, download with `just at-download-taxonomy {taxonomy_id}` first.

---

## Step 0: Candidate discovery

If `curator_hypothesis` is provided, skip to Step 1 using those candidates.

Otherwise, query the taxonomy DB for candidates at each rank, then refine with a subagent.

### Step 0a: DB query

Run the taxonomy DB candidate search at each requested rank. Ranks are integers
(0 = most granular/leaf, incrementing toward root). The mapping between rank and
level name is taxonomy-specific — check `taxonomy_meta.yaml` `level_hierarchy`
for the target taxonomy.

```bash
# For each rank in {ranks}, run:
just find-candidates {classical_node_file} {classical_node_id} {taxonomy_id} {rank} {top_k} \
  > {output_dir}/discovery_candidates_rank{rank}.json
```

Default: `top_k=5` per rank. Adjust ranks based on the taxonomy's
level_hierarchy — some taxonomies have more or fewer levels.

Phase 1 Stage A scoring (see [planning/map_cell_type_redesign_roadmap.md](../planning/map_cell_type_redesign_roadmap.md) §3 for the full
specification):

- **Hard prerequisite filters** (drop, not penalise): region match
  (programmatic anat-table check + LLM-adjacency fallback for non-overlap
  cases like CA1 ↔ subiculum); NT match (only when both classical and
  candidate carry NT). Annotation-transfer-matched candidates bypass
  both filters.
  - **Rank ≥ 1 descendant-anat fallback** (BCKG workaround): when a
    rank ≥ 1 candidate's own `anat` rows fail to intersect the expanded
    query closure, find_candidates retries against the *union of its
    rank-0 descendants' anat*. If that intersects, the candidate
    survives and the result carries `region_evidence: descendant_only`.
    Rationale: upstream Brain Cell KG strips non-dominant regions from
    non-leaf taxonomy nodes via a percent-of-cells cutoff, so the
    subclass `anat` row is unreliable; rank-0 (cluster) anat comes
    from the source cluster-cell-anat table and is intact. **This
    fallback should be removed once BCKG ships an upstream
    anat-rollup fix.** See
    [planning/at_blind_region_drop_findings_2026-05-12.md](../planning/at_blind_region_drop_findings_2026-05-12.md)
    § a, § B2.
- **Soft scoring** within the surviving pool: per-marker presence/absence
  credit and percentile-based discrimination (defining markers +
  neuropeptides + negative markers, equal-weight); annotation-transfer
  F1 buckets (+3/+2/+1); sex-bias bonus at rank 0.
- **Heterogeneity coverage** at rank ≥ 1: positive-marker scores are
  soft-dampened by `coverage^0.5` where coverage is the fraction of
  rank-(N−1) children with detectable expression. Tempers over-confidence
  on heterogeneous supertypes.
- **Output**: `expression_detail` (per-gene val/percentile/score),
  `region_fraction`, `at_hit`, `coverage` are emitted alongside the score
  for downstream consumption.

### Step 0b: Refinement subagent (optional)

Phase 1 changed Step 0b's role. Under the previous design, this subagent
produced the STRONG / PLAUSIBLE / WEAK / EXCLUDE assessment that backed
the curator gate at Step 1. With the gate removed and Stage A scoring
now emitting per-gene `expression_detail`, `region_fraction`, `at_hit`,
and (at rank ≥ 1) `coverage` directly in the JSON, most of that
assessment is redundant.

Step 0b is now **optional**. Skip unless Step 0a output is inadequate
for some specific reason (e.g. a curator wants narrative summarisation
of the candidate pool). When run, the subagent's job shrinks to:

- Reading the per-rank `discovery_candidates_rank*.json` files.
- Surfacing the structured fields already emitted by find-candidates
  in human-readable form for an out-of-band curator review.
- Optionally adding cross-references that the structured data
  doesn't already encode (e.g. parent supertype name for rank-0
  candidates).

Do **not** re-implement scoring or filtering logic in this subagent —
Stage A is the authority. The previous full prompt used to drive
gate-time decisions is preserved in git history.

---

### Step 0b legacy prompt (deprecated)

The prompt below is retained for reference only — running it under the
Phase 1 architecture duplicates work that find-candidates already does
(coverage, AT lookup, region fraction). Keep for now until report-stage
synthesis (Phase 3) supersedes the narrative role entirely.

```
[deprecated — see Step 0b note above. Previous prompt body lives in git
history at the pre-Phase-1 commit.]
```

---

## Step 1: Cutoff (no curator gate)

The Stage A→B curator gate has been removed (Phase 1). Top-K candidates
from Step 0 — default `K=5`, configurable via the `top_k` arg to
`just find-candidates` — feed Stage B mapping-subagent spawning directly.
Every above-cutoff candidate gets a `MappingEdge` written; the report
(generated downstream) is the human review point.

If discovery ran, read `discovery_candidates.json` for context but do not
present a gate. Proceed directly to Step 2.

If `curator_hypothesis` was provided in PARAMS, use those candidates as
the input set instead of discovery output.

---

## Step 2: Pre-flight — proactive enrichment

`precomputed_expression` data on candidate atlas nodes is now provisioned
proactively, not on demand per mapping. Before running this orchestrator,
ensure:

```bash
just enrich-marker-union {taxonomy_id} {stats_h5} {gene_mapping_tsv}
```

has been run for the taxonomy. This single command:

1. Scans `kb/graphs/**/*.yaml` for non-atlas nodes and collects the union
   of all their `defining_markers + neuropeptides + negative_markers`
   symbols.
2. Enriches every taxonomy node at the cluster + supertype levels with
   `precomputed_expression` for those genes (the supertype path also
   populates `child_cluster_expression` for the heterogeneity coverage
   signal at rank ≥ 1).
3. Rebuilds the SQLite DB to reflect the new data.

Re-run when classical nodes are added or their marker lists change.
Phase 1 commit 10 introduced this; previous per-mapping Step 2b/2c are
removed.

If `stats_h5` or `gene_mapping_tsv` is unavailable for the target
taxonomy, expression data will be sparse and Stage A scoring will fall
back to metadata-only marker matching (binary +1). Mapping subagents
will mark expression-comparisons as `NOT_ASSESSED` for genes absent from
atlas metadata. This is a degraded mode; address by acquiring the HDF5
and re-running enrichment.

---

## Step 3: Mapping edge subagent

For each confirmed candidate, spawn a **mapping subagent** with this exact prompt:

```
You are a mapping edge generation agent. You produce a MappingEdge with structured
property comparisons and evidence items.

CLASSICAL NODE FILE: {classical_node_file}
CLASSICAL NODE ID: {classical_node_id}
ATLAS NODE ACCESSION: {cell_set_accession}
TAXONOMY ID: {taxonomy_id}
TAXONOMY DIR: kb/taxonomy/{taxonomy_id}/
RELATIONSHIP: {relationship_type}
DISCOVERY DATA: {path to discovery_candidates.json, if available}

REFERENCE: Read kb/graphs/cerebellum/CB_PLI_types.yaml for structural reference —
specifically the edges section (starts after the nodes). Match that format exactly.

TASK:

1. Read the classical node from the graph file. Find the atlas node by searching
   for `cell_set_accession: {cell_set_accession}` in the taxonomy YAML files
   under TAXONOMY DIR (check the level file matching the accession pattern:
   SUPT → supertype.yaml, CLUS → cluster.yaml, SUBC → subclass.yaml).
   Read the CB_PLI_types.yaml edges for structural reference.

2. Build property_comparisons for at minimum:
   - nt_type
   - location (one comparison per classical location with `compartment: SOMA`
     or no compartment — skip `AXON_TARGET` / `DENDRITE` entries, which are
     not captured in atlas MERFISH data)
   - Each classical defining_marker (property: "marker_{symbol}")
   - Each classical negative_marker (property: "negative_marker_{symbol}")
   - Each classical neuropeptide (property: "neuropeptide_{symbol}")

   For each comparison:
   - node_a_value: verbatim from classical node (include quantitative expression
     data if available from source-side re-analysis, e.g. detection rate and
     mean counts)
   - node_b_value: verbatim from atlas node metadata (or "not present" if absent).
     If the atlas node has a `precomputed_expression` block (populated by
     `just enrich-marker-union`, see Step 2), include the quantitative mean
     expression for each gene alongside the metadata annotation. See
     "Expression cross-check" below.
   - alignment: CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED
   - notes: brief explanation (required for APPROXIMATE and DISCORDANT). If
     the precomputed expression value disagrees with the taxonomy metadata
     annotation, note the discrepancy factually (e.g. "Pnoc listed in
     taxonomy metadata neuropeptides; precomputed_expression shows 0.0 in
     this cluster"). Do not attempt to explain the discrepancy — flag it
     for investigation.

   **Phase 1 alignment rules for marker comparisons** (gap-aware):
   - CONSISTENT: atlas value ≥ MIN_DETECTABLE AND classical type asserts the
     marker is present.
   - APPROXIMATE: presence agrees but signal is weak — `val ≥ MIN_DETECTABLE`
     with sibling-non-discriminating expression (presence credit only),
     OR a low coverage at rank ≥ 1 (cite the `coverage` value from
     `expression_detail`: "supertype mean 5.0; coverage 0.25 across child
     clusters — concentrated in CS20230722_CLUS_NNNN").
   - DISCORDANT: classical asserts the marker is present but the atlas
     value is below `MIN_DETECTABLE` (absence on the candidate side), OR
     classical asserts a negative marker but the atlas value is above
     `MIN_DETECTABLE`.
   - NOT_ASSESSED: gene absent from `precomputed_expression` and from
     atlas metadata.

   **Expression cross-check.** The atlas node's `precomputed_expression.genes`
   list (if present in the taxonomy YAML) contains per-gene mean expression
   values pulled from the MapMyCells precomputed stats. For each classical
   defining_marker, negative_marker, and neuropeptide:

   a. Look up the gene symbol in `precomputed_expression.genes`.

   b. Populate `node_b_value` with the quantitative expression (e.g.
      "Chrna2: 4.3 (precomputed mean); listed in supertype markers").
      This upgrades NOT_ASSESSED comparisons where the gene is absent from
      atlas metadata but present in the expression data, and adds
      quantitative grounding to metadata-only comparisons.

   c. Where a gene shows zero expression but is annotated in the taxonomy
      metadata, or vice versa, note the discrepancy in the `notes` field.
      Do not adjudicate — report both values for downstream interpretation.

   d. If no `precomputed_expression` block is present, mark expression
      comparisons as NOT_ASSESSED for genes absent from atlas metadata.

   LOCATION alignment rules:
   - CONSISTENT: atlas node has cells in the matching soma region
   - APPROXIMATE: atlas node has cells in an adjacent subfield (possible
     registration error — note the adjacent region and cell count; do not
     treat as strong counter-evidence)
   - DISCORDANT: atlas node has substantial cells in a distant, anatomically
     unrelated region (e.g. amygdala cells in a hippocampal cluster). Note
     that the classical type may still be a subtype of the T-type even when
     distant cells are present — the mapping is weakened but not disproven.
   - NOT_ASSESSED: classical location not representable from atlas metadata

3. **Do NOT set `confidence`, `confidence_score`, or `rationale`.**
   Phase 3 (2026-05-13) moved authority for the holistic verdict +
   rationale to the report-time agent (`workflows/gen-report.md`
   Step 3). Stage B emits structured data only — the report-gen agent
   reads it back, synthesises the verdict against the full evidence
   picture (including the AT pool-candidate pre-pass and cross-edge
   indistinguishability), writes `confidence` + `confidence_score` +
   `rationale` + `rationale_source_hash` + `report_path` +
   `rationale_generated_at` back to the edge. The schema makes
   `confidence` optional for exactly this reason. See #64 for the
   design.

4. Assemble evidence items. Each item needs:
   - evidence_type (LITERATURE / ATLAS_METADATA / ANNOTATION_TRANSFER / etc.)
   - supports (SUPPORT / REFUTE / PARTIAL / NO_EVIDENCE)
   - reference (PMID or DOI)
   - explanation (concise, citable)

   For stub-stage mappings with no primary literature on the edge itself,
   use ATLAS_METADATA evidence (the atlas node's own properties as evidence
   for the mapping). This is valid LOW-confidence evidence.

   **ANNOTATION_TRANSFER evidence: metrics_by_level is populated
   programmatically — DO NOT transcribe F1 numbers.** When you create
   an ANNOTATION_TRANSFER evidence item, supply only:

   ```yaml
   - evidence_type: ANNOTATION_TRANSFER
     run_ref: at_run_<id>                    # matches a dir under kb/annotation_transfer_runs/
     source_cluster_label: <bare CSV label>  # matches source_label in at_results.yaml
     supports: <leave unset>                 # post-process sets this from noise floor
     target_atlas: ...                       # human-readable
     method: ...                             # for back-compat; otherwise run_ref carries it
     source_dataset_accession: ...
     # DO NOT write metrics_by_level, best_f1_score, best_mapping_level,
     # best_mapping_rank, n_cells_mapped, coverage, purity, f1_score
     # — these are written programmatically from
     # kb/annotation_transfer_runs/{run_ref}/at_results.yaml using
     # (run_ref, source_cluster_label, edge.taxonomy_type) by
     # src/evidencell/at_metrics.py::compute_edge_metrics().
     # Run `just refresh-at-metrics --apply` after writing edges to
     # populate them.
     explanation: |
       Qualitative read of the AT result for this edge. Cite cell
       counts, regional pattern, source-vs-edge-target relationship
       where relevant. NOT the F1 number itself — that's in
       metrics_by_level after the programmatic populate.
   ```

   `source_cluster_label` MUST be the bare label exactly as it appears
   in the AT run's `at_results.yaml` `source_label` field — not a
   free-text aggregate like `"BIC (hBIC n=11 + vBIC n=9 aggregated)"`
   (which doesn't join). If the AT run pools upstream (e.g. Que 2021
   aggregates hBC+vBC as `BC`), use the pooled name; record the
   composition in the `source_groups` slot below.

   **Pooled AnnotationTransferEvidence.** When the `metrics_by_level` /
   `best_f1_score` on an AT evidence item were computed by pooling
   multiple raw source clusters into one pseudo-source (the
   `at_figures --pool A,B:NAME --emit-metrics` workflow), record the
   pool composition in `source_groups`:

   ```yaml
   source_groups:
     - label: {pseudo_source_name}         # matches --pool ...:NAME
       members: [{raw_label_1}, {raw_label_2}, ...]
       # rationale: optional — see below
   ```

   `label` must match the source_label key in the figure-rendering
   sidecar (`figures/f1_for_*_metrics.json`) so stored metrics and
   rendered figure are joinable. `members` are the bare source_label
   strings from `f1_matrix.csv`.

   **You MAY seed `source_groups[*].rationale`** when the
   `property_comparisons` you just built already establish that the
   pooled cohorts map indistinguishably to the same target cluster set
   (an AT-side-only observation). Phrase the rationale per the example
   forms in `SourceGroup.rationale` (schema), cite the AT run id, and
   keep to one or two sentences. **Leave it blank** when (a) the AT
   matrix shows scatter within the pool (different members go to
   different targets), or (b) you have not done a cross-cohort
   comparison — the report-time agent has full literature in scope
   and can extend the rationale later. Never overwrite an existing
   rationale; if you find one already present, leave it alone.

5. Add caveats for any DISCORDANT or APPROXIMATE property comparisons, and for
   any known heterogeneity in the classical type.

6. Add unresolved_questions and proposed_experiments where relevant.

7. Produce the MappingEdge YAML block. Edge id format:
   `edge_{lit_type_id}_to_{taxonomy_type_id}`. The edge MUST set
   both `lit_type` and `taxonomy_type` (Phase 2 schema overhaul,
   2026-05-12 — `type_a` / `type_b` are deprecated aliases retained
   only for the transition window).

   **Predicate selection rubric (2026-05-26 refresh).** Apply the
   following decision tree against the property_comparisons you
   just built. The report-time agent (gen-report Stage C) uses the
   same rubric — your initial pick should match what gen-report
   would land on.

   Step (i) — **Cardinality at this rank.** Count how many lit_types
   plausibly map to this taxonomy_type and vice versa **at the
   atlas-side rank you are working**.
     - Multiple lit_types → one taxonomy_type ⇒ `skos:broadMatch` +
       `mapping_cardinality: 1:n`.
     - One lit_type → multiple taxonomy_types at this rank,
       collapsing to one type at rank N+1 ⇒ prefer `skos:broadMatch`
       at rank N+1.
     - One lit_type → multiple taxonomy_types at this rank, with no
       higher rank that rescues to a single broader type ⇒
       `evidencell:CrossCuttingMatch`.
     - Multiple lit_types → one taxonomy_type with the lit-side being
       narrower per-instance ⇒ `skos:narrowMatch` + `mapping_cardinality: n:1`.
     - Otherwise — clean 1:1 candidate — proceed.

   Step (ii) — **Location gate (for clean 1:1 candidates).**
     - taxonomy_type located in classical region + adjacent only ⇒
       proceed to step (iii).
     - taxonomy_type located in regions distant from classical
       region + adjacent ⇒ `skos:broadMatch` + `mapping_cardinality: 1:n`
       (the taxonomy_type is broader by location).

   Step (iii) — **AT gate (when AT evidence is present).**
     - F1 > 0.75 at the working rank with no major contradiction ⇒
       `skos:exactMatch` + `mapping_cardinality: 1:1`.
     - F1 in a borderline band or coverage/purity asymmetry, OR
       marker / location contradictions present ⇒ `skos:closeMatch`.

   Step (iv) — **AT absent.** A clean 1:1 candidate with consistent
   location + markers + literature may still be `skos:exactMatch`,
   but flag in `caveats` that AT is missing — the report-time agent
   will cap confidence at MODERATE. Any unresolved contradiction
   demotes to `skos:closeMatch`.

   Step (v) — **Unresolvable.** If evidence is insufficient to pick
   between any of the above ⇒ `evidencell:UncertainRelationship` +
   `mapping_justification: semapv:UnspecifiedMatching` +
   `reconciliation_note` describing what additional evidence would
   resolve it.

   The hidden-1:1 broadMatch case (broadMatch + 1:1) is **removed**
   — if the specific sub-cluster is TBD, map at the next rank up
   where the relationship is cleanly 1:n.

   `evidencell:PartialOverlapMatch` is **deprecated** as of
   2026-05-26 — do not emit on new edges. The new rubric absorbs
   its cases into `skos:closeMatch` (1:1-ish with contradictions)
   or one of the broad/narrow/cross-cutting predicates.

   Set `mapping_justification: semapv:UnreviewedManualMapping` by
   default (agent-emitted); curators promote to
   `semapv:ManualMappingCuration` on review. See
   [`docs/mapping_schema_2026-05-12.md`](../docs/mapping_schema_2026-05-12.md)
   for the SKOS direction convention and worked examples.

8. **Copy the candidate's `discovery_score` block onto the edge
   verbatim.** When DISCOVERY DATA is provided, locate this
   candidate's entry in `candidates[]` (match on
   `node_id == cell_set_accession`) and copy its
   `discovery_score` value as-is onto the edge's `discovery_score`
   slot. No transformation, no re-interpretation — Stage A's JSON
   already matches the schema shape. The block captures Stage A's
   cohort-ranking view: composite score, rank-in-cohort,
   percentile contexts, per-gene contributions (raw_tier +
   applied_score), and the AT signal that fed scoring. It is
   meta-signal about candidate generation, NOT a confidence
   value; the report-time agent will weigh it as one input
   alongside marker comparisons, AT metrics, and literature.

   If DISCOVERY DATA is unavailable (legacy edge, hypothesis
   mode without a discovery run), omit `discovery_score` —
   it's optional. The backfill module
   (`just backfill-discovery-score`) can populate it later from
   on-disk discovery JSONs.

RETURN the complete MappingEdge YAML block as a code fence. Do not write files.
```

---

## Step 4: [GATE] Expert reviews proposed edges

Present each proposed edge to the curator:

```
PROPOSED EDGE: {classical_name} → {atlas_name}
════════════════════════════════════════════════
Relationship: {RELATIONSHIP}
Cardinality:  {CARDINALITY}
Justification: {JUSTIFICATION}

Verdict + rationale: (pending — written by gen-report)

Property comparisons:
  nt_type:              {alignment} — {node_a} vs {node_b}
  location:             {alignment} — {node_a} vs {node_b}
  marker_Sst:           {alignment} — ...
  marker_Chrna2:        {alignment} — ...
  neuropeptide_Npy:     {alignment} — ...
  ...

Evidence items: {count}
Caveats: {count}
Unresolved questions: {list}
Proposed experiments: {list}

What would let gen-report reach a confident verdict: {specific gaps}
```

Ask:
> "Review this edge. Approve, modify (relationship/cardinality/caveats), or reject.
> The verdict (`confidence` / `confidence_score` / `rationale`) is not set at
> Stage B — gen-report will synthesise and write it back. If you want to proceed
> to lit review before committing, say 'defer' — the edge will be saved as a
> draft proposal."

---

## Step 5: Write to KB

For approved edges:

1. For each atlas node referenced by an edge, ensure a minimal taxonomy ref stub
   exists in the graph's `nodes:` list. A stub needs only:
   `id` (= cell_set_accession), `name`, `definition_basis: ATLAS_TRANSCRIPTOMIC`,
   `taxonomy_id`, `cell_set_accession`. Full node data lives in the taxonomy
   reference store at `kb/taxonomy/{taxonomy_id}/`.

2. Append approved edges to the `edges:` section of the target file. Edge
   `taxonomy_type` should use the `cell_set_accession` (e.g. `CS20230722_CLUS_0769`).

3. Update `target_atlas` on the graph if it was null (as for ASTA report ingests
   that started without an atlas target).

For deferred edges:
- Write to `{output_dir}/proposed_edges_{classical_node_id}.yaml` as a standalone
  fragment. These are picked up after lit review and re-evaluated.

---

## Rules

- **Discovery is the default.** Curator hypotheses are welcome but not required.
  The orchestrator surfaces candidates from the data; the curator adjudicates.
- **Ranks are taxonomy-agnostic.** Always use integer ranks (0=leaf, incrementing),
  never hardcoded level names like "cluster" or "supertype". Check the target
  taxonomy's `taxonomy_meta.yaml` `level_hierarchy` for available ranks.
- **No HIGH confidence from literature alone.** The agent must check the decision
  guide. Annotation transfer or experimental data (ephys/morphology) required.
- **No literature found → UNCERTAIN.** Document the evidence gap explicitly.
  Do not guess. Propose experiments that would resolve it.
- **Stubs are valid starting points.** Atlas metadata (markers, NT, location) is
  real evidence — it supports LOW-confidence edges. Confidence upgrades come from
  lit review and experimental evidence.
- **CB PLI example must be in-context** for the mapping subagent — the MLI1/MLI2
  cross-cutting case is the canonical worked demonstration of non-trivial inference.
- **Single agent for small graphs** (≤5 edges). Spawn per-edge subagents for
  complex multi-type regions.
- **Subagent prompts are contracts.** Do not paraphrase — pass verbatim with
  variables filled in.

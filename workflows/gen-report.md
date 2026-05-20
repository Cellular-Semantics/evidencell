# Report Generation Orchestrator

You are a report coordinator for the evidencell knowledge base. You generate
high-quality human-readable mapping reports from KB YAML + references.json and
verify them for factual accuracy before delivering them to the curator.

The pipeline has three stages:
1. **Fact extraction** (Python, deterministic) — reads YAML, builds reference index,
   emits `{node_id}_facts.json` with all claims labelled by provenance.
2. **Synthesis** (LLM subagent) — reads facts JSON, writes coherent Markdown prose
   with neuroanatomical interpretation. Strictly cite only from the facts file.
3. **Validation** (LLM subagent) — cross-checks generated report against facts JSON.
   Rejects any hallucinated IDs, fabricated quotes, or invented references.

---

## Run parameters

```
PARAMS:
  graph_file: ""        # path to KB YAML containing the edges to report (required)
  node_id: null         # classical node id; null = all non-terminal nodes in graph
  mode: "summary"       # summary | drilldowns | all
  output_dir: null      # default: reports/{region}/
  model: "sonnet"
```

---

## Step 1 — Validate inputs

Read `graph_file` using `yaml.safe_load()`. Confirm:
- File exists and is valid YAML
- `references/{region}/references.json` exists (warn if absent — drill-downs require it)
- If `node_id` is specified: confirm it exists in `graph.nodes[]` as a non-terminal node
  (i.e. `is_terminal` is false or absent)

Print a validation summary:
```
Graph: {graph_file}
Atlas: {target_atlas}
Region: {brain_region}
Nodes: {N total} ({M classical}, {K atlas terminals})
Edges: {E edges} ({counts by confidence tier})
references/{region}/references.json: {found | MISSING}
```

Fail with a clear error message if inputs are invalid. Do not proceed.

---

## Step 2 — Extract structured facts

For each `node_id` to report (one or all classical nodes), run:

```bash
just gen-facts {graph_file} {node_id}
```

This calls `python -m evidencell.render facts {graph_file} --node {node_id}` and writes:
`reports/{region}/{node_id}_facts.json`

If the command exits non-zero, print the error and stop. Do not attempt to reconstruct
facts manually from YAML — the Python extractor enforces provenance labelling.

Confirm the facts file exists and is valid JSON before proceeding to Step 2b.

**Phase 3 note (2026-05-13).** The facts extractor is responsible for stripping
report-time output fields (`rationale`, `confidence`, `confidence_score`,
`rationale_generated_at`, `rationale_source_hash`, `report_path`) from each
edge before serialising — these are the synthesis subagent's outputs and
must not be visible as inputs (loop-avoidance, design issue #64).

---

## Step 2b — Pool-candidate discovery (Phase 3)

For each `node_id`, surface candidate source-group pools for the synthesis
subagent to judge:

```bash
just pool-candidates {graph_file} --node {node_id} \
  > reports/{region}/{node_id}_pool_candidates.json
```

This is a deterministic pre-pass that compares pairs of distinct `lit_type`s
in the graph whose AT-evidence `metrics_by_level` rows are within tolerance
(~5% F1 / precision / recall) across their shared atlas targets. Each
candidate entry names the source groups, the shared targets, and the
property panels assessed (markers, anat, NT, ephys, morphology, dev).

The output is **surfacing only** — the synthesis subagent reads it and
decides whether to act (writing a "no transcriptomic distinction" call into
`rationale` + `reconciliation_note` + a lit-to-lit `skos:closeMatch` edge
per the prompt instructions in Step 3). See #61 for the worked Winterer
Sst-OLM / Htr3a-OLM case and #62 for the related ingest-side prevention.

---

## Step 3 — Synthesis subagent

Spawn a **synthesis subagent** with this exact prompt (substitute values for
`{node_id}`, `{facts_file}`, `{pool_candidates_file}`, `{summary_file}`,
`{region}`, `{graph_file}`):

```
You are a cell type mapping report writer. Write a high-quality, biologist-readable
summary report from structured evidence facts, AND emit a structured verdict
block for write-back to the MappingEdge YAML.

INPUTS YOU READ:
- FACTS FILE: {facts_file}
- POOL CANDIDATES: {pool_candidates_file} (may be empty)
- References corpus: references/{region}/references.json (for quote_keys)

INPUTS YOU MUST NOT READ (Phase 3 loop avoidance):
- The edge's existing `rationale`, `confidence`, `confidence_score`,
  `rationale_generated_at`, `rationale_source_hash`, or `report_path`. The
  facts extractor strips these from {facts_file} so you cannot see them.

OUTPUT FILE: {summary_file}

First, read all inputs completely. Then write the Markdown report below.

---

## Report structure (paper-style — follow exactly, in this order)

The report uses paper-style top-level sections so it can be screenshotted
into a publication. Sections appear in the order: Header → Introduction →
Results → Methods → Discussion → References. Methods is a `<details>` fold
to limit scrolling on screen review (it carries provenance receipts most
readers don't need by default).

### 1. Header

```
# {classical_node.name} — {graph_meta.target_atlas} Mapping Report
*{graph_meta.creation_date} · Source: `{graph_meta.graph_file}`*
```

---

## Introduction

This top-level section bundles location note + classical type table + literature
support. Open the `## Introduction` section with one or two sentences of biological
framing — what is this cell type, why does the mapping matter — drawn from the
classical literature (LITERATURE evidence on the node). Use only facts present in
the facts file; do not invent biological context.

The Cell Ontology mapping line (see "### 4. Cell Ontology mapping" below) is
emitted *after* the classical type description block, not in the framing
paragraph — readers see the biology first, then the ontology placement.

### 2. Location note (conditional)

Emit only if `graph_meta.has_merfish_location` is true:

> **Location note.** WMBv1 location data derives from MERFISH spatial
> registration and records **soma position** only. Axonal and dendritic
> projection targets are not reflected in atlas cluster location fields and
> are not used in mapping assessments.

Then explain briefly why this matters for this specific classical type (e.g. if the
classical type has an axonal projection target that might be confused with soma location).
Use only information from the facts file; do not invent projection targets.

### 3. Classical type table

One row per property from `classical_nodes[0]`. Columns: Property | Value | References.
Use `[n]` labels from `classical_nodes[0].location_refs`, `nt_refs`, marker `refs` etc.

Include rows for: Soma location, NT, Markers, Negative markers, Neuropeptides.
If CL term is present, include it. Omit empty rows.

**Direct expression evidence:** If any marker or neuropeptide has a source whose `method`
contains "re-analysis" or "raw counts", note the quantitative detection rate in the Value
column (e.g. "Sst (100% of OLM cells), Chrna2 (35%), mGluR1/Grm1 (96%)"). These are
directly assessed from the source dataset and provide stronger evidence than literature
reports alone.

After the table, add a collapsible details block with per-property literature support:

```html
<details>
<summary>### Details — source evidence for classical type properties</summary>

For each property in the table that has a source (from `classical_nodes[0]`), write
one bullet per source entry:
- **{Property}:** {method} · {species/scope if specified} · [{n}]
  If a verbatim quote is available in `facts.quotes` for this source, include it as a
  sub-blockquote with the required attribution line:
  > {quote text}
  > — {author} et al. {year}, {section if known} · [{n}] <!-- quote_key: {key} -->

Omit properties with no source entries. Use `[n]` labels that match the References
section. Do not invent sources or quotes not present in `facts.quotes`.
</details>
```

### 4. Cell Ontology mapping

Closes the Introduction. Place this *after* the classical type table and its
Details fold so the reader has the biological description in mind before the
ontology placement.

If `methods_summary.cl_mapping.cl_term_id` is non-empty, emit one line citing
the Cell Ontology term:

> Cell Ontology mapping: {cl_term_label} [[{cl_term_id}]({ols_url})] ({mapping_type}).

If `cl_mapping.cl_term_id` is empty, state:

> No Cell Ontology term currently covers this type — candidate for a new CL term.

If `classical_nodes[0].proposed_cl_term` is populated, follow with:

```markdown
**Proposed CL term:** *{proposed_cl_term.label}* ({proposed_cl_term.status})
> {proposed_cl_term.definition}
```

The blockquote body is the verbatim `proposed_cl_term.definition` text — this
is curator-authored prose stored on the KB node, not a quoted literature
source, so no `quote_key` attribution is required (the hook treats node-level
authored prose like other authored-prose blockquote paths).

For BROAD / RELATED / NARROW mappings, `mapping_notes` is reprised in the
Discussion's Best candidate + caveats section (do not duplicate it here).

---

## Results

This top-level section bundles the mapping candidate overview, per-candidate
property alignment + Evidence support tables, and the per-candidate paragraph(s).
Open with one summary sentence: how many candidates were assessed and what the
primary verdict is (e.g. "Three candidate atlas clusters were assessed; CLUS_1915
in SUPT_0486 is the primary mapping at MODERATE confidence").

**Annotation-transfer overview figure (run-level, filtered)**

If `methods_summary.annotation_transfer_runs[*].figure_relpath` is non-empty
for any run, embed each run's figure once near the top of Results (after the
opening summary sentence, before the candidates table). The figure is
run-level so it does NOT go in any specific candidate paragraph.

**Filter to relevant source groups before embedding.** The canonical figure
on disk (`figures/f1_tree.png` or `figures/f1_heatmap.png`) usually shows
*every* source group in the AT run, including ones irrelevant to the
classical type being reported. For each cited AT run:

1. Collect the set of `source_cluster_label` values that appear on
   `evidence_items[*].fields.source_cluster_label` for AT evidence items
   on edges of this node. That set defines the relevant source groups.
2. Run the figure renderer with `--source` to produce a node-scoped
   variant. Output filename must be node-specific so reports don't
   clobber each other:

   ```bash
   just gen-at-figure {run_id} \
     --source {comma_separated_source_labels} \
     [--f1 {non-standard CSV relpath if needed}] \
     --output figures/f1_for_{node_id}.png \
     --emit-metrics figures/f1_for_{node_id}_metrics.json
   ```

   Use `--pool A,B:NAME` when the source groups are transcriptomically
   indistinguishable and the report's reading is to merge them (e.g. the
   OLM Sst-OLM + Htr3a-OLM case; see [[feedback_at_no_distinction_judgement]]).

   **Caption grounding (mandatory).** `--emit-metrics` writes a JSON
   sidecar with the per-(source, level, target) F1/precision/recall rows
   that the figure actually rendered (after `--pool` and `--source` are
   applied). Captions and any inline figure-supporting statistics in the
   report MUST be derived from this sidecar — read it, pick the rows you
   want to cite, and quote the numbers verbatim. Never re-derive F1
   numbers from the raw `f1_matrix.csv` or copy them from the edge YAML's
   `metrics_by_level`, because those may have been computed under a
   different grouping than the figure. The sidecar and the PNG are
   produced from the same in-memory rows so they are guaranteed in sync.
3. Embed the filtered figure using its relative path from the report:

   ```markdown
   ![Filtered AT figure for {classical_node_name}]({relative_path_to_filtered_png})

   *F1 across taxonomy levels for the {N} source group(s) relevant to
   {classical_node_name}. Each panel row is a source-cell group; nodes
   are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown
   inline. Coverage = fraction of source-group cells landing on this
   target; Purity = fraction of this target's cells coming from the
   source group. With multiple source groups in the figure, Purity
   differentiates them; with a single pooled source, Purity is 1.0 at
   every target and only Coverage discriminates. F1 ≥ 0.5 at a level
   indicates a clean mapping at that resolution.*
   ```

   Emit the **Purity / Coverage gloss only on the FIRST AT figure** in
   the report (subsequent figures can use a one-liner: *"As before, Pur
   = target purity; Cov = source coverage."*).

   If you also want to show the full multi-source figure as supporting
   context (e.g. to justify a pooling decision), generate a *second*
   figure without `--source` and reference it as a follow-up — but the
   filtered figure is the primary embed.

4. The pre-existing canonical `figure_relpath` on the manifest is left
   untouched; reports generate per-node variants on demand and reference
   those.

Use a short interpretive line below the figure (≤2 sentences) drawing on
`methods_summary.annotation_transfer_runs[*].caveats` if relevant.

### 4. Mapping candidates table + property alignment table

**4a. Candidate overview table (one row per edge)**

Columns: Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict.

The **Cells (10x)** column shows the total 10x scRNA-seq cluster size from
`facts.edges[*].n_cells` (sourced from the taxonomy reference DB at gen-facts
time). MERFISH spatial cell counts (per-region distribution from
`anatomical_location[*].cell_count`) belong in the property-alignment table's
location row, not in this column.

Note: if the rendered facts file shows `n_cells: null` for an edge, the
taxonomy DB is stale relative to the schema (the n_cells column was added in
PR #21). Rebuild with `just build-taxonomy-db {taxonomy_id}` and re-run
`just gen-facts` before continuing.

Sort: MODERATE before LOW before UNCERTAIN. Rank only MODERATE and LOW edges (1, 2, …);
use "—" for UNCERTAIN.

For "Key property alignment", give a 1-2 word summary of the most informative
property comparison for that edge (e.g. "Chrna2 APPROXIMATE · Npy CONSISTENT").

Use confidence badges: 🟢 HIGH / 🟡 MODERATE / 🔴 LOW / ⚪ UNCERTAIN.

Note at the end: total edge count and relationship type.

**4b. Property alignment table (mandatory for each primary candidate)**

For the primary (highest-confidence) candidate, and for any secondary candidate
with confidence ≥ MODERATE, write **two** tables immediately after the candidate
overview:

**Table 1 — Property comparison.** One row per *classical property* that has a
comparison in `edges[*].property_comparisons`:

```
| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | {region [MBA:XXX]} | {n}/{total} cells in target region | {cluster primary soma (MBA:XXX)} | CONSISTENT/APPROXIMATE/DISCORDANT |
| NT type | {type} | {supertype NT label} | {cluster NT annotation} | |
| {gene1} expression | defining marker | {supertype mean} | {cluster mean (CLUS_XXXX)} | |
| Sex ratio | {expected direction or "not documented"} | not available | MFR={value} (CLUS_XXXX) | CONSISTENT/APPROXIMATE/DISCORDANT/NOT_ASSESSED |
```

Rules for Table 1:
- One row per property comparison; do NOT include evidence-item rows here.
- Supertype column: use `node_b_value` from the property_comparison where
  `atlas_node_accession` is a supertype (rank ≥ 1). Write "not available" if absent.
- Best cluster column: if the discovery data or edge YAML identifies a best child
  cluster, use that cluster's values. Write "not assessed" if no child-cluster
  data was collected.
- Alignment column: use the `alignment` field from property_comparisons. If
  supertype and cluster alignments differ, show both: "SUPT: APPROXIMATE; CLUS:
  CONSISTENT".
- Sex ratio row: always include. Use MFR from the best child cluster; write
  "not available" at supertype level (MFR is only computed at rank 0).
- Use only values from `facts.edges[*].property_comparisons`. Do not invent.

**Table 2 — Evidence support.** One row per evidence item on the edge,
generated *generically* from `edges[*].evidence_items[*]`. NO per-evidence-type
hard-coded rows or rules. New evidence types appear automatically.

```
| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| {short label} | {EVIDENCE_TYPE_LABELS[evidence_type]} | {supports} | {headline metric or digest} | {ref_label or "atlas-internal"} |
```

Rules for Table 2:
- **Evidence**: a short human label. Derive from `explanation` (first phrase),
  or from `fields.run_ref` / dataset name when more informative. Examples:
  "Knoedler 2022 TRAP-seq", "Atlas precomputed expression", "MapMyCells AT".
- **Type**: the human label for `evidence_item.evidence_type`. The renderer's
  `EVIDENCE_TYPE_LABELS` covers known types; for unknown types fall back to
  the raw enum string.
- **Supports**: `evidence_item.supports` (SUPPORT / PARTIAL / REFUTE /
  NOT_ASSESSED).
- **Headline**: a one-line digest. Pull from `evidence_item.fields` whichever
  field(s) make the supporting numerics legible — examples:
  - `BULK_CORRELATION`: read `fields.statistics` (e.g. "δ=0.0180, rank 1/5322")
  - `ANNOTATION_TRANSFER`: read `fields.best_f1_score` (e.g. "F1=0.62")
  - `LITERATURE`: omit (the snippet appears as a blockquote elsewhere)
  - other types: digest of `explanation`
  If no obvious headline numeric is present, leave blank.
- **Source**: `evidence_item.ref_label` if populated (e.g. "[3]"); else
  "atlas-internal" for ATLAS_METADATA / ATLAS_QUERY items where the data lives
  in the atlas itself; else "—".

This Evidence support table replaces the previous hardcoded "Annotation
transfer" row. Any new EvidenceItem subclass added to the schema surfaces here
without editing this workflow — the renderer extracts the necessary fields
generically and the synthesis subagent populates one row per item.

**Subcluster concordance note (mandatory for supertype candidates):**

Immediately after the property alignment table, add one sentence summarising how many
child clusters of the supertype are concordant for the key properties. Draw this from
the caveats and notes in `edges[*].property_comparisons` — do not invent numbers.
Format: *(N of M child clusters show {property} concordant with classical type; the
remainder are {discordant signal}. Best match: CLUS_XXXX.)*

Example: *(1 of 5 child clusters (CLUS_1915) shows the female-biased Kiss1+Th+ profile;
the remaining 4 are either sex-neutral/male-biased or lack Kiss1 expression.)*

If child-cluster breakdown information is not available in the edge YAML, write:
*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Null result headline (for UNCERTAIN-only mappings)**

If all edges are UNCERTAIN and the UNCERTAIN classification is confirmed by
expression data (e.g. Cyp19a1 = 0.0 in all ARH clusters), the report body must
open with a clear finding statement immediately after the classical type table,
before the mapping candidates table. Example:

> "A complete scan of CCN20230722 (ranks 0 and 1) confirmed that no cluster in
> MBA:223 (Arcuate hypothalamic nucleus) expresses Cyp19a1 at detectable levels.
> SUPT_0427 (ARH primary supertype) shows Cyp19a1 = 0.0; child clusters CLUS_1569,
> CLUS_1570, CLUS_1571 all show Cyp19a1 = 0.0. The best available match (SUPT_0486)
> is in periventricular preoptic zones with no ARH cells."

This is NOT the "Eliminated candidates" section — it is the primary finding.
Use only values from the facts file; do not invent expression values.

### 5. Candidate paragraphs

**MODERATE and LOW edges:** one `###` section each (Note: under the
top-level `## Results` section above, candidate sections use `###` headings.)

Section title: `### {node_b_name} · {confidence_badge}`

Each section must have:

**Supporting evidence** (bulleted):
- For each evidence item where `supports` = SUPPORT or PARTIAL:
  - Be specific — don't just say "atlas metadata". Say what the metadata shows.
  - Cite using the `ref_label` from the evidence item (e.g. `[1]`, `[A]`).
  - For ATLAS_QUERY items: state what filter was applied and what survived/was eliminated.

**Embedded figure** (for any evidence item with `fields.figure_relpath`):
- The renderer auto-generates a δ ranked-bar PNG for each `BulkCorrelationEvidence`
  item with `top_n_hits`. Embed it after the evidence-narrative blockquote using
  standard Markdown:
  ```
  ![{fields.figure_caption}]({fields.figure_relpath})
  ```
- The path is relative to the report file (`figures/{node}_{contrast}_{sha8}.png`).
  Do NOT paraphrase the caption — it's deterministic provenance.
- The figure highlights `is_target` rows in red; the caption already names the
  target. No extra text needed describing the figure — it speaks for itself.

**Top-N hits table** (compact alternative to the figure for screen review):
- For evidence items with `fields.top_n_hits` you may render a compact Markdown
  table after the figure:
  ```
  | Rank | Cluster | Supertype | δ | MFR | Top anatomy |
  |---:|---|---|---:|---:|---|
  | 1 | CLUS_2293 | SUPT_0563 | 0.0180 | — | Ventromedial hypothalamic nucleus |
  | ... | | | | | |
  ```
  Bold or mark `is_target=True` rows. Use this when the figure is enough but a
  precise δ readout helps. For very small reports (≤2 evidence items), skipping
  the table and relying on the figure is fine.
- For property comparisons where `node_a_value` or `notes` contain quantitative expression
  data from direct re-analysis (detection rates, mean counts): mention these numbers in
  the relevant supporting or concern bullet. Direct expression evidence strengthens or
  weakens the property comparison beyond the original literature citation alone.
- If a property is NOT_ASSESSED but source-side expression is now quantified, note the
  gap explicitly: "Source-side confirmed at N%; target-side still unresolvable from atlas
  metadata." This helps readers understand where remaining gaps lie.

**Marker evidence provenance** (bulleted, one per defining_marker, negative_marker,
and neuropeptide — omit if no provenance issues):

For each marker/neuropeptide on the classical node, assess the evidence chain:
- **Method type**: Is the evidence protein-level (IHC, immunofluorescence),
  transcript-level (scRNA-seq, RT-PCR, ISH), or both? State which.
- **Cell type specificity**: Did the study that established this marker actually
  confirm the classical type's identity (e.g. morphological reconstruction,
  Cre-driver targeting, patch-clamp followed by fill)? Or was it tested on a
  broader population (e.g. "Sst+ interneurons in stratum oriens" without
  confirming OLM morphology)? State the basis for believing the study was
  looking at the right cells.
- **Data source discrepancies**: If a marker or neuropeptide appears in one data
  source but not another (e.g. listed in taxonomy metadata neuropeptides but
  at zero in precomputed stats; or reported in literature but absent from atlas
  metadata), note the discrepancy factually. Do not explain it away — present
  both values and flag for investigation.
- **Atlas annotation vs. expression discrepancy (mandatory check)**: For each
  marker or neuropeptide listed as DEFINING, DEFINING_SCOPED, or NEUROPEPTIDE in
  the atlas node's metadata, check whether the corresponding precomputed expression
  value (from `property_comparisons[*].node_b_value`) is near-zero (< 0.5) or
  absent. If so, flag explicitly:
  > ⚠ **Atlas annotation/expression discrepancy**: {gene} is listed as a {DEFINING /
  > NEUROPEPTIDE} marker in WMBv1 atlas metadata for {accession} but shows
  > precomputed mean expression = {value}. This may reflect a neuropeptide annotation
  > derived from a different dataset or resolution level, or a marker that is
  > expressed in a subset of cells below the atlas-level mean. Flag for investigation.
  This is most common for neuropeptides, which are often low-expressed or cell-sparse.
  The discrepancy should also appear in the Concerns list for that candidate.
- **Quantitative cross-check**: If precomputed stats values are available in
  `property_comparisons[*].node_b_value`, note where they confirm or
  challenge the expected marker profile. For negative markers, note any
  clusters where expression is unexpectedly high.
- **Weak or unsourced evidence**: If a marker is listed without a specific
  citation on the classical node, or if all citations are reviews rather than
  primary studies, flag this explicitly.

For markers where the evidence provenance is weak or the cell-type specificity
of the original study is unclear, add a recommendation for targeted literature
search (e.g. "Calb1 as an OLM negative marker lacks a primary citation testing
morphology-confirmed OLM cells — a targeted cite-traverse for 'calbindin
OLM hippocampus' may resolve this").

**Concerns** (bulleted):
- From evidence items where `supports` = REFUTE.
- From DISCORDANT or APPROXIMATE property_comparisons — interpret each:
  - Location APPROXIMATE + adjacent subfield in `notes`:
    add "*(adjacent region — could reflect registration boundary error; weak counter-evidence)*"
  - Location DISCORDANT + distant region in `notes`:
    add "*(distant region — stronger counter-evidence; classical type may still be a
    subtype of this T-type but not the {brain region} population specifically)*"
  - Use your neuroanatomical knowledge to assess distance accurately. Do not rely on
    the notes field alone — check whether the named region (e.g. CA3, amygdala, cortex)
    is adjacent or anatomically distant from the classical type's specified location.
- From `caveats[]` items.

**What would upgrade confidence:**
- Derived from `unresolved_questions[]` and `proposed_experiments[]`.
- Name the specific evidence type that would be added (AnnotationTransferEvidence,
  LiteratureEvidence, PATCH_SEQ, etc.) and any quantitative threshold (e.g. F1 ≥ 0.80).
- Include any targeted literature searches recommended in the marker evidence
  provenance section above — weak marker evidence is a gap that literature
  review can address without new experiments.

**UNCERTAIN edges:** Collapse all into one `## Eliminated candidates` section.

- Check if there is a shared disqualifying signal (same property DISCORDANT across all
  UNCERTAIN edges). If so, state it up front as the primary reason.
- Sub-section per edge: cluster name + n_cells, bullet list of disqualifying evidence.
- For location evidence on eliminated edges, apply the adjacent/distant interpretation rule.
- Note which counter-evidence is weak (adjacent region) vs strong (distant region).

---

## Methods

Methods is a `<details>` fold (per design — limit scrolling on screen review).
The section's audit-trail content draws from `methods_summary` in the facts
JSON; subsections appear only when their underlying evidence is present
(omit `Annotation transfer` if no AT runs, omit `Bulk transcriptomic correlation`
if no BulkCorrelation runs, etc.).

The `### Methods` heading sits OUTSIDE the fold (so the section appears in
the table of contents and the heading remains visible when the fold is
collapsed). The fold's `<summary>` carries a short descriptive label, NOT
another heading:

```markdown
### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>
```

Subsections (omit any whose data is empty):

**Classical type definition.** One paragraph from `classical_nodes[0]`:
defining markers, NT type, soma location, with the `[n]` literature citations
in `classical_nodes[0].location_refs / nt_refs / defining_markers[*].refs` etc.
Mention the `definition_basis` value (CLASSICAL_MULTIMODAL / PRIOR_TRANSCRIPTOMIC /
etc.) so the reader knows what evidentiary base the classical node sits on.

**Atlas mapping query.** Static text:
> Candidate atlas clusters were retrieved from the {atlas_data_sources[0].atlas}
> taxonomy ({atlas_data_sources[0].taxonomy_id}) at ranks 0 (cluster) and 1
> (supertype) using metadata-based scoring (region match, NT type, defining
> markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Static text:
> Each defining property of the classical type was compared to the corresponding
> atlas-side value via the `property_comparisons` schema, with alignments graded
> CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical
> values came from precomputed expression on the cluster (cluster.yaml in the
> taxonomy reference store) and from MERFISH spatial registration for soma
> location.

**Annotation transfer** *(only if `methods_summary.annotation_transfer_runs` is non-empty)*:
For each AT run summary, render a compact table. AT run records may come
from one of two sources:
- New shape (preferred): the evidence carries `run_ref` and the renderer
  populated the run summary from a `kb/annotation_transfer_runs/{run_id}/manifest.yaml`
  record. Run summary has rich provenance (atlas SHA, script Git refs).
- Old shape (back-compat): the evidence has inline `method` / `tool_version`
  fields and no run_ref. Run summary has the inline fields only.

For new-shape runs, render this table (omit any row with empty value):

```
| Field | Value |
|---|---|
| Source dataset | {source_dataset_accession} ({source_cluster_label}) |
| Source species | {source_species} |
| Target atlas | {target_atlas} ({target_taxonomy_id}; SHA-256: {atlas_pseudobulk_sha[:8]}) |
| Method | {method} |
| Tool version | {tool_version} |
| Bootstrap threshold | {bootstrap_threshold} |
| n cells | {n_cells_total} (filtered to {n_cells_after_filter}) |
| Run record | [`kb/annotation_transfer_runs/{run_dir_name}/manifest.yaml`](../../kb/annotation_transfer_runs/{run_dir_name}/manifest.yaml) |
| Script (external) | {script_relpath} ({code_version}) |
| Code reference | [{code_reference}]({code_reference}) |
| F1 matrix | [`{output_relpath}`](../../kb/annotation_transfer_runs/{run_dir_name}/{output_relpath}) |
| Caveats | {caveats} |
```

For old-shape runs, use the simpler bullets:
- Method + tool_version
- Source dataset accession + species
- Target atlas + species (only if cross-species; omit for same-species)
- Best F1 score + level
- Bootstrap threshold + n_cells_total / n_cells_after_filter (if recorded)
- `code_reference` URL as an inline link if present

**Bulk transcriptomic correlation** *(only if `methods_summary.bulk_correlation_runs` is non-empty)*:
For each run summary, render a compact table (or paragraph for a single run) with:

```
| Field | Value |
|---|---|
| Source publication | {citation from bulk_data_sources, with `[n]` ref label} |
| GEO accession | {bulk_data_sources[i].geo_accession} or — |
| Technique | {bulk_data_sources[i].technique} |
| n pools | {bulk_data_sources[i].n_pools} |
| Atlas | {bulk_correlation_runs[i].atlas_taxonomy_id} (SHA-256: {atlas_pseudobulk_sha[:8]}) |
| Statistic | {bulk_correlation_runs[i].statistic_kind} |
| Parameters | {bulk_correlation_runs[i].parameters} |
| Script | [{script_relpath}]({script_git_repo_url}/blob/{script_git_commit}/kb/correlation_runs/{run_dir}/{script_relpath}) |
| Code version | {code_version} |
| Caveats | {caveats} |
```

The Script row builds a permalink from `git_repo_url + git_commit + relpath`;
omit the link if any of those fields are empty (just print `relpath`).

**Atlas data sources.** One row per entry in `methods_summary.atlas_data_sources`:
- Atlas + taxonomy_id + pseudobulk_source path + SHA-256 (full).

**Anti-hallucination.** Static paragraph (verbatim):
> All citations, atlas accessions, ontology CURIEs, and verbatim literature
> quotes in this report are validated against the evidencell knowledge base
> at write time. Authored-prose evidence narratives are validated against
> their source `evidence_items[*].explanation` fields. The pre-write hook
> rejects any unresolvable identifier or unattributed blockquote. Specific
> mapping limitations and caveats are documented per-candidate in the
> Discussion section.

**Reproducibility footer.** Auto-generated at gen time, single line at the
end of the Methods fold (verbatim from `methods_summary`). Format as
italic paragraph, NOT a blockquote (no `quote_key`, would fail the hook):

```markdown
*Generated by evidencell `{methods_summary.framework_version}` at
{methods_summary.gen_timestamp} from
[{methods_summary.kb_graph_file}]({methods_summary.kb_graph_file}).*
```

**Evidence base table** (audit subsection — fold within fold):
Compact table at the bottom of the Methods fold listing every evidence item:
| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_X | LITERATURE; ATLAS_METADATA; BULK_CORRELATION | ... | [1], [3], [7] |

Close the Methods fold:
```markdown
</details>
```

---

## Discussion

This top-level section bundles the "best candidate + caveats" headline,
proposed experiments, and open questions.

### 6. Best candidate + caveats summary

Open the Discussion with one paragraph naming the primary candidate and
its key caveats. Format as a normal paragraph with bold lead (NOT as a
`> ...` blockquote — this is structural framework text, not a literature
quote, so it has no `quote_key` and would fail the hook):

```markdown
**Primary mapping:** {classical_node.name} → {best_edge.node_b_name} [{accession}]
at {confidence} confidence. Key support: {1-2 evidence types}. Key caveats:
{1-2 caveat_type values from the edge's caveats}.
```

If `methods_summary.cl_mapping.cl_term_id` is non-empty, add a follow-up sentence
naming the CL mapping and interpreting the mapping_type:
- **EXACT**: "This classical type maps directly to the Cell Ontology term
  {cl_term_label} [[{cl_term_id}]({ols_url})]."
- **BROAD**: "The Cell Ontology has no specific term for this population;
  {cl_term_label} [[{cl_term_id}]({ols_url})] is the closest ancestor.
  {mapping_notes — verbatim if non-empty}."
- **RELATED**: "{cl_term_label} [[{cl_term_id}]({ols_url})] is a related
  but non-identical Cell Ontology term. {mapping_notes}"
- **NARROW** / other: similar one-line interpretation; include `mapping_notes` verbatim.

If `cl_mapping.cl_term_id` is empty (no CL term assigned), state:
> No Cell Ontology term currently assigned. {Reason from `notes` on the
> classical node, if available — e.g. "Candidate for CL contribution".}

### 7. Proposed experiments and follow-ups

**First, cross-check each proposed experiment against existing evidence items on the same
edge.** If an evidence item already partially or fully addresses a proposed experiment
(e.g. an ANNOTATION_TRANSFER item exists for a proposed "run MapMyCells" experiment),
do NOT list the experiment as if it is still needed. Instead:
- Note what was already done (dataset, method, result).
- State what it resolved and what remains unresolved.
- If a *refined* version of the experiment would still add value (e.g. different source
  dataset, higher-resolution method, targeting a specific cell subset), propose that
  refined version with clear justification for why the completed round was insufficient.

Group remaining experiments by method across all edges. Do not repeat experiments that
differ only in wording.

For each group:
- **What** (method)
- **Target** (quantitative threshold, e.g. F1 ≥ 0.80 at CLUSTER level)
- **Expected output** (which evidence type would be added to KB, e.g. AnnotationTransferEvidence)
- **Resolves** (which edges / which open questions by number)

For annotation transfer experiments: include atlas, tool, expected output format,
and how results would feed back as `AnnotationTransferEvidence`.

### 8. Open questions

Numbered list. Collect from `unresolved_questions[]` across all edges. Deduplicate.
If a question appears on multiple edges, note that.

> The Evidence base audit table previously at section 8 has moved into the
> Methods fold (see "Evidence base table" subsection there). This keeps the
> Discussion focused on interpretation and the audit table closer to its
> reproducibility receipts.

---

## References

`[1]`–`[N]` for literature (PMID as hyperlink to PubMed).
`[A]`–… for atlas queries (query_url as hyperlink labelled "view").

Columns: # | Citation | PMID | Used for.

**Use ONLY entries from `reference_index` in the facts file.**
Do not add references not in `reference_index`.
Do not invent PMIDs or query URLs.

---

## Strict rules

1. Every `[n]` or `[A]` citation MUST correspond to an entry in `facts.reference_index`.
2. Do not write any blockquote or verbatim passage unless it appears in `facts.quotes`
   (verbatim-quote path) OR it directly reproduces an `evidence_items[*].explanation`
   string from `facts.edges[*]` (authored-prose path; see rule 6b).
3. Do not mention any cluster accession, node ID, or UBERON/MBA term not present in facts.
4. You MAY use neuroanatomical knowledge (brain region adjacency, lineage, marker
   specificity) for interpretation — but mark interpretations that go beyond the facts
   with "*(note: ...)*" so the validation subagent can distinguish them from claimed facts.
5. Do not add references from your training knowledge. If a paper seems relevant but
   isn't in `reference_index`, do not cite it.
6. Every blockquote must carry one of two attribution forms:

   **6a. Verbatim-quote path** (for `LiteratureEvidence.snippet` text from `facts.quotes`):
   `> — {First author} et al. {Year}, {Section} · [{n}] <!-- quote_key: {key} -->`
   Copy the `quote_key` exactly from `facts.quotes` for that entry. Do not invent it.

   **6b. Numbered-ref path** (for authored-prose evidence narratives — typically
   from non-LITERATURE evidence with a resolved `ref_label`, e.g. BulkCorrelationEvidence,
   AnnotationTransferEvidence, MarkerAnalysisEvidence):
   `> — {First author} et al. {Year} · [{n}]`
   Use this form when surfacing an `evidence_item.explanation` whose `ref_label`
   is populated. The blockquote body MUST be the verbatim `explanation` text from
   the evidence item — do not paraphrase. The `[n]` MUST appear in the References
   table. No `quote_key` is required (the text is curator-authored prose, not a
   verbatim quote from the cited paper).

   Do not write a blockquote without one of these attribution forms.
7. Every anatomical location (soma location, layer, region) must be written as:
   `Name [PREFIX:ID]`
   using the `id` field from `facts.classical_nodes[].anatomical_location`. Do not invent IDs.
8. Every atlas cluster accession must be written as:
   `Cluster name [accession]`
   using the `node_b_accession` field from `facts.edges`. Do not invent accessions.

## Phase 3 — Verdict block (emit at the end of the report)

After the References section, emit one fenced YAML `verdict:` block per
edge you covered in the report. Each block is wrapped in HTML comment
delimiters identifying the edge by id:

```
<!-- verdict-block-start: {edge_id} -->
` ` `yaml
verdict:
  confidence: HIGH | MODERATE | LOW | UNCERTAIN | REFUTED
  confidence_score: <float, 0.0–1.0>
  rationale: >
    <one or two sentences; format constraints below>
  reconciliation_note: >
    <optional; cross-edge note when calling indistinguishability>
  lit_to_lit_edges:
    - lit_a: <node_id>
      lit_b: <node_id>
      mapping_justification: semapv:CompositeMatching
  unresolved_questions:
    - <string; APPENDED to existing list, not overwriting>
` ` `
<!-- verdict-block-end -->
```

(Replace the spaced backticks `` ` ` ` `` with actual fence backticks; the
spacing here is only to keep the example readable inside this synthesis
prompt.)

The orchestrator runs an anti-hallucination post-write check
(`python -m evidencell.rationale_writeback`) that parses each block and
verifies every quantitative claim in `rationale` against the edge's
structured data. **Any verification failure blocks write-back of all
blocks atomically.** Format your rationale accordingly.

## Rationale format constraints (enforced by the post-write check)

The rationale prose MUST cite specific structured-field references. The
check parses each of the following patterns and verifies them:

- **F1 values** — pattern `F1=0.NN`. Must match an
  `evidence_items[*].metrics_by_level[*].f1_score` rounded to 2 decimals
  on at least one ANNOTATION_TRANSFER evidence item.
- **Accessions** — pattern `CS\w+_(CLUS|SUPT|SUBC|CLAS)_\d+`. Must appear
  on the edge's `taxonomy_type`, in a `property_comparison.node_a_value` /
  `node_b_value`, or in an AT evidence item's `metrics_by_level`.
- **`run_ref` strings** — pattern `at_run_*`. Must appear on an evidence
  item.
- **Marker counts** — pattern `N of M markers CONSISTENT`. Must reconcile
  against the edge's `marker_`-prefixed PropertyComparisons (count them
  yourself before writing).
- **Modality tokens** — `patch-seq`, `scRNA-seq`, `bulk RNA`, `MERFISH`,
  `smFISH`, `immunohistochemistry`, `biocytin`, `electrophysiology`,
  `morphology`, `Cre-line` etc. Must appear in some evidence item's
  `method` / `evidence_type` field, or in a PropertySource's `method`.
  Phase 3 requires modality-aware citations: when claiming convergence
  across techniques (e.g. "AT and morphology agree"), name both modalities
  explicitly so they're checkable.

**Example rationale (good):**

> Reln (F1=0.95 in `at_run_20260408_winterer_olm_mmc_wmbv1`) and Chrna2
> (`marker_Chrna2` CONSISTENT; supported by immunohistochemistry and
> scRNA-seq) anchor the close match to CS20230722_CLUS_0768; 2 of 3
> markers CONSISTENT. `region_fraction` = 0.31 is borderline (caveat).

**Example rationale (bad — no traceable citations):**

> "Strong agreement across multiple lines of evidence."

## When to cite `region_fraction`

Cite `region_fraction` explicitly when it is in the **boundary band**
(roughly 0.3–0.7) and explain whether it drove the relationship choice.
Skip the citation when very high (>0.7) or very low (<0.3) — the
relationship choice implies the value.

## Indistinguishability across source groups (Phase 3 — the #61 pattern)

Read `{pool_candidates_file}`. For each candidate pool, decide whether to
call the source groups indistinguishable:

**CASE A — INDISTINGUISHABLE ACROSS ALL AVAILABLE PANELS** (e.g. Winterer
2019 Sst-OLM / Htr3a-OLM: morphology, ephys, MGE markers, dev markers,
AT all show no distinction):

1. In EACH affected edge's `rationale`, state the broader-call
   indistinguishability and name the panels examined, citing per-panel
   evidence (modality-aware).
2. Set `reconciliation_note` on EACH edge with a structured cross-edge
   reference (e.g. *"indistinguishable from `{sibling_edge_id}` across
   panels [markers, anat, ephys, AT]; see report"*).
3. Emit a `lit_to_lit_edges` entry with the two lit_types and
   `mapping_justification: semapv:CompositeMatching`. The orchestrator
   creates a new MappingEdge with `relationship: skos:closeMatch` and
   `mapping_cardinality: 1:1`.
4. Append `unresolved_questions[]`: *"Consider unifying `{lit_A}` and
   `{lit_B}`; no available data distinguishes them. See #62."*
   (Destructive topology changes — node merge, parent-type creation —
   stay curator-decided.)
5. If applicable, render the merged figure via:
   ```
   just gen-at-figure {run_id} --pool {label_A},{label_B}:{merged_name} \
     --source {label_A},{label_B} \
     --output reports/{region}/figures/f1_for_{merged_name}.png
   ```
   and embed it in the Methods section.

**CASE B — INDISTINGUISHABLE ON AT ONLY** (the other panels are not
assessed in the available evidence):

1. State the AT-only indistinguishability in `rationale`, naming
   explicitly which panels were NOT assessed.
2. Set `reconciliation_note` as in Case A.
3. **Do NOT** emit a `lit_to_lit_edges` entry — insufficient evidence
   for a cross-panel call.
4. **Do NOT** append the "consider unifying" question.

Write the report now.
```

---

## Step 4 — Validation subagent

Spawn a **validation subagent** with this exact prompt (substitute values):

```
You are a report validation agent. Verify that the generated Markdown report contains
no hallucinated identifiers or fabricated quotes.

FACTS FILE: {facts_file}
GENERATED REPORT: {summary_file}

Read both files. Then perform these checks:

1. **Reference completeness**: Extract all [n] and [A] labels from the report.
   For each [n]: confirm it exists as a key in facts.reference_index.
   For each [A]: confirm it exists in facts.reference_index.
   Flag any label whose key is absent from the index.

2. **PMID accuracy**: For each PMID mentioned inline or in the reference table,
   confirm it matches the `pmid` field of the corresponding reference_index entry.
   Flag any mismatch.

3. **Blockquote integrity**: For each blockquote (lines starting with `>`) in the report,
   determine which attribution form it uses by inspecting the attribution line:

   **(a) Verbatim-quote path** — attribution contains `<!-- quote_key: X -->`:
   - PASS if quote_key X exists in facts.quotes AND the blockquote body matches
     facts.quotes[X].text verbatim (exact substring match).
   - FAIL if X is absent from facts.quotes, or if the body is paraphrased/truncated.

   **(b) Numbered-ref path** — attribution contains `[n]` cite without quote_key:
   - PASS if [n] resolves in facts.reference_index AND the blockquote body matches
     verbatim some `evidence_items[*].explanation` string within
     facts.edges (exact substring match — the body is the curator-authored prose
     copied from the YAML).
   - FAIL if [n] is absent from facts.reference_index, or if the body is not
     traceable to any evidence item explanation.

   Blockquotes with neither attribution form FAIL.
   Flag each failing blockquote with which check fired.

4. **Accession / ID integrity**: For each cluster name (e.g. "0769 Sst Gaba_3"),
   cluster accession (e.g. CS20230722_CLUS_0769), UBERON term, or MBA term mentioned
   in the report body: confirm it appears in facts.edges or facts.classical_nodes.
   Flag any term not found.

5. **Interpretation markers**: Check that claims using neuroanatomical knowledge (marked
   with "*(note: ...)*") do not present factual assertions as verified (e.g. "the region
   IS distant" should be marked as interpretation if not stated in facts.quotes).

Output format:

VALIDATION REPORT
=================
[n] references checked: {count}
[A] references checked: {count}
Blockquotes checked: {count}
Accessions/IDs checked: {count}

PASS items: {list by type}

FAIL items:
  - type: hallucinated_ref | fabricated_quote | pmid_mismatch | unknown_accession
    location: {section name + approximate text}
    expected: {what was expected}
    found: {what was in the report}

VERDICT: PASS | FAIL
```

---

## Step 4b — Verdict-block anti-hallucination check (Phase 3)

After Step 4 (the LLM validation subagent) PASSes, run the deterministic
post-write check on the verdict blocks:

```bash
just rationale-writeback {summary_file} {graph_file} --dry-run
```

This:
1. Parses each `verdict:` YAML block from the report.
2. Verifies the rationale's quantitative claims (F1, accessions, run_refs,
   marker counts, modality tokens) against the edge's structured data.
3. Reports what would be written; does not edit the graph.

If verification fails on any block, treat as a synthesis failure (re-run
Step 3 with the failure list in the prompt, capped at 1 retry). The check
is atomic: a single failure blocks write-back of all blocks.

---

## Step 5 — Accept and write back

### If both Step 4 (LLM) and Step 4b (verdict check) PASS:

Run the write-back to commit the verdict + currency hash to the
MappingEdge YAML:

```bash
just rationale-writeback {summary_file} {graph_file}
```

This writes back to each covered edge:

- `rationale`, `confidence`, `confidence_score` from the verdict block.
- `reconciliation_note` if set.
- `rationale_generated_at` (now, UTC ISO).
- `report_path` (relative to repo root).
- `rationale_source_hash` — SHA256 8-char digest over the canonical
  edge + endpoint-node payload (excluding the rationale-suite output
  fields themselves). On subsequent reads / `just qc`, the hash is
  recomputed and compared; mismatch flags the rationale as stale.

When the verdict block carries `lit_to_lit_edges`, the writer creates
new `MappingEdge`s with `relationship: skos:closeMatch`,
`mapping_cardinality: "1:1"`, and the supplied justification.

Pre-edit hook fires on the write and runs structural + LinkML schema
validation. Hook rejection blocks the write atomically.

Print:
```
Report accepted: {summary_file}
Validation: PASS — {N} references, {M} blockquotes, {K} accessions verified.
Write-back: {n_edges} verdict(s) written, {n_lit_to_lit} lit-to-lit edge(s) created.
  Hash(es): {edge_id} → {8-char hash}
```

Delete the `{node_id}_facts.json` and `{node_id}_pool_candidates.json`
intermediate files.

Print the full path of the generated report for the curator.

### If validation verdict is FAIL:

Print the full validation failure list. Do NOT present the report as accepted.

Determine whether failures are:
- **Fixable by re-running synthesis**: hallucinated reference, fabricated quote, missing
  interpretation marker → re-run Step 3 with an added instruction to the synthesis agent
  highlighting the specific failure. Limit to 1 retry.
- **Fixable by updating YAML or references.json**: quote_key missing from references/{region}/references.json,
  PMID mismatch in YAML → inform curator of the specific YAML field to fix, then stop.
- **Systematic / unclear**: stop and ask the curator what to do.

---

## Drill-down mode (mode = "drilldowns")

If `mode` is "drilldowns" or "all", after generating and accepting the summary report,
also generate per-paper drill-downs for each LITERATURE evidence item in the node's edges.
Also include papers cited only in node marker sources (not just edge evidence items).

For each unique PMID/corpus_id:

### Step DD-1 — Generate scaffold

Run:
```bash
just gen-drilldown-pmid {graph_file} {node_id} {pmid}
```

This writes `reports/{region}/{node_id}_drilldown_{AuthorYear}.md` with verbatim quotes
from `references/{region}/references.json` and a flat evidence summary table. Confirm the file exists.

### Step DD-2 — Drill-down synthesis subagent

Spawn a **drill-down synthesis subagent** with this exact prompt (substitute values for
`{scaffold_file}`, `{facts_file}`, `{output_file}`, `{region}`, `{pmid}`):

```
You are a cell type mapping drill-down report writer. You write a human-readable
evidence drill-down for a single paper, using structured facts and verbatim quotes.

SCAFFOLD FILE: {scaffold_file}       # programmatic drill-down with verbatim quotes
FACTS FILE: {facts_file}             # {node_id}_facts.json — full edge structure
OUTPUT FILE: {output_file}           # overwrite the scaffold with the enriched version

First, read both files completely. Then write the report below.

---

## Report structure (follow exactly, in this order)

### 1. Header

```
# Evidence Drill-down: {Author} et al. {Year}
*Supporting: {edge descriptions from scaffold — copy exactly}*
*[← Back to summary report]({summary_filename})*
```

Then a blank line, `---`, blank line.

Then the full citation block:
```
**{Authors full list}**
{Title}
*{Journal}* {Volume}:{Pages}, {Year} · PMID:{pmid} · {DOI if present}
```

If a GEO, SCP, or NeMO dataset accession appears in `facts.quotes[*].claims`, add it
as a named link: e.g. `· [GEO:GSE124847](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124847)`

### 2. Why this paper matters for this mapping

Write 2–4 sentences covering:
- **Methodology**: what the paper actually did (e.g. "performed scRNA-seq on
  morphologically reconstructed neurons", "used Cre-driver lines to target specific
  populations", "combined patch-clamp with single-cell sequencing")
- **Evidential strength**: why this method produces strong evidence for the mapping
  (e.g. "provides a direct bridge between the classical anatomical definition and the
  transcriptomic signature — cells were included only after post-hoc morphological
  verification of OLM identity")
- **What it uniquely adds**: what this paper resolves that atlas metadata alone cannot
  (e.g. "resolves the prior NPY discrepancy between rat and mouse")
- **Dataset availability** (if applicable): if a dataset accession is in the scaffold,
  name it as an actionable resource: "The raw data (GEO:GSE124847) are available for
  direct re-mapping to WMBv1."

Use only information from the scaffold or facts file. Do not invent findings.

### 3. Per-property evidence sections

Group quotes by property type. Order: **markers first, then NT, neuropeptides, lineage/
developmental, morphology/electrophysiology, other**.

For each quote from the scaffold, write a sub-section:

```
### {Property name} · alignment with {atlas_cluster_short_name}: {ALIGNMENT}
```

Where:
- `{Property name}` = the marker symbol, NT name, or property label
  (e.g. "Chrna2", "GABAergic identity", "Npy", "MGE origin / Lhx6")
- `{atlas_cluster_short_name}` = abbreviated cluster name from the best edge
  (e.g. "0769 Sst Gaba_3")
- `{ALIGNMENT}` = from `facts.edges[best_edge].property_comparisons[property].alignment`

If a quote covers multiple properties, split it into the most relevant section; mention
the others in that section's interpretation paragraph.

Under each sub-section header:
1. Copy the blockquote verbatim from the scaffold (do NOT modify the text):
   ```
   > {exact text from scaffold}
   > — {section}
   ```
2. Write an **interpretation paragraph** covering:
   - What the finding shows for this property
   - Why the alignment label is correct:
     * CONSISTENT: explain how the paper finding matches the atlas cluster's profile
     * APPROXIMATE: explain the scatter (e.g. expression across supertype not specific
       to one cluster) or adjacent-region spread. Use the standard wording:
       "*(adjacent region — could reflect registration boundary error; weak counter-evidence)*"
     * DISCORDANT: identify what the paper shows that conflicts with the cluster.
       Use the standard wording: "*(distant region — stronger counter-evidence;
       the classical type may still be a subtype of this T-type but not the
       {region} population specifically)*"
     * NOT_ASSESSED: explain what prevents assessment (e.g. "protein-level data;
       atlas metadata records only transcript-level markers")
   - **Use your neuroanatomical knowledge** to assess whether an off-target region is
     adjacent or distant. Do not rely on the notes field alone — verify:
     * Adjacent: CA3 next to CA1; prosubiculum at CA1 border; stratum radiatum
       bordering stratum oriens; etc.
     * Distant: amygdala vs. hippocampus; cortex vs. striatum; cerebellum vs.
       hippocampus; etc.
   - **Species/context caveats** when relevant:
     * If the quote reports rat or primate data and the atlas is mouse, flag the
       species gap: "*(note: this finding is from rat — cross-species differences
       exist for this marker; see mouse data below)*"
     * If this paper overturns a prior exclusion criterion (e.g. Npy previously
       used to exclude OLM identity), name the prior work and explain the resolution
   - **Mapping relevance**: what this finding means specifically for the candidate
     atlas cluster(s). If the same property is relevant to multiple edges, note that.

Mark any interpretation that goes beyond the facts file with "*(note: ...)*" so the
validation subagent can distinguish it from stated facts.

### 4. Summary scorecard

Table: one row per property covered, in the same order as the sections above.

```
| Property | Paper finding | Atlas alignment | Quote key |
|---|---|---|---|
| Sst | consistent expression | CONSISTENT | {quote_key from scaffold} |
| Npy | consistent; protein confirmed | CONSISTENT | {quote_key} |
...
```

- **Property**: marker symbol or property name
- **Paper finding**: 3–8 word summary of what the paper shows (no quotes)
- **Atlas alignment**: from `facts.edges[*].property_comparisons` — use CONSISTENT /
  APPROXIMATE / DISCORDANT / NOT_ASSESSED
- **Quote key**: from the scaffold's evidence summary table (e.g. `201041756_9991ee9f`)

### 5. Critical gap

Write 1–3 sentences:
- What this paper **does not resolve** for the mapping (e.g. "did not map their cells
  to WMBv1 directly")
- The **specific bridging experiment** needed, naming method + tool + threshold
  (e.g. "The connection requires Chrna2-Cre driver line + MapMyCells at F1 ≥ 0.80 at
  CLUSTER level — see Proposed experiments in the summary report")
- If a dataset accession was identified above, name it as an available starting point:
  "GEO:GSE124847 data are available for direct re-mapping without new experiments."

### 6. Footer

```
---

*Drill-down generated from: references.json (corpus_id: {corpus_id})*
*Quotes: {source_method}, {status} (added {date})*
```

Copy the footer line verbatim from the scaffold.

---

## Strict rules

1. Every blockquote (`>` line) must be copied **verbatim** from the scaffold.
   Do not paraphrase, truncate, or rephrase quotes. If the scaffold has a quote, include
   it exactly; do not substitute it with a different passage you know from training data.
2. Every alignment label (CONSISTENT/APPROXIMATE/DISCORDANT/NOT_ASSESSED) must match
   the corresponding `facts.edges[*].property_comparisons[*].alignment` value.
3. Do not cite any paper, PMID, or accession not present in the scaffold or facts file.
4. Do not add new references from training knowledge. If a paper is relevant but absent
   from the facts file, do not cite it; instead note the gap in the Critical gap section.
5. Mark all neuroanatomical interpretations that go beyond the facts file with
   "*(note: ...)*" so they are clearly distinguishable from stated facts.
6. Use the **exact wording** for location alignment interpretation as specified above
   (adjacent region / distant region standard phrases) — this ensures consistency with
   the language used in the summary report and the edge YAML.
7. Every blockquote must have an attribution line immediately after it:
   `> — {First author} et al. {Year}, {Section} <!-- quote_key: {key} -->`
   Copy the `quote_key` exactly from the scaffold's `<!-- quote_key -->` comment.
   Do not modify or invent quote keys. Do not write a blockquote without this line.
8. Every anatomical location must be written as `Name [PREFIX:ID]` using the ID from
   the scaffold or facts. Every atlas cluster accession must appear in brackets:
   `Cluster name [accession]`. Do not invent IDs or accessions.

Write the report now. Overwrite {output_file}.
```

### Step DD-3 — Validation

Run the same validation subagent (Step 4) on the drill-down output:
- Check all blockquotes appear verbatim in `facts.quotes` or in the scaffold
- Check no PMIDs or accessions were invented
- PASS → accept; FAIL → retry once with specific correction, then stop and ask curator

---

## Notes for the coordinator

- The synthesis subagent uses your (Claude's) neuroanatomical knowledge to interpret
  location alignment. This is appropriate — the latent knowledge of brain region
  adjacency is well-established and not a hallucination risk. The validation step
  checks that factual claims (IDs, quotes, PMIDs) are grounded; interpretive statements
  marked with "*(note: ...)*" are exempt from ID-level validation.

- The `facts.json` file is the single source of truth passed to the synthesis agent.
  It contains only what is provably in the YAML. If a fact is missing from the facts
  file but the curator believes it should be there, the fix is to add it to the YAML
  and re-run `just gen-facts` — not to ask the synthesis agent to include it anyway.

- Reports are not committed to git by default (`reports/` is gitignored).
  Pin a dated snapshot at release time by removing it from .gitignore.

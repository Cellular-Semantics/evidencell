# Taxonomy Ingestion Orchestrator

You are a taxonomy ingestion coordinator. You read a source taxonomy file,
propose a mapping of its fields to the evidencell schema, gate on human approval,
then generate CellTypeNode stubs. You delegate to focused subagents with exact
prompts. Data flows through files on disk, not through context windows.

**Scope**: Initial ingestion only — creating CellTypeNode stubs from a new
taxonomy source. Subsequent enrichment (adding new columns, updated registrations,
additional analysis outputs) is out of scope; handle those as manual edits or a
future `enrich-nodes` workflow.

---

## Run parameters

```
PARAMS:
  taxonomy_file: ""           # path to source file (required)
  output_dir: ""              # research/{region}/ — inferred from taxonomy metadata
                              # or specified by user; confirm before writing
  target_level: "all"         # which taxonomy level(s) to ingest: "all", "cluster",
                              # "supertype", "subclass", etc. Default: all levels.
  model: "sonnet"
```

When the user provides the file path, resolve `output_dir` from the taxonomy
metadata if possible (atlas name, region). If ambiguous, ask before proceeding.

---

## Pre-Step 0a: Taxonomy metadata check

Before inspecting the source file, check whether a metadata input file exists:

```
METADATA_INPUT = inputs/taxonomies/{taxonomy_id}_meta.yaml
```

**If the file exists:** read it and show a compact summary to the human:
```
TAXONOMY METADATA INPUT: {taxonomy_id}
  Name:              {taxonomy_name}
  Species:           {species_label} ({species_id})
  Tissue:            {tissue_label} ({tissue_id})
  Anatomy ontology:  {anatomy_ontology}
  MapMyCells:        {at_taxonomy_id} (S3 URLs present: yes/no)
  Source query:      {source_query}
```
Ask: "Metadata confirmed? (yes / edit first)"
- Yes: proceed using this metadata during ingest.
- Edit: pause, let the human edit the file, then re-read.

**If the file does not exist:**
Prompt the human for the following fields:
- Taxonomy name (e.g. "WMBv1 (Whole Mouse Brain v1)")
- Species (NCBITaxon CURIE + label, e.g. NCBITaxon:10090 / Mus musculus)
- Tissue (UBERON CURIE + label, e.g. UBERON:0000955 / brain)
- Anatomy ontology used for location data (e.g. MBA, DHBA — or "unknown")
- MapMyCells at_taxonomy_id (if this taxonomy is supported by MapMyCells)
- MapMyCells S3 URLs (stats + markers) if known — can be null
- Source query file path (for KG-backed taxonomies)

Write the metadata input file to `inputs/taxonomies/{taxonomy_id}_meta.yaml` before
proceeding. This file persists and will be used automatically on future re-ingests.
Show a template and ask the human to fill any blanks, or allow them to provide just
the name and proceed with nulls for the rest.

---

## Pre-Step 0b: Fast-path check for known taxonomy

Before running any inspection subagent, check whether a confirmed field mapping already
exists for this taxonomy:

```
FAST_PATH_CONFIG = kb/taxonomy/{taxonomy_id}/field_mapping.json
```

**If the file exists and contains `"confirmed": true`:**

1. Read the file and show the human a compact summary:
   ```
   KNOWN TAXONOMY: {taxonomy_id}
   Source format: {source_format}
   Levels: {taxonomy_level_extraction.levels}
   Field mapping: confirmed on prior ingest
   ```
2. Ask: "Confirmed field mapping found for `{taxonomy_id}`. Proceed with existing
   mapping, or re-inspect the file? (yes to proceed / re-inspect to run inspection)"
3. If the human says yes (or similar): skip Step 0 entirely and jump to Step 2
   (stub generation), passing the existing `field_mapping.json` as the confirmed mapping.
4. If the human requests re-inspection: continue to Step 0 below.

**If the file does not exist or is not confirmed:** continue to Step 0.

---

## Step 0: Detect format and run inspection subagent

1. Check the file extension and peek at the first ~100 bytes to determine format.

2. **If the file is JSON and contains `cellannotation_schema_version` or both
   `annotations` and `labelsets` at the top level**: it is CellAnnotation Schema
   (CAS) format. Run the **CAS inspection subagent** (see §CAS path below).

3. **All other formats** (CSV, TSV, Excel, YAML, JSON without CAS structure,
   or anything else): run the **general inspection subagent** (see §General path).

4. After inspection returns, proceed to Step 1 (gate).

---

## §CAS path — CAS inspection subagent

Spawn a single subagent with this exact prompt (fill in `{taxonomy_file}`,
`{output_dir}`, `{target_level}`):

```
You are a taxonomy inspection agent working with a CellAnnotation Schema (CAS) file.

FILE: {taxonomy_file}
OUTPUT DIR: {output_dir}
TARGET LEVEL: {target_level}

TASK:

1. Parse the file using cas-tools:
   uv run --with cas-tools python3 -c "
   from cas.model import CellTypeAnnotation
   import json, sys
   with open('{taxonomy_file}') as f:
       data = json.load(f)
   cas = CellTypeAnnotation(**data)
   print('title:', cas.title)
   print('labelsets:', [(ls.name, ls.rank) for ls in cas.labelsets])
   print('total annotations:', len(cas.annotations))
   # Sample first annotation of each labelset
   by_labelset = {}
   for ann in cas.annotations:
       by_labelset.setdefault(ann.labelset, []).append(ann)
   for ls, anns in by_labelset.items():
       print(f'\\n=== {ls} (sample) ===')
       a = anns[0]
       print('  cell_label:', a.cell_label)
       print('  cell_set_accession:', a.cell_set_accession)
       print('  cell_ontology_term_id:', a.cell_ontology_term_id)
       print('  parent_cell_set_accession:', a.parent_cell_set_accession)
       print('  marker_gene_evidence:', a.marker_gene_evidence[:5] if a.marker_gene_evidence else None)
       aaf = a.author_annotation_fields or {}
       print('  author_annotation_fields keys:', list(aaf.keys()))
       print('  sample aaf:', {k: aaf[k] for k in list(aaf.keys())[:6]})
   "

2. From the output, build a field mapping table. CAS fields map as follows
   (these are HIGH confidence — do not second-guess them):

   CAS field                           → evidencell field
   ──────────────────────────────────────────────────────
   cell_set_accession                  → node_id
   cell_label                          → name
   parent_cell_set_accession           → parent_id
   labelset (+ labelsets[].rank)       → taxonomy_level (use labelset name as free text)
   cell_ontology_term_id               → cell_ontology_term.id (HIGH — already CL)
   cell_ontology_term                  → cell_ontology_term.label
   rationale                           → definition_references (as note; DOIs extracted separately)
   rationale_dois                      → definition_references (list of DOIs)
   marker_gene_evidence                → defining_markers (aggregate; see below)

3. Inspect author_annotation_fields keys across ALL annotations (not just the sample).
   Collect the full set of unique keys. For each key, make a confident classification:

   CLASSIFICATION GUIDE for author_annotation_fields:
   - Keys containing "neurotransmitter" or "nt" or "NT" → map to nt_type (MODERATE)
   - Keys containing "neuropeptide" or "np" or "NP" → map to neuropeptides (MODERATE)
   - Keys containing "region", "dissection", "location", "anatomy" → map to anatomical_location (MODERATE)
   - Keys containing "marker" or "gene" (beyond marker_gene_evidence) → POTENTIAL_ENRICHMENT
     (additional marker evidence — aggregate with marker_gene_evidence, note source key)
   - Keys containing "transfer" or "label" or "MTG" → POTENTIAL_ENRICHMENT
     (cross-taxonomy annotation transfer reference — potentially useful for map-cell-type)
   - QC/technical keys (UMI, fraction, doublet, spliced, mitochondrial, donor counts,
     cell counts, etc.) → POTENTIAL_ENRICHMENT (not biologically defining)
   - Keys with sex or F/M proportions that are extreme (e.g. >0.9 one sex) →
     SCHEMA_CANDIDATE (sex_bias: biologically meaningful, could be optional schema field)
   - Keys you cannot confidently classify → UNCERTAIN (describe your best guess)

4. For markers: aggregate marker_gene_evidence plus any author_annotation_fields
   keys classified as marker-related into one unified list. For each gene, note
   which source key(s) it came from. Prefer marker_gene_evidence as primary.
   If a key is clearly "scoped" (markers distinctive within a parent group, not
   globally), flag it as high-mapping-value.

5. Write field_mapping.json to {output_dir}/:
   {
     "source_file": "{taxonomy_file}",
     "format": "CAS",
     "cas_version": "...",
     "title": "...",
     "labelsets": [{"name": "...", "rank": N}, ...],
     "target_level": "{target_level}",
     "field_mappings": [
       {
         "source_field": "cell_set_accession",
         "target_field": "node_id",
         "confidence": "HIGH",
         "notes": null
       },
       ...
     ],
     "author_annotation_field_mappings": [
       {
         "source_key": "Neurotransmitter auto_annotation",
         "classification": "nt_type",
         "confidence": "MODERATE",
         "notes": "auto-annotation field; review values for accuracy"
       },
       {
         "source_key": "sex_bias",
         "classification": "SCHEMA_CANDIDATE",
         "candidate_field_name": "sex_bias",
         "rationale": "extreme sex bias may be biologically defining for some types",
         "notes": "flag for schema discussion; preserve as YAML comment for now"
       },
       ...
     ],
     "marker_aggregation": {
       "primary_source": "marker_gene_evidence",
       "additional_sources": ["Top Enriched Genes"],
       "scoped_sources": [],
       "strategy": "aggregate all; note source per gene as YAML comment"
     }
   }

RETURN:
One-line summary: "CAS file parsed. N annotations across M labelsets. Field mapping
written to {output_dir}/field_mapping.json. SCHEMA_CANDIDATE fields: [list]. UNCERTAIN
fields: [list]."

DO NOT write any KB YAML files. DO NOT proceed past field mapping.
```

---

## §General path — general inspection subagent

Spawn a single subagent with this exact prompt (fill in `{taxonomy_file}`,
`{output_dir}`, `{target_level}`):

```
You are a taxonomy inspection agent. Your job is to read an unfamiliar taxonomy
file and propose a field→schema mapping. The file may be in any format. You do
not know in advance what columns it contains or how it is structured.

FILE: {taxonomy_file}
OUTPUT DIR: {output_dir}
TARGET LEVEL: {target_level}

TASK:

1. Read the file and determine its structure:
   - For CSV/TSV: read headers and first 3-5 rows
   - For Excel: list sheet names; read headers and first 3-5 rows of the main sheet
   - For YAML/JSON (non-CAS): read top-level structure, first 2-3 records
   - For anything else: read the first ~50 lines and describe what you see

   Use uv run python3 for parsing. For Excel, use: uv run --with openpyxl python3

2. Look for these biological concepts — they may be encoded in ANY naming convention:

   ACCESSIONS: A stable unique ID for each cell type. Look for: any column that
   looks like a code or ID (alphanumeric with underscores, a counter, a CCN-style
   string like CS+digits+_+type). There may be one per taxonomy level (cluster,
   supertype, subclass, class, etc.). If multiple ID columns exist, map the most
   granular to node_id and note the others.

   HIERARCHY: How types relate to each other. Look for: parent columns, columns
   that repeat values across rows suggesting grouping, level/rank fields, or
   columns whose names suggest a broader grouping of the same thing (e.g. if
   there's a "cluster" and a "supertype" and a "class" column, that's a hierarchy).

   CELL TYPE NAMES / LABELS: The human-readable name. May be separate from the ID,
   or may be the only identifier. Map to `name`.

   TAXONOMY LEVEL: Which level of resolution this row represents (cluster,
   supertype, subclass, etc.). May be explicit (a "level" column), encoded in the
   accession format, or implied by the file structure (one file = one level).

   CL TERMS: Cell Ontology identifiers. Look for: columns containing "CL:" prefix
   values, "cell_ontology", "cl_id", or similar.

   NEUROTRANSMITTER (NT): The primary NT phenotype. Look for: columns named
   "neurotransmitter", "nt_type", "nt", "transmitter", or values like "Glut",
   "GABA", "Glut-GABA". May be abbreviated. Map to `nt_type`.

   NEUROPEPTIDES (NP): Peptide co-transmitters. Look for: "neuropeptide", "np",
   "peptide" columns, or gene lists that are clearly peptide-encoding (Sst, Cck,
   Vip, Cartpt, etc.). Map to `neuropeptides`.

   MARKERS: Genes that characterise the type. Look for: columns named "markers",
   "marker_genes", "defining_genes", "top_genes", or comma-separated gene symbol
   lists. There may be multiple marker columns of different types (TF markers,
   MERFISH markers, combo markers, scoped markers). Aggregate into one list but
   note source column per gene. Scoped markers (distinctive within a parent group)
   are especially valuable for mapping — flag them.

   LOCATION / ANATOMY: Where the type is found. Look for: columns with "region",
   "anatomy", "spatial", "CCF", "location", "annotation", or values that look like
   brain area abbreviations (STR, GPi, CTX, etc.). CCF proportional formats like
   "STR:0.9,Adj:0.1" are common — map to `anatomical_location` with a note about
   the format.

   LITERATURE: Source references for the type definition. Look for: DOI, PMID,
   "rationale", "literature", "reference", "citation" columns. Map to
   `definition_references`.

3. For each column you find, make a confident classification. If a column clearly
   maps to one of the above concepts, say so with HIGH or MODERATE confidence.
   Do not hedge everything — make a best-effort call and explain your reasoning.

   For columns that do NOT map to the above concepts, classify as one of:
   - POTENTIAL_ENRICHMENT: biologically interesting, not currently in schema,
     preserve as YAML comment (examples: cross-taxonomy labels, embedding info,
     colour codes, display order, size metrics)
   - SCHEMA_CANDIDATE: biologically meaningful enough that it might warrant an
     optional schema field (example: sex_bias if values indicate strong sex
     specificity; donor_count; cell_count). Flag with a rationale.
   - TECHNICAL: QC/pipeline metadata with no biological meaning for mapping
     (doublet scores, UMI counts, fraction unspliced, etc.) — skip, do not
     preserve
   - UNCERTAIN: you cannot confidently classify it — describe what it looks like
     and your best guess

4. Note the file structure:
   - Is this one row per finest-level type (denormalised), one row per node at
     one level, or a nested structure?
   - If denormalised (multiple hierarchy levels in one row): note which columns
     belong to which level

5. Write field_mapping.json to {output_dir}/:
   {
     "source_file": "{taxonomy_file}",
     "format": "CSV" | "Excel" | "YAML" | "JSON" | "other: ...",
     "structure": "one row per cluster (denormalised)" | "one row per node" | "...",
     "target_level": "{target_level}",
     "field_mappings": [
       {
         "source_field": "<column name or key path>",
         "target_field": "<evidencell field name, or POTENTIAL_ENRICHMENT / SCHEMA_CANDIDATE / TECHNICAL / UNCERTAIN>",
         "confidence": "HIGH" | "MODERATE" | "LOW",
         "notes": "<reasoning, or null>"
       }
     ],
     "schema_candidates": [
       {
         "source_field": "...",
         "candidate_field_name": "...",
         "rationale": "...",
         "example_values": [...]
       }
     ],
     "marker_aggregation": {
       "primary_source": "<most specific/scoped marker column>",
       "additional_sources": [...],
       "scoped_sources": [...],
       "strategy": "aggregate all; note source per gene as YAML comment"
     },
     "structure_notes": "..."
   }

RETURN:
One-line summary: "Format: X. Structure: Y. N columns mapped (H HIGH, M MODERATE,
L LOW). SCHEMA_CANDIDATE: [list]. UNCERTAIN: [list]. Field mapping written to
{output_dir}/field_mapping.json."

DO NOT write any KB YAML files. DO NOT proceed past field mapping.
```

---

## Step 1: [GATE] Human reviews and corrects mapping

After the inspection subagent returns:

1. Read `{output_dir}/field_mapping.json`.
2. Present the mapping table to the human in a readable format:

```
PROPOSED FIELD MAPPING
======================
Source field                      → Target field                    Confidence
──────────────────────────────────────────────────────────────────────────────
cell_set_accession                → node_id                         HIGH
cell_label                        → name                            HIGH
parent_cell_set_accession         → parent_id                       HIGH
Neurotransmitter auto_annotation  → nt_type                         MODERATE  ⚠
nt_type_combo_label               → nt_type (duplicate — confirm)   MODERATE  ⚠
np.markers                        → neuropeptides                   MODERATE  ⚠
CCF_acronym.freq                  → anatomical_location             MODERATE  ⚠
                                    (proportional CCF format)
rationale_dois                    → definition_references           HIGH
colour_hex                        → [POTENTIAL_ENRICHMENT]          —
Number of cells                   → [POTENTIAL_ENRICHMENT]          —
sex_bias                          → [SCHEMA_CANDIDATE]              —         🔵
Transferred MTG Label             → [POTENTIAL_ENRICHMENT]          —

SCHEMA_CANDIDATE fields (may warrant optional schema addition):
  sex_bias — strong sex specificity may be biologically defining. Add as
             optional schema field, or preserve as YAML comment?

UNCERTAIN fields (need your input):
  embedding_set — unclear purpose, looks like a grouping label
```

3. Ask:
   > "Please review this mapping. Correct any rows where the target field is wrong,
   > mark any POTENTIAL_ENRICHMENT field as SKIP if you don't want it preserved,
   > and tell me what to do with SCHEMA_CANDIDATE fields (add as comment / flag
   > for schema discussion / skip). Ready to proceed?"

4. Apply any corrections. Update `field_mapping.json` with the confirmed mapping.
   Add `"confirmed": true` to the top level.

---

## Step 2: Stub generation subagent

After mapping is confirmed, spawn a single subagent with this exact prompt
(fill in all variables from `field_mapping.json` and run context):

```
You are a taxonomy stub generation agent. You produce CellTypeNode YAML stubs
from a confirmed field mapping. You perform ONLY the steps below.

SOURCE FILE: {taxonomy_file}
FIELD MAPPING: {output_dir}/field_mapping.json
OUTPUT DIR: {output_dir}
TARGET LEVEL: {target_level}

TASK:

1. Read the confirmed field_mapping.json. Read the source taxonomy file.

2. For each taxonomy node at TARGET_LEVEL (or all levels if target_level="all"):
   produce a CellTypeNode stub in this form:

   - node_id: {cell_set_accession or equivalent}
     name: "{cell type label}"
     node_type: ATLAS_TRANSCRIPTOMIC
     atlas: "{infer from file metadata or taxonomy title}"
     taxonomy_id: "{taxonomy_id if present}"
     cell_set_accession: "{cell_set_accession}"
     parent_id: "{parent_cell_set_accession if present}"
     taxonomy_level: "{labelset name or level label}"
     cell_ontology_term:          # leave null if not present in source
       id: null
       label: null
     nt_type:                     # from confirmed NT field, or null
       name_in_source: "{verbatim source value}"
       cl_terms: []               # leave empty — CL lookup deferred
     neuropeptides: []            # from confirmed NP field, gene symbols only
     defining_markers:
       - symbol: "{gene}"
         ncbi_gene_id: null       # leave null — ID resolution deferred
         # sources: {comma-separated list of source columns this gene appeared in}
     negative_markers: []
     anatomical_location: []      # leave empty — complex; preserve source as comment
     definition_references: []    # from rationale_dois or literature fields if present
     evidence: []
     # --- source data preserved below ---
     # {POTENTIAL_ENRICHMENT fields: one comment per field, format: # {key}: {value}}
     # {SCHEMA_CANDIDATE fields: # SCHEMA_CANDIDATE {field_name}: {value} — {rationale}}
     # anatomical_location source: # anatomy_source: "{verbatim CCF or region string}"

3. Group nodes by region/subregion where possible. Write one YAML file per
   region (or one file if region is unclear). File naming: {region_slug}.yaml.
   Use the existing KB examples in kb/draft/ as structural reference.

4. At the top of each output file, add a header block:
   # Taxonomy: {title}
   # Source: {taxonomy_file basename}
   # Ingested: {today's date}
   # Status: STUB — evidence lists empty; accession lookup, CL terms, and
   #         anatomical_location to be completed before graduation to kb/mappings/
   # SCHEMA_CANDIDATE fields preserved as comments — see field_mapping.json

5. Write files to {output_dir}/.

RETURN:
"Stubs written: {list of files}. Nodes generated: N. SCHEMA_CANDIDATE fields
preserved as comments: [list]. Fields skipped: [list]."

DO NOT modify field_mapping.json. DO NOT write to kb/mappings/.
DO NOT run linkml-validate (stubs will not yet pass — that is expected).
```

---

## Step 3: [GATE] Human reviews stubs

After generation:

1. Report the files written and node count.
2. Say:
   > "Stubs written to {output_dir}/. Please open and review before proceeding.
   > When ready, run `just validate-draft` to see what the schema validator reports
   > (failures are expected at this stage — accessions, CL terms, and anatomy
   > are incomplete). When you are satisfied with the structure, reply 'proceed'
   > to build the taxonomy reference DB."

3. Do not proceed autonomously. Wait for the human.

---

## Step 4: Build taxonomy reference DB

After human approves stubs, determine the source format from `field_mapping.json`
`"source_format"` value and route accordingly:

---

### Route A — KG export JSON (source_format starts with "JSON")

The source file is a VFB graph export already on disk. Run directly:

```
just ingest-taxonomy-db {taxonomy_file} {taxonomy_id}
```

This runs two steps in sequence:
1. `just ingest-taxonomy-yaml {taxonomy_file} {taxonomy_id}` — streams the source JSON
   through `evidencell.taxonomy_db`, generates compact YAML reference files under
   `kb/taxonomy/{taxonomy_id}/` (one file per level + enriched `taxonomy_meta.yaml`
   read from `inputs/taxonomies/{taxonomy_id}_meta.yaml` if present)
2. `just build-taxonomy-db {taxonomy_id}` — reads those YAML files and builds a SQLite
   query index at `kb/taxonomy/{taxonomy_id}/{taxonomy_id}.db`

---

### Route B — KG-backed with cypher file (source_format == "cypher")

The source is a `.cypher` file; the JSON has not been fetched yet (or may be stale).

Ask the human: "Fetch fresh from KG, or use cached JSON if present?"

**Option A — Re-fetch:**
```
just fetch-taxonomy-kg {cypher_file} {taxonomy_id}
```
This queries `bolt://localhost:7687` and writes `inputs/taxonomies/{taxonomy_id}.json`.
Then run:
```
just ingest-taxonomy-db inputs/taxonomies/{taxonomy_id}.json {taxonomy_id}
```

**Option B — Use cached JSON** (`inputs/taxonomies/{taxonomy_id}.json` exists):
```
just ingest-taxonomy-db inputs/taxonomies/{taxonomy_id}.json {taxonomy_id}
```

Note: `just fetch-taxonomy-kg` requires the [kg] optional dep group and a running
local neo4j KG. If the KG is not available, use Option B with a previously exported JSON.

---

### Route C — Ad hoc (CSV, XLSX, non-VFB JSON)

The source is not a KG export. Invoke the ad hoc YAML-writing steps from
`workflows/ingest-adhoc-taxonomy.md` (Steps 2–4), passing the already-confirmed
`field_mapping.json` from Step 1 of this orchestrator.

Tell the agent: "Run workflows/ingest-adhoc-taxonomy.md with taxonomy_id={taxonomy_id},
source_file={taxonomy_file}, field_mapping=already confirmed in Step 1."

---

### All routes: anatomy closure

After the DB is built (any route), build the anatomical region closure tables if the
taxonomy uses MBA regions (check `anatomy_ontology` in `taxonomy_meta.yaml`):

```
# Download MBA ontology if not already present
just fetch-mba-ontology        # skip if conf/mba/mbao-full.json already exists

# Build closure tables
just build-anat-closure {taxonomy_id}
```

This parses `conf/mba/mbao-full.json` and adds three tables to the SQLite DB:
- `anat_terms` — MBA region labels + UBERON cross-references
- `anat_hierarchy` — direct parent→child edges (spatial `part_of` + ontological `is_a`)
- `anat_closure` — transitive ancestor→descendant table enabling queries like
  "all supertypes with cells anywhere under hippocampal region (MBA:1080)"

For non-MBA anatomy ontologies, skip `build-anat-closure` and note the limitation
in a comment in `taxonomy_meta.yaml`.

After completion, confirm the DB is queryable:

```
just test-fast   # verifies taxonomy_db unit tests pass
```

Then say:
> "Taxonomy reference DB built at `kb/taxonomy/{taxonomy_id}/` with anatomical
> region closure. Stubs are in `{output_dir}/`. You can now run
> `workflows/lit-review.md` or `workflows/map-cell-type.md` — the DB will be
> queried automatically for candidate atlas matches using region hierarchy."

**Notes:**
- The YAML reference files are the canonical ground truth. The SQLite DB is derived
  and can be rebuilt at any time with `just build-taxonomy-db {taxonomy_id}` — no
  source JSON required after the YAML is generated.
- `conf/mba/mbao-full.json` is gitignored (large download). It is shared across all
  taxonomies — download once, reuse for any subsequent `just build-anat-closure` runs.
- The MBA ontology URL always resolves to the latest release. Re-run
  `just fetch-mba-ontology` to update.

---

## Rules

- **Two gates, no exceptions.** Nothing is written to `kb/` before the mapping
  gate. Nothing is written beyond stubs without human stub review.
- **No schema changes.** SCHEMA_CANDIDATE fields are preserved as YAML comments
  and flagged — they are not added to the YAML structure. Schema changes happen
  separately in `schema/celltype_mapping.yaml`.
- **No information loss.** POTENTIAL_ENRICHMENT fields are preserved as YAML
  comments. TECHNICAL fields are the only ones silently dropped.
- **Stubs are stubs.** `evidence: []`, empty CL terms, and empty
  `anatomical_location` are expected. The stub is the starting point, not the
  end state.
- **Subagent prompts are contracts.** Do not paraphrase — pass verbatim with
  variables filled in.

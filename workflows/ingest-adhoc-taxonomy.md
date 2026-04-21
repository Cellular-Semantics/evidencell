# Ad Hoc Taxonomy Ingest Orchestrator

Build a taxonomy reference DB from a one-off source file (CSV, XLSX, or non-VFB JSON).
Unlike the standard `ingest-taxonomy.md` flow (which uses `ingest_to_yaml()` for KG
exports), this orchestrator has the agent write the per-level YAML directly using the
confirmed field mapping.

Can be invoked:
- **Standalone**: directly by the user to build a reference DB without stub generation.
- **From `ingest-taxonomy.md` Step 4 (Route C)**: after stubs have been generated,
  passing the pre-confirmed `field_mapping.json` to skip Steps 1–2.

---

## Run parameters

```
PARAMS:
  taxonomy_id:      ""     # required — e.g. CCN20250101
  source_file:      ""     # path to CSV/XLSX/JSON source
  field_mapping:    ""     # optional — path to pre-confirmed field_mapping.json
                           # if absent, Steps 1–2 run inline to create one
  model: "sonnet"
```

---

## Step 1 — Inspect and propose field mapping

**Skip this step if `field_mapping` parameter points to an already-confirmed file.**

Spawn a subagent with this prompt (fill in variables):

```
You are a taxonomy field mapping agent for an ad hoc source file.
Your job: inspect the source and propose a field_mapping.json scoped to the
taxonomy reference DB schema (not stub generation).

SOURCE FILE: {source_file}
TAXONOMY ID: {taxonomy_id}

TARGET SCHEMA FIELDS (all optional except node_id, label, taxonomy_level):
  node_id                 — stable unique identifier per node
  label                   — human-readable name
  taxonomy_level          — class / subclass / supertype / cluster / etc.
  parent_id               — parent node_id (null for root nodes)
  cl_id                   — CL CURIE e.g. CL:0000123 (null if absent)
  cl_label                — CL term label
  nt_type                 — neurotransmitter type string (GABA, Glut, etc.)
  defining_markers_scoped — comma-separated gene symbols, scoped to parent group
  defining_markers        — comma-separated gene symbols, global
  tf_markers              — transcription factor markers
  merfish_markers         — MERFISH spatial panel markers
  np_markers              — neuropeptide markers (raw string "Gene:score,...")
  neighborhood            — broad grouping label
  anat[]                  — anatomy associations (id, label, cell_count, cell_ratio)

TASK:

1. Read the source file:
   - CSV/TSV: uv run python3 -c "import csv; ..."
   - Excel: uv run --with openpyxl python3 ...
   - JSON: read with stdlib json

   Report: file format, row count, column names (or top-level keys), 3 sample rows.

2. Identify:
   - Which column(s) give the taxonomy level (or is this a single-level file?)
   - Which column is the unique node_id
   - Which column is the human-readable label
   - Which column is the parent identifier (or how to infer hierarchy)
   - Which columns map to each target schema field above

   For anatomy: note if location info is present. Common formats:
   - Single column with region name/ID: map anat[0].id and anat[0].label
   - Proportional format "STR:0.9,Adj:0.1": document format in notes; will need
     parsing logic in Step 2

   For taxonomy_level_extraction:
   - If the file has one level per row with an explicit level column: use that column
   - If all rows are the same level: use "constant: {level_name}"
   - If the file is denormalised (multiple levels in one row): describe the structure

3. Write field_mapping.json to kb/taxonomy/{taxonomy_id}/field_mapping.json:
{
  "taxonomy_id": "{taxonomy_id}",
  "source_format": "CSV" | "XLSX" | "JSON",
  "confirmed": false,
  "taxonomy_level_extraction": {
    "type": "column" | "constant",
    "column": "<column name if type=column>",
    "value": "<level name if type=constant>"
  },
  "field_mappings": {
    "common_to_all_levels": [
      {"source": "<column name>", "target": "node_id", "confidence": "HIGH"},
      {"source": "<column name>", "target": "label", "confidence": "HIGH"},
      ...
    ],
    "<level_name>": [
      ...
    ]
  },
  "anat_format": "<describe format: 'single_column_id', 'single_column_name',
                   'proportional_string', 'multi_column', 'absent'>",
  "notes": "<any encoding issues, special handling needed, ambiguous columns>"
}

RETURN:
"Format: X. {N} rows. Proposed mapping written to kb/taxonomy/{taxonomy_id}/field_mapping.json.
Unmapped columns: [list]. Requires anatomy parsing: yes/no."

DO NOT write per-level YAML files yet.
```

---

## Step 2 — [GATE] Human reviews field mapping

1. Read `kb/taxonomy/{taxonomy_id}/field_mapping.json` and present the proposed mapping.
2. Flag any `"confidence": "LOW"` entries or unresolved anatomy format for human decision.
3. Ask:
   > "Please review the proposed field mapping. Correct any incorrect source columns,
   > and confirm how anatomy should be handled (if present). Reply 'confirmed' to proceed."
4. When confirmed, set `"confirmed": true` in the JSON file.

---

## Step 3 — Write per-level YAML directly

Spawn a subagent with this prompt (fill in variables):

```
You are a taxonomy YAML writer for an ad hoc source.
Write per-level YAML files in the standard evidencell taxonomy reference format
using a confirmed field mapping.

SOURCE FILE: {source_file}
TAXONOMY ID: {taxonomy_id}
FIELD MAPPING: kb/taxonomy/{taxonomy_id}/field_mapping.json
OUTPUT DIR: kb/taxonomy/{taxonomy_id}/

TASK:

1. Read the confirmed field_mapping.json. Read the source file using:
   - pandas for CSV/XLSX: uv run --with pandas --with openpyxl python3 ...
   - stdlib json for JSON

2. Group rows by taxonomy_level (per "taxonomy_level_extraction" in the mapping).
   For "constant" level: all rows are one level.

3. For each level group, generate a list of node dicts in this structure:
   {
     "node_id": <value>,
     "short_form": <value>,      # same as node_id if no separate short_form column
     "label": <value>,
     "taxonomy_level": <level>,
     "parent_id": <value or null>,
     "cl_id": <value or null>,
     "cl_label": <value or null>,
     "nt_type": <value or null>,
     "defining_markers_scoped": [<gene>, ...] or null,
     "defining_markers": [<gene>, ...] or null,
     "tf_markers": [...] or null,
     "merfish_markers": [...] or null,
     "np_markers": <string or null>,
     "neighborhood": <string or null>,
     "anat": [{"id": <id>, "label": <name>, "cell_count": <int or null>}] or null
   }
   Drop all-null fields for compactness (same as standard ingest output).
   For marker fields: split comma-separated strings into lists.
   For anat: parse per "anat_format" in the mapping.

4. Write one YAML file per level: kb/taxonomy/{taxonomy_id}/{level}.yaml
   Use yaml.dump with allow_unicode=True, sort_keys=False.

5. Write taxonomy_meta.yaml to kb/taxonomy/{taxonomy_id}/taxonomy_meta.yaml:
   - Read inputs/taxonomies/{taxonomy_id}_meta.yaml if present (name, species, tissue, etc.)
   - Add: taxonomy_id, source_file (basename), ingest_date (today), level_counts (per level)

RETURN:
"YAML written: {list of files}. Level counts: {dict}. Nodes with anat: N.
Nodes with CL: N. Nodes with markers: N."

DO NOT run just build-taxonomy-db. DO NOT modify field_mapping.json.
```

---

## Step 3 — [GATE] Human spot-checks YAML

After the subagent returns, prompt:

> "YAML written to `kb/taxonomy/{taxonomy_id}/`. Please spot-check:
> - A few node entries (label/node_id/nt_type look correct?)
> - Anat entries present where expected?
> - Marker lists sensible?
> Reply 'proceed' to build the DB, or describe any issues."

Wait for human confirmation before building the DB.

---

## Step 4 — Build and verify DB

After human confirms, run:

```
just build-taxonomy-db {taxonomy_id}
```

If `anatomy_ontology` in `taxonomy_meta.yaml` is "MBA" and `conf/mba/mbao-full.json` exists:
```
just build-anat-closure {taxonomy_id}
```

Verify using the discovery queries in `.claude/skills/query-taxonomy-db.md` Step 1:
- Level counts match expected
- Field coverage (has_nt_type, has_markers, etc.) as expected
- Anat closure built (if MBA)

Report field coverage summary to the human.

---

## Rules

- **Field mapping must be confirmed** (Step 2 gate) before any YAML is written.
- **Marker lists are split on commas**: "Sst,Pvalb" → ["Sst", "Pvalb"].
- **No taxonomy_id field in per-node YAML**: the standard output does not store
  taxonomy_id per node (it's implicit from the file's location).
- **The field_mapping.json is the re-ingest recipe**: preserve it exactly as confirmed.
  On future source file updates, re-run from Step 3 with the same mapping.
- **Stubs vs DB YAML are different**: this orchestrator writes the reference DB YAML
  (`kb/taxonomy/`), not CellTypeNode stubs (`kb/draft/` or `kb/mappings/`). These serve
  different purposes and are written to different locations.

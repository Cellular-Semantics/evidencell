# Skill: Query Taxonomy Reference DB

## When to use

Use this skill when you need to find candidate atlas nodes for a classical cell type
mapping, explore what a taxonomy contains, or check what metadata fields are populated
before running targeted queries.

Taxonomies vary significantly in metadata richness. **Always run discovery first** —
it tells you which fields are populated and which queries are worth running.

---

## Input

The user provides:
- `taxonomy_id` — e.g. `CCN20230722` (required)
- Optionally one or more of:
  - `region` — MBA CURIE (`MBA:1080`), UBERON term (`UBERON:0001954`), or plain name
  - `nt_type` — neurotransmitter prefix (`GABA`, `Glut`, `Gly`, `GABA-Glyc`, etc.)
  - `markers` — gene symbol list (`Sst`, `Pvalb`, `Reln`, …)
  - `level` — taxonomy level to return (`supertype` default, `cluster`, `subclass`)

---

## Steps

### Step 1: Discovery — what does this taxonomy contain?

```python
import sqlite3, json
from evidencell.paths import taxonomy_db_path
from pathlib import Path

db_path = taxonomy_db_path("{taxonomy_id}")
if not db_path.exists():
    raise FileNotFoundError(f"DB not found: {db_path}. Run: just build-taxonomy-db {taxonomy_id}")

con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row

# Level counts
levels = con.execute(
    "SELECT taxonomy_level, COUNT(*) AS n FROM nodes GROUP BY taxonomy_level ORDER BY n DESC"
).fetchall()
print("Levels:", {r["taxonomy_level"]: r["n"] for r in levels})

# Optional field coverage (which metadata fields are actually populated?)
cov = con.execute("""
    SELECT
        COUNT(*) AS total,
        SUM(cl_id IS NOT NULL)                    AS cl_mapped,
        SUM(nt_type IS NOT NULL)                  AS has_nt_type,
        SUM(defining_markers_scoped IS NOT NULL)  AS has_scoped_markers,
        SUM(defining_markers IS NOT NULL)         AS has_markers,
        SUM(tf_markers IS NOT NULL)               AS has_tf_markers,
        SUM(merfish_markers IS NOT NULL)          AS has_merfish,
        SUM(np_markers IS NOT NULL)               AS has_np_markers,
        SUM(neighborhood IS NOT NULL)             AS has_neighborhood,
        SUM(circadian_ratio IS NOT NULL)          AS has_circadian,
        SUM(sex_bias IS NOT NULL)                 AS has_sex_bias,
        SUM(rationale IS NOT NULL)                AS has_rationale
    FROM nodes
""").fetchone()
print("Field coverage (all levels):", dict(cov))

# NT type distribution (clusters only — NT type is propagated from here)
nt_dist = con.execute("""
    SELECT nt_type, COUNT(*) AS n FROM nodes
    WHERE taxonomy_level = 'cluster' AND nt_type IS NOT NULL
    GROUP BY nt_type ORDER BY n DESC
""").fetchall()
print("NT types at cluster level:", [(r["nt_type"], r["n"]) for r in nt_dist])

# Has MBA closure tables?
has_closure = con.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='anat_closure'"
).fetchone() is not None
print("Anat closure built:", has_closure)
if has_closure:
    n_terms = con.execute("SELECT COUNT(*) FROM anat_terms").fetchone()[0]
    n_uberon = con.execute("SELECT COUNT(*) FROM anat_terms WHERE uberon_id IS NOT NULL").fetchone()[0]
    print(f"  anat_terms: {n_terms}  ({n_uberon} with UBERON xref)")
```

**Interpret before proceeding.** Fields with zero coverage are unavailable for this
taxonomy — skip corresponding query steps. Adjust query strategy accordingly.

---

### Step 2: Resolve region (if provided)

If the user gave a region, resolve it to MBA CURIE(s) for use in candidate queries.

**If given an MBA CURIE** (e.g. `MBA:1080`): use directly as `anat_root_ids`.

**If given a UBERON term** (e.g. `UBERON:0001954`): look up via `anat_terms`:
```python
rows = con.execute(
    "SELECT anat_id, label FROM anat_terms WHERE uberon_id = ?", (uberon_id,)
).fetchall()
# Use the matching anat_id as the root
```

**If given a plain name** (e.g. "hippocampus"): fuzzy search `anat_terms.label`:
```python
rows = con.execute(
    "SELECT anat_id, label FROM anat_terms WHERE label LIKE ?", (f"%{name}%",)
).fetchall()
# Show matches and ask the user to confirm which to use if ambiguous
```

If closure tables are absent and a region root is requested, fall back to exact
`anat_id` matching only — note the limitation to the user.

---

### Step 3: Candidate query

```python
import sys
sys.path.insert(0, "src")
from evidencell.taxonomy_db import TaxonomyDB

db = TaxonomyDB(db_path)

hits = db.find_candidates(
    anat_root_ids=["{mba_root}"],   # from Step 2; omit if no region given
    anat_ids=[...],                  # exact leaf IDs if no closure
    nt_type="{nt_type}",            # omit if not specified; prefix-matched at cluster level
    markers=["{m1}", "{m2}"],       # omit if not specified
    level="{level}",                # default: supertype
)
```

**Important**: `nt_type` is only populated at **cluster** level in this taxonomy.
For supertype queries, NT type filtering works by scoring (clusters are scored, supertypes
inherit if most of their clusters match). If this taxonomy has `nt_type` at supertype
level, direct filtering works; check coverage from Step 1 first.

---

### Step 4: Present results

For each hit, show the fields that are actually populated (use coverage from Step 1
to decide which columns to include). Always show:
- `node_id`, `label`, `taxonomy_level`, `_score`
- `cl_id` / `cl_label` if CL-mapped

Show conditionally (only if the field has coverage):
- `nt_type` — if `has_nt_type > 0`
- scoped markers — if `has_scoped_markers > 0` (highest mapping value — markers
  distinctive within parent group)
- global markers — if `has_markers > 0`
- `tf_markers` — if `has_tf_markers > 0` (transcription factor markers)
- `merfish_markers` — if `has_merfish > 0` (spatial panel markers)
- `np_markers` — if `has_np_markers > 0` (neuropeptide markers, format "Gene:score")
- `neighborhood` — if `has_neighborhood > 0`
- `circadian_ratio` — if `has_circadian > 0` (Light fraction; only stored when skewed
  >0.7 or <0.3; may aid identification for small number of types)
- `sex_bias` — if `has_sex_bias > 0`

For each hit also show the top anatomical regions (by cell count) that overlap with
the query region:
```python
for hit in hits[:20]:
    regions = con.execute("""
        SELECT a.anat_id, t.label, a.cell_count
        FROM anat a LEFT JOIN anat_terms t ON t.anat_id = a.anat_id
        WHERE a.node_id = ?
        ORDER BY a.cell_count DESC LIMIT 3
    """, (hit["node_id"],)).fetchall()
```

---

### Step 5: NT-type propagation query (if nt_type requested and coverage is at cluster only)

When `nt_type` is specified and NT type is only available at cluster level, run an
explicit graph propagation to find supertypes by cluster composition:

```python
rows = con.execute(f"""
    SELECT
        sup.node_id, sup.label, sup.cl_id, sup.cl_label,
        sup.defining_markers_scoped,
        COUNT(cl.node_id) AS matching_clusters,
        COUNT(cl.node_id) * 1.0 /
            (SELECT COUNT(*) FROM nodes c2
             WHERE c2.parent_id = sup.node_id AND c2.taxonomy_level = 'cluster')
            AS nt_fraction
    FROM nodes sup
    JOIN nodes cl ON cl.parent_id = sup.node_id
    WHERE cl.taxonomy_level = 'cluster'
      AND cl.nt_type LIKE ?
      AND sup.taxonomy_level = ?
      {region_join_clause}
    GROUP BY sup.node_id
    HAVING nt_fraction >= 0.5
    ORDER BY nt_fraction DESC, matching_clusters DESC
""", (f"{nt_type}%", level, ...)).fetchall()
```

Report the fraction alongside results so the user knows whether a supertype is
predominantly or incidentally of the requested NT type.

---

## Important notes

- **Scoped markers** (`defining_markers_scoped`) are distinctive within the parent
  subclass, not globally — they are the highest-value markers for mapping.
  Prefer these over global `defining_markers` when both are present.
- **NT type is cluster-level only** in WMB/CCN20230722. Use Step 5 for clean NT
  filtering at supertype level.
- **UBERON ↔ MBA translation** requires closure tables. If absent, the user needs
  to run `just fetch-mba-ontology && just build-anat-closure {taxonomy_id}`.
- **Field coverage varies** between taxonomies. A taxonomy without `merfish_markers`
  or `np_markers` is not incomplete — those fields simply weren't part of its annotation.
  Do not report absences as errors.
- **Score interpretation**: region match = 2 pts, NT match = 2 pts (cluster level),
  each marker match = 1 pt. A score of 2 means region match only. Score of 4 means
  region + NT. Higher scores indicate more overlapping evidence.

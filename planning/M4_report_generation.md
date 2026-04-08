# M4 Report Generation — Implementation Plan

*Links from: [ROADMAP.md § M4](ROADMAP.md#m4--report-generation-mvp-for-biologists)*
*Working examples: `kb/draft/hippocampus/reports/` (OLM case study)*

---

## Report granularity

**One report per classical (literature) cell type**, not per graph file.

A graph file is a storage unit — one region, multiple classical types and their
atlas candidates in one YAML. But the *review unit* is a single classical type
and all its candidate edges: a biologist reviewing OLM mappings does not need
basket cell mappings on the same page.

`just gen-report {graph_file}` iterates over every non-terminal node in the graph
and produces one report per classical type. `just gen-report {graph_file} {node_id}`
produces a report for one specific classical type.

---

## Overview

Two-tier output per classical type: a **summary report** for orientation and
decision-making, and per-paper **drill-down pages** for evidence review. Both are
generated from KB YAML + `references.json`; neither requires reading the schema
or raw YAML.

The prototype (`examples/reports/generate_report.py`) handles single-tier full +
condensed output for the CB/BG examples. The production `render.py` extends this
with the per-classical-type summary format, drill-downs, numbered references, and
the new evidence types added at M3 (`AtlasQueryEvidence`).

---

## Tier 0 — Region index

**File:** `kb/{draft|mappings}/{region}/reports/index.md`
**Triggered by:** `just gen-index {region}`

One row per classical type across all graph files in the region. The entry point
for a biologist exploring the region — shows what's been mapped and at what
confidence, so they can choose which classical type to investigate further.

### Columns

| Classical type | CL term | Best atlas hit | Best confidence | Candidates | Link |
|---|---|---|---|---|---|
| OLM interneuron | — | 0769 Sst Gaba\_3 | 🟡 MODERATE | 5 (1 MODERATE, 1 LOW, 3 UNCERTAIN) | [report](olm_hippocampus_summary.md) |

- **Classical type** — `node.name`
- **CL term** — `node.cl_mapping.cl_term.id` if present, else `—`
- **Best atlas hit** — atlas node name from the highest-confidence edge
- **Best confidence** — badge for highest-confidence edge in this classical type
- **Candidates** — total edge count, broken down by confidence tier in parentheses
- **Link** — relative link to the per-classical-type summary report

### Sorting

Primary: best confidence (HIGH → MODERATE → LOW → UNCERTAIN).
Secondary: classical type name alphabetically.

### Header

```markdown
# {Region} Cell Type Mapping Index
*{N} classical types · {date} · {draft|canonical}*

Atlas: {target_atlas from first graph, or list if multiple}
```

---

## Tier 1 — Summary report

**File:** `{output_dir}/{graph_stem}_summary.md`
**Triggered by:** `just gen-report {graph_file}`

### Sections (in order)

#### 1. Header

```
# {graph_name} — {target_atlas} Mapping Report
*{status} · {date} · Source: {graph_file}*
```

If status is `draft`, add a warning banner:
> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

#### 2. Location note (conditional)

Emit when any atlas node has MERFISH-derived location data:

> **Location note.** WMBv1 location data derives from MERFISH spatial
> registration and records **soma position** only. Axonal and dendritic
> projection targets are not reflected in atlas cluster location fields and
> are not used in mapping assessments.

#### 3. Classical type table

One row per non-terminal node in the graph. Columns:
- Name + CL term (if mapped)
- NT type
- Key markers (defining, up to 5; then "…")
- Neuropeptides
- Soma location (UBERON label + Allen name_in_source)

#### 4. Mapping candidates table

One row per edge. Columns:
- Rank (by confidence tier, then composite discovery score if available)
- WMBv1 cluster name + accession
- Supertype
- n_cells
- Confidence badge (🟢 HIGH / 🟡 MODERATE / 🔴 LOW / ⚪ UNCERTAIN)
- Key property alignment summary (e.g. "Chrna2 APPROXIMATE · Npy CONSISTENT")
- Verdict (free text from edge notes, or derived: Best candidate / Speculative / Eliminated)

Edges grouped by confidence tier. UNCERTAIN edges collapsed into a single
"Eliminated" block with shared rationale if they share a common disqualifying signal.

#### 5. Candidate paragraphs

One section per MODERATE or LOW edge. UNCERTAIN edges share a combined section
titled "Eliminated candidates".

Each section:
- **Supporting evidence** — bulleted, inline `[n]` citations
- **Concerns** — bulleted, inline `[n]` citations; location caveats flagged as
  adjacent (weak) vs distant (stronger) per the soma-only location rule
- **What would upgrade confidence** — derived from `unresolved_questions[]` and
  `proposed_experiments[]` on the edge; explicit about what evidence type is needed
  and what threshold

#### 6. Proposed experiments

Consolidated across edges — group by experiment type, not by edge. Cross-edge
experiments (e.g. Chrna2-Cre + MapMyCells applies to multiple edges) appear once.

For each experiment:
- What (method)
- Target (quantitative threshold, e.g. F1 ≥ 0.80 at CLUSTER level)
- Expected output (evidence type that would be added to KB)
- Resolves (which edges / which open questions)
- Where annotation transfer: include atlas, tool, expected output format, and
  how results feed back as `AnnotationTransferEvidence`

#### 7. Open questions

Numbered list, pulled from `unresolved_questions[]` across all edges, deduplicated.

#### 8. Evidence base table

Compact table: edge | evidence types | supports. No quotes.
One-liner per evidence item. Makes clear how much is atlas-metadata vs literature.

#### 9. References

Numbered `[1]`–`[N]` reference table. Columns:
- `[n]` index
- Author et al. Year
- Journal
- PMID (linked)
- Used for (one-line, e.g. "Chrna2 as OLM marker")

`[A]`, `[B]`… for non-literature sources (atlas browser queries, database accessions).
`AtlasQueryEvidence` items use `[A]`-style labels with `query_url` as the link.

Reference numbers are assigned in order of first appearance in the document.

---

## Tier 2 — Evidence drill-down

**File:** `{output_dir}/{graph_stem}_drilldown_{author}{year}.md`
One file per cited paper (generated on demand or all at once).
**Triggered by:** `just gen-drilldown {graph_file} {pmid}` or `just gen-report` with `--drilldowns`

### Sections

#### 1. Header

```
# Evidence Drill-down: {Author} et al. {Year}
*Supporting: {edge_id} ({classical_name} → {atlas_name})*
*[← Back to summary report]({summary_file})*
```

#### 2. Citation + Why this paper matters

Full citation. One paragraph explaining: what the paper measured, why it's relevant
to this specific mapping (bridging classical anatomy to transcriptomics, establishing
a marker, providing annotation transfer data, etc.).

#### 3. Per-property evidence sections

One `###` section per relevant claim. For each:
- Property name
- Alignment with specific atlas cluster (CONSISTENT / APPROXIMATE / etc.)
- Verbatim quote, indented as blockquote, with section label
- Interpretation paragraph: how the finding connects to the atlas node

Ordering: markers first, then neuropeptides, then NT, then location, then lineage/other.

#### 4. Summary scorecard table

| OLM property | Paper finding | Atlas cluster alignment | Quote key |
|---|---|---|---|

Quote keys link back to `references.json` entries for traceability.

#### 5. Critical gap

One paragraph: what the paper establishes vs what still needs to be done to confirm
the mapping. Should name the bridging experiment explicitly (e.g. "GEO:GSE124847 is
available for direct MapMyCells re-mapping").

#### 6. Footer

```
*Drill-down generated from: references.json (corpus_id: {id})*
*Quotes: source_method={method}, status={status}*
```

---

## render.py implementation

### Port from prototype

The following functions in `generate_report.py` port directly into `render.py`
with minor updates:

| Prototype function | Action |
|---|---|
| `_conf_badge()` | Port as-is |
| `_rel_badge()` | Port as-is |
| `_ot()` | Port as-is |
| `fmt_literature()` | Update: use `snippet` field; add numbered ref lookup |
| `fmt_atlas_metadata()` | Update: use `defining_markers` (renamed from `positive_markers` in v0.5.3); drop deprecated `nt_consistent_with_classical` |
| `fmt_annotation_transfer()` | Port as-is; add `source_species`/`target_species` fields added in v0.5 |
| Mermaid generation | Port as-is for condensed/full; not needed for summary |

### New functions required

```python
# render.py additions

def build_reference_index(graph: dict, refs: dict) -> dict[str, RefEntry]:
    """
    Scan all evidence items across all edges.
    Assign [1]..[N] to PMIDs/DOIs in order of first appearance.
    Assign [A]..[Z] to non-literature sources (AtlasQueryEvidence query_urls,
    database accessions).
    Return lookup: pmid_or_url → RefEntry(index, label, citation_line, used_for)
    """

def fmt_atlas_query(ev: dict, ref_index: dict) -> str:
    """
    Format an AtlasQueryEvidence item.
    Fields: atlas, query_url, filters_applied, atlas_version, explanation, supports.
    Label: [A]-style from ref_index.
    """

def render_summary(graph: dict, refs: dict, out_path: Path) -> None:
    """Top-level: builds and writes the summary report."""

def render_drilldown(graph: dict, refs: dict, pmid: str, out_path: Path) -> None:
    """Top-level: builds and writes one drill-down from references.json quotes."""

def _location_note(graph: dict) -> str | None:
    """
    Return soma-only location note if any atlas node has MERFISH location data.
    Condition: any node with is_terminal=True and non-empty anatomical_location.
    """

def _candidate_verdict(edge: dict, nodes: dict) -> str:
    """
    Derive verdict string from confidence + Chrna2/key-marker alignment.
    MODERATE+ → 'Best candidate' or 'Strong candidate'
    LOW → 'Speculative'
    UNCERTAIN with DISCORDANT marker → 'Eliminated ({reason})'
    UNCERTAIN otherwise → 'Uncertain'
    """

def _group_experiments(edges: list) -> list[ExperimentGroup]:
    """
    Collect proposed_experiments[] across all edges.
    Deduplicate by method type (fuzzy match on method keywords).
    Return groups with list of edges each experiment resolves.
    """

def render_index(region: str, kb_root: Path, out_path: Path) -> None:
    """
    Scan all graph YAMLs in kb/{draft|mappings}/{region}/.
    For each non-terminal node, extract: name, cl_mapping, best edge
    (highest confidence), edge count by tier.
    Write sorted index table with relative links to summary reports.
    """

def _best_edge(edges: list, node_id: str) -> dict | None:
    """
    From edges where type_a == node_id, return the edge with the highest
    confidence (HIGH > MODERATE > LOW > UNCERTAIN).
    """
```

### Location caveat rendering

When rendering a location property comparison:
- If alignment is APPROXIMATE: append `*(adjacent region — possible registration error)*`
- If alignment is DISCORDANT with a location property: append
  `*(distant region — stronger counter-evidence; classical type may still be a subtype)*`

This is derived from the `notes` field on the PropertyComparison, not hardcoded —
the mapping agent already writes these notes per the updated `map-cell-type.md`.

---

## Justfile recipes

```makefile
# Generate summary report(s) for one graph file — one report per classical type
gen-report GRAPH_FILE:
    uv run python -m evidencell.render summary {{GRAPH_FILE}}

# Generate one classical-type report by node id
gen-report-node GRAPH_FILE NODE_ID:
    uv run python -m evidencell.render summary {{GRAPH_FILE}} --node {{NODE_ID}}

# Generate all drill-downs for a classical type
gen-drilldowns GRAPH_FILE NODE_ID:
    uv run python -m evidencell.render drilldowns {{GRAPH_FILE}} --node {{NODE_ID}}

# Generate region index (one-row-per-classical-type overview)
gen-index REGION:
    uv run python -m evidencell.render index {{REGION}}

# Regenerate all reports + indices for canonical KB
gen-report-all:
    for f in $(find kb/mappings -name "*.yaml"); do \
        uv run python -m evidencell.render summary $f; \
    done
    for region in $(ls kb/mappings); do \
        uv run python -m evidencell.render index $region; \
    done
```

CLI entry point via `src/evidencell/render.py`:
```
python -m evidencell.render summary <graph_file> [--node NODE_ID] [--output-dir DIR] [--drilldowns]
python -m evidencell.render drilldowns <graph_file> --node NODE_ID [--pmid PMID] [--output-dir DIR]
python -m evidencell.render index <region> [--output-dir DIR]
```

---

## Output file conventions

Reports are scoped to one classical type. The classical node `id` is the stable
identifier used in filenames.

| Output | Path |
|---|---|
| Summary report | `{graph_dir}/reports/{node_id}_summary.md` |
| Drill-down | `{graph_dir}/reports/{node_id}_drilldown_{AuthorYYYY}.md` |

Example for OLM:
```
kb/draft/hippocampus/reports/
  olm_hippocampus_summary.md
  olm_hippocampus_drilldown_Winterer2019.md
  olm_hippocampus_drilldown_Leao2012.md
```

Draft reports go in `kb/draft/{region}/reports/`.
Canonical reports go in `kb/mappings/{region}/reports/`.
Reports are not committed to git by default (add to `.gitignore`); regenerate
from KB YAML. Exception: pin a report at release time as a dated snapshot.

`{graph_dir}/reports/index.md` — auto-generated index listing all classical types
in the graph with links to their summary reports and date last generated.

---

## Evidence type coverage

| Evidence type | Summary report | Drill-down | Notes |
|---|---|---|---|
| `LITERATURE` | Reference [n] + explanation | Full quote + section + interpretation | Core drill-down type |
| `ATLAS_METADATA` | "Atlas metadata" label | Not drill-down-able (no quotes) | Evidence base table only |
| `ATLAS_QUERY` | Reference [A] + filters + explanation | Query URL + filters + observation | New in v0.5.4 |
| `ANNOTATION_TRANSFER` | F1 score + level | Metrics table per level | Port from prototype |
| `PATCH_SEQ` | Label + explanation | Not yet (no quote structure) | Extend if needed at M5 |

---

## What the OLM case study demonstrated

These design decisions emerged from the OLM hippocampus mock-up and must be reflected
in `render.py`:

1. **Soma-only location note** — always emit when atlas has MERFISH data; do not
   compare axon/dendrite projection targets to atlas location fields.

2. **Adjacent vs distant off-target location** — use `notes` field on location
   PropertyComparison to distinguish. Adjacent → weak caveat; distant → stronger
   caveat with subtype caveat preserved.

3. **UNCERTAIN edges collapsed** — when multiple UNCERTAIN edges share a common
   disqualifying signal (e.g. all Sst Gaba\_6 clusters eliminated by Chrna2
   absence), group them into one "Eliminated" section with shared rationale
   rather than repeating per edge.

4. **Npy species caveat** — when Npy (or any marker) has a known rat/mouse
   discrepancy documented in the literature, the drill-down must surface it
   explicitly (Winterer et al. 2019 reversed the prior Npy exclusion rule).

5. **GEO/dataset accessions as actionable links** — when a drill-down source
   paper has a public dataset (GEO, SCP, NeMO), include it in the critical gap
   section as a direct bridging experiment path.

6. **`[A]`-style atlas query references** — `AtlasQueryEvidence` items use
   `query_url` as the citable reference; label as `[A]`, `[B]` etc. distinct
   from numbered literature references.

---

## Deferred (not M4)

- HTML rendering (Jinja2 → HTML) — deferred pending community need
- Report versioning via git log — implement when reports are committed to repo
- Automated experiment structuring (atlas + tool + expected output from free text) —
  requires schema extension to `proposed_experiments[]`; deferred to M5
- Per-node drill-downs (classical type characterisation page) — deferred; focus
  is edges for M4

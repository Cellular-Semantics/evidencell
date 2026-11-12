# HMBA Basal Ganglia Consensus Taxonomy — ingest plan

**Status:** **Implemented on branch `bg-ingest-180`** (closes
[#180](https://github.com/Cellular-Semantics/evidencell/issues/180), 2026-11-12).
WS1 (parameterised anatomy loader, DHBA), gap 2 (label-derived `nt_type` with
qualified provenance) and WS3 (BG accession codes) are in `taxonomy_db.py`;
`inputs/taxonomies/CCN20250428.cypher`, `CCN20250428_meta.yaml` and
`kb/taxonomy/CCN20250428/field_mapping.json` are authored, and the ingest has
been run end-to-end against the live KG: 61/36/12/4 nodes, 86 DHBA locations,
NT on 75/113 nodes each with one qualifying source, DHBA closure 3,317 terms.
`field_mapping.json` is still `confirmed: false` pending the ingest gate.

The brain_cell_KG changes this plan waited on landed 2026-10-27 (BG Group soma
locations transferred onto `BG:` taxonomy nodes; DHBA/CLM CURIE prefixes fixed).
**The two-hop `exemplar_data_of` anatomy path, the `ns3:` prefix workaround and
the Group-level gate described below are obsolete** — anatomy is now on the node
via `obsolete_some_soma_located_in` / `obsolete_cell_ratio`, exactly as WMBv1;
the Cypher file is a near-copy of `CCN20230722.cypher`. Still absent in the KG:
`nt_type` (no property on any BG node) and a computed marker panel (WS5).

**NT decision (curator, 2026-11-12):** bring NT in for all BG nodes, derived
from the cluster **label** (not the CL target's neo4j labels, which lose
dopamine and add a spurious `hist`), with a qualified `nt_type.sources` entry
carrying method, scope, `support: WEAK` and a caveat; cholinergic groups are a
Chol / Chol+GABA mix and need the caveat most. Citation used as `ref`: the
taxonomy preprint, Johansen, Fu et al. 2025, bioRxiv 10.64898/2025.12.15.694496.

Remaining: WS5 (precomputed stats → expression), WS6 (KB rewiring; `CL:0020004`
vs `CL:4310096` on GPi Shell), marker case-sensitivity before mapping.

**Date:** 2026-10-22
**Taxonomy:** `CCN20250428` (HMBA Basal Ganglia Consensus; accessions `CS20250428_*`)
**KG:** live and queryable on `bolt://localhost:7687` — see probe sections below
(initial probe 2026-10-22; anatomy re-probe 2026-10-25)

---

## Decisions taken (curator, 2026-10-22)

| Question | Decision |
|---|---|
| Anatomy ontology | DHBA, loaded the same way as MBA |
| Taxonomy levels | Derived from the graph (labelset edges); curator can supply canonical level names for cross-check |
| Species | Single taxon, `NCBITaxon:9443` Primates — matches the existing BG graph stubs |
| Accessions | Taken from the KG, not re-derived or re-minted |
| MapMyCells / precomputed stats | Local stats HDF5 + summary expression files available, as for WMBv1 |

### Decisions added after the KG probe (curator, 2026-10-22)

| Question | Decision |
|---|---|
| Implementation timing | **Wait for the KG refactoring to land.** Design is settled; do not build against a moving schema. |
| Anatomy | Curator to track down the BG anatomy links. They are gross-level (region, not subregion) but still useful — gross anatomy is enough to separate BG candidates from the rest of the brain, which is most of what anatomy scoring buys. |
| Markers | More may be available upstream. **Proceed without them for now** — rationale markers + the precomputed stats panel are enough to start. |
| NT type | May be derived from the cluster name, but **must carry an explicit qualification** that it was not tested at cluster level. See the NT provenance section below. |

No KB content edits are in scope for this plan — it covers ingest
infrastructure and the ingest run only. KB rewiring is listed in WS6 as a
separate, later task.

---

## Verified finding: DHBA can reuse the MBA loader

> **Confirmed required (2026-10-25).** The anatomy that landed in the KG is
> DHBA — IRIs under `purl.brain-bican.org/ontology/dhbao/`. The structural
> analysis below is therefore the live design, not a contingency.


Checked `dhbao-full.json`
(`brain-bican/developing_human_brain_atlas_ontology`, release v2025-02-10)
against `mbao-full.json` (v2025-07-04):

| | MBA | DHBA |
|---|---|---|
| Atlas CLASS terms with labels | 1,327 | 3,317 |
| Intra-atlas tree edges (`is_a` + `part_of`) | 1,992 | 3,490 |
| Terms with a UBERON `is_a` target (xref) | 610 (46%) | 751 (23%) |
| IRI form | `…/ontology/mbao/MBA_399` | `…/ontology/dhbao/DHBA_10344` |
| `*:ENTITY` pseudo-roots | none | none |

The two files are structurally identical — same ODK/TDT build, same Obograph
shape, same conventions: the spatial tree is predominantly `BFO_0000050`
(part_of) with a minority of `is_a`, and the UBERON link is an `is_a` edge from
the atlas term to a UBERON class. `_parse_mba_obograph()` already consumes
**both** predicates and already derives `uberon_id` from the atlas→UBERON `is_a`
edge, so **no parsing logic changes are needed** — only the literal `"MBA:"`
prefix (three occurrences, `taxonomy_db.py:1395-1420`) has to become a
parameter.

Spot-check: `DHBA:10344` "internal segment of globus pallidus" — the anchor
already used in `kb/graphs/BG/GPi_shell_neuron.yaml` — carries
`is_a UBERON:0002477` (medial globus pallidus) and `part_of DHBA:10342`
(globus pallidus). Both the xref path and the closure path resolve.

Two caveats:

- **UBERON xref coverage is half MBA's rate** (23% vs 46%). `find-candidates`
  resolves classical-node UBERON IDs → atlas IDs via the xref table, falling
  back to `_resolve_mba_by_name()` label matching. Expect the name-fallback
  path to carry more traffic for DHBA; its warnings should be reviewed on the
  first mapping run rather than assumed benign.
- **DHBA is the *developing* human atlas.** It is the anchor the existing BG
  graph uses (with a noted intent to migrate once HOMBA stabilises), and
  `human_brain_atlas_ontology` (hbao) and `primate_brain_atlas_ontology`
  also exist in the same org — hbao released, pbao with no release yet.
  **Confirm against the KG which ontology the BG anatomy edges actually point
  at before loading** (WS2 Step 1); if they are HBA or UBERON-direct, the same
  parameterised loader applies with a different prefix and URL.

---

## KG probe — 2026-10-22 (live instance, `bolt://localhost:7687`, neo4j 4.4.44)

Probed over the HTTP transaction endpoint (no auth required). **BG is present
and queryable.** 51,611 nodes total; BG occupies the `BG:` CURIE prefix.

### Structure

| Level (labelset) | `rank` | Accession pattern | Nodes |
|---|---|---|---|
| Group (terminal) | 0 | `CS20250428_GROUP_nnnn` | 61 |
| Subclass | 1 | `CS20250428_SUBCL_nnnn` | 36 |
| Class | 2 | `CS20250428_CLASS_nnnn` | 12 |
| Neighborhood | 3 | `CS20250428_NEIGH_nnnn` | 4 |

113 taxonomy nodes + 4 labelset meta-nodes (`BG:Group`, `BG:Subclass`,
`BG:Class`, `BG:Neighborhood`) = the 117 `BG:` Individuals. Labelsets carry an
explicit `rank` property; it agrees exactly with what
`_build_level_hierarchy()` derives topologically, so no override is needed —
and the derived hierarchy can be checked against it as a free invariant.

Edges match the post-2026-04 WMBv1 conventions exactly: `has_labelset` (113),
`subcluster_of` (109 — Group→Subclass→Class→Neighborhood), `composed_primarily_of`
→ CL (87). Node IRIs are `purl.brain-bican.org/ontology/CS20250428/…`;
`short_form` carries the authoritative accession.

### The default query pattern is sufficient, with two edits

Taking `CCN20230722.cypher` and substituting `WMB:` → `BG:`, then **deleting
the anatomy `OPTIONAL MATCH`**, the query runs clean and returns:

```
rows=113   with_parent=109   with_cl=87   levels=4
```

The `cl.curie =~ "CL:\d{7}"` filter works unchanged (`CL:0020004` etc.).
The `has_labelset` join correctly excludes the 4 labelset meta-nodes, exactly
as it does for WMBv1's 5. **No new query idiom is required.**

### Gap 1 — no anatomy in the KG for BG — **RESOLVED 2026-10-25**

> Superseded by the anatomy re-probe below: crude DHBA locations are now
> present, reached two hops out via the CL/PCL term. The text below records
> the state as of 2026-10-22.

BG nodes have **no soma-location edges of any kind**. The only UBERON links are
`INSTANCEOF → UBERON:0001062 "anatomical entity"` (50×) — an upper-level type
assertion, not a location. A KG-wide sweep for any edge targeting a `DHBA:`,
`HBA:`, or `PBA:` CURIE returns **zero rows** — those ontologies are not loaded
at all.

**This reverses WS1's priority.** The DHBA closure loader is *not* on the
ingest critical path: with no anatomy on BG nodes, `find-candidates` anatomy
scoring contributes nothing whether or not the closure table exists. Ingest can
and should proceed without it. WS1 only becomes necessary once BG anatomy is
sourced from somewhere — and that is now an open curator question (see below).

### Gap 2 — no `nt_type` property (needs a small decision)

WMBv1 nodes carry `nt_type_label`; BG nodes carry no NT property at all. NT is
recoverable two ways, neither reachable through `field_mapping.json` as it
stands:

- From the CL target's neo4j labels: `composed_primarily_of → (cl:Cell)` where
  `cl` is labelled `GABA` / `Glu` / `Chol` / `Gly` / `hist`. Coverage across
  the 87 CL-linked nodes: GABA 39, none 35 (non-neuronal), neuron-only 6,
  Chol+GABA+hist 3, Glu 3, GABA+Glu 1.
- From the label string itself (`"LAMP5-LHX6 GABA"`, `"CN GABA-Glut"`).

`_extract_node` reads `nt_type` only from the node's own properties
(`_first_prop(props, …)` — `taxonomy_db.py:531`), so a derived Cypher column
cannot be routed to it. Options, cheapest first:

1. **Leave `nt_type` null and rely on `cl_id`.** Costs the NT component of
   candidate scoring (`query_by_nt`, `query_by_nt_propagated`).
2. **Dev-request: let `field_mapping.json` map a target field to a top-level
   row column**, not just a node property. Generally useful — any derived
   Cypher column becomes mappable. Then the query returns
   `[l IN labels(cl) WHERE l IN ['GABA','Glu','Chol','Gly','hist']] AS nt_type`.
3. **Derive `nt_type` from the CL term at ingest** when absent. Narrower, and
   bakes a CL→NT table into ingest.

Recommend (2) — **but a derived `nt_type` must not be written bare**; see the
NT provenance section below.

### Gap 3 — markers are curation rationale, not a computed panel

`marker_gene_evidence` is present on **42 of 61 Groups and on no node above
Group level** (Class 0/12, Subclass 0/36, Neighborhood 0/4). It holds the genes
cited in the curator's `rationale` — e.g. GROUP_0016 → `["Sst","Tbr1","Slc17a6"]` —
not a WMBv1-style `cluster_markers_combo` panel.

Good news: `_split_markers()` already accepts a list, so
`"defining_markers": ["marker_gene_evidence"]` in `field_mapping.json` works
with **zero code change**.

Consequence: **WS5 (precomputed stats → `enrich-marker-union`) is not optional
for BG** — it is the only route to a marker panel with real coverage. Sparse,
Group-only rationale markers will not support candidate scoring on their own.

### Asset — curated BG↔WMBv1 correspondences already in the KG

BG Groups carry SKOS links to WMBv1 nodes: `exactMatch` → supertype (38) and
→ subclass (16), `broadMatch` → subclass (40), `relatedMatch` → supertype (41)
and → subclass (4). **58 of 61 Groups have at least one WMBv1 match.**

Spot-check: `BG:CS20250428_GROUP_0016` "GPi Shell" →
`exactMatch WMB:CS20230722_SUPT_0504` and
`broadMatch WMB:CS20230722_SUBC_112` — precisely the two nodes already
hand-authored into `kb/graphs/BG/GPi_shell_neuron_Mmus.yaml`. That is a strong
independent confirmation of the existing curation, and a ready-made oracle set
for a cross-species methods audit.

These edges are **out of scope for this ingest** (they are cross-taxonomy
mapping assertions, not node properties, and the DB is one-taxonomy-per-file).
Capture them as a separate decision — see open questions.

### Reconciliation note (no edits made)

`GROUP_0016` links via `composed_primarily_of` to **`CL:0020004`** "internal
globus pallidus shell projection neuron", while
`kb/graphs/BG/GPi_shell_neuron.yaml` asserts **`CL:4310096`** "GPi Shell
internal globus pallidus shell projection neuron (Primate)". Both terms are
live in CL (checked via OLS); the KG holds the general term, the KB the
primate-specific one. Ingested stubs will therefore carry `cl_id: CL:0020004`,
differing from the hand-authored graph. Flagged for curator resolution at the
WS6 rewiring stage.

---

## Anatomy re-probe — 2026-10-25 (crude locations now present)

**Anatomy has landed, and it is usable.** It is not where WMBv1 puts it, and
the path has one trap, but every terminal node is covered and the entries carry
cell ratios.

### Where it lives: two hops, via the CL/PCL term

```
(BG Individual) -[:exemplar_data_of]-> (CL/PCL class) -[:some_soma_located_in]-> (DHBA term)
```

Not on the cluster node, and not reachable via `composed_primarily_of`
(0 nodes, 0 edges by that route). The predicate is `some_soma_located_in`
(`CLM_0010001`) — note **not** WMBv1's `obsolete_some_soma_located_in`.

Worked example, `BG:CS20250428_GROUP_0016` "GPi Shell" → `CL:4310096`:

| Region | `cell_ratio` |
|---|---|
| `DHBA:10344` internal segment of globus pallidus | 0.6 |
| `DHBA:10333` striatum | 0.1 |
| `DHBA:10343` external segment of globus pallidus | 0.1 |

Each edge also carries `comment: "Location assignment based on CCF broad
region."` and `evidence: EFO:0008992` — which resolves to **MERFISH**. So these
are spatial measurements binned to broad CCF regions, not annotation guesses.
That is better provenance than "crude" suggests, and it should be recorded as
such: `method` is MERFISH, the *coarseness* is in the binning, not the evidence.

### Coverage and granularity

**All 61 Groups have anatomy** — 86 location entries total, every one with a
`cell_ratio`. One CL/PCL term per node at every level, so no fan-out.

| Regions per Group | Groups |
|---|---|
| 1 | 40 |
| 2 | 17 |
| 3 | 4 |

Only **five distinct regions** are used across the whole taxonomy — striatum
(53 Groups), external segment of globus pallidus (17), substantia nigra (11),
subthalamic nucleus (3), internal segment of globus pallidus (2). This is as
crude as it gets: the five BG nuclei, nothing below them. It is still enough
for the job anatomy does in candidate scoring — separating BG candidates from
the rest of the brain, and separating striatal from pallidal from nigral types
within BG.

**Ratios are not normalised.** Per-Group sums range 0.1 → 1.0 (median ~0.65):
cells outside the five BG nuclei simply have nowhere to go, and ratios appear
rounded to 1 d.p. Treat `cell_ratio` as "fraction of this cluster's cells in
this region", with the remainder meaning *elsewhere*, not *unknown*. Anything
that assumes the ratios sum to 1 will be wrong.

### Trap — take anatomy at Group level only

`exemplar_data_of` is **not level-matched**. `CS20250428_CLASS_0002`
"CN GABA-Glut", `CS20250428_NEIGH_0003` "Subpallium GABA-Glut" and
`CS20250428_SUBCL_0014` "CN GABA-Glut" *all* point at `CL:4310096` — the
GPi Shell term, derived from a single descendant Group. Following the link at
those levels would attribute one Group's GPi locations to an entire
neighbourhood.

Some higher-level links are genuinely level-matched (`SUBCL_0018` "Macrophage"
→ `PCL:0160091` "Macrophage border associated macrophage (Primate)"), so the
relation is not uniformly wrong — but it is not reliably right either, and
non-Group anatomy coverage is thin regardless (Subclass 11/36, Class 1/12,
Neighborhood 1/4).

**Rule: gate the anatomy match on `labelset.short_form = 'Group'`.** If
ancestor anatomy is wanted later, roll it up from descendants (sum ratios
across child Groups) rather than following the CL link — that is what WMBv1's
rollup edges amount to anyway.

### Trap — the DHBA namespace prefix is unmapped

DHBA terms are in the KG (233 classes) but carry
`curie = "ns3:DHBA_10344"` — an auto-generated namespace placeholder. The IRI
is correct (`https://purl.brain-bican.org/ontology/dhbao/DHBA_10344`).

Worth reporting upstream as a KG prefix-map gap. Until then, normalise in
Cypher from the IRI rather than reading `curie`:

```cypher
replace(split(a.iri,'/')[-1], '_', ':')   // → "DHBA:10344"
```

Filter on `a.iri CONTAINS '/dhbao/'` for the same reason — `a.curie STARTS
WITH 'DHBA'` matches nothing today and would silently return zero anatomy.

### Trap — `collect()` on an unmatched OPTIONAL MATCH

A bare `collect({anat_id: …})` emits one all-null junk entry per node with no
anatomy — 52 of them here (Class 12, Subclass 36, Neighborhood 4). Wrap in
`CASE WHEN a IS NULL THEN null ELSE {…} END`; neo4j drops nulls from
`collect()`. Verified: with the guard, `sum(size(anat)) = 86` and non-Group
levels get `[]`.

> This is a latent issue in `CCN20230722.cypher` too, which uses the unguarded
> form. For WMBv1 it produces `AnatomicalLocation` entries with `id: null` on
> every node lacking spatial data. Worth checking the WMBv1 YAML for null-id
> location entries — separate from this plan.

### Verified Cypher

```cypher
MATCH (node:Individual)-[:has_labelset]->(labelset)
WHERE node.curie STARTS WITH "BG:"
OPTIONAL MATCH (node)-[:subcluster_of]->(parent:Individual)
  WHERE parent.curie STARTS WITH "BG:"
OPTIONAL MATCH (node)-[:composed_primarily_of]->(cl:Cell)
  WHERE cl.curie =~ "CL:\\d{7}"
OPTIONAL MATCH (node)-[:exemplar_data_of]->(ex)-[r:some_soma_located_in]->(a)
  WHERE labelset.short_form = "Group" AND a.iri CONTAINS "/dhbao/"
WITH node, parent, cl, labelset,
     collect(CASE WHEN a IS NULL THEN null ELSE {
       anat_id:    replace(split(a.iri,"/")[-1], "_", ":"),
       anat_label: a.label,
       cell_ratio: toFloat(head(r.cell_ratio)),
       source:     head(r.evidence),
       notes:      head(r.comment),
       exemplar_term: ex.curie
     } END) AS anat
RETURN cl, node, parent.curie AS parent_curie,
       labelset.short_form AS level, anat
```

Returns `rows=113, with_parent=109, with_cl=87, anat_entries=86, levels=4`.

Two ingest-side notes on the `anat` payload:

- `_extract_node` expects `cell_count` / `cell_ratio` / `source` as **parallel
  lists indexed by source**. Here there is exactly one source per edge, and
  scalars are accepted (`counts if isinstance(counts, list) else [counts]`,
  `taxonomy_db.py:469-478`), so scalars are fine. `cell_count` is absent —
  only ratios are published. Check nothing downstream requires an absolute
  count where only a ratio exists.
- `exemplar_term` is not a field `_extract_node` reads; it is carried in the
  query for provenance/debugging and to make the two-hop derivation auditable.
  Either drop it or add it to the field mapping deliberately.

### Reconciliation note resolved

The 2026-10-22 note flagged the KG giving `CL:0020004` where the KB asserts
`CL:4310096`. Both links now exist and they are not in conflict:
`composed_primarily_of → CL:0020004` (the general term) and
`exemplar_data_of → CL:4310096` (the primate-specific term the KB uses). The
default field mapping reads `cl_id` from `composed_primarily_of`, so ingested
stubs will carry the general term while the hand-authored graph carries the
primate one. Still a curator decision at WS6 — but it is a modelling choice
now, not a discrepancy.

### Still absent

No `nt_type` property — gap 2 and the NT provenance section stand unchanged.
Markers still `marker_gene_evidence` only, 42/61 Groups, Group level only.

### Incidental

Group nodes gained a block of `CCN20230722_*`-prefixed properties (colours,
display order, tokens, `accession_class` / `accession_subclass` /
`accession_neighborhood`). The `CCN20230722_` prefix on BG nodes looks like a
labelset-prefix artefact from the export rather than a real WMBv1 reference —
worth a question to the KG team, but none of it is needed for ingest.

---

## NT provenance — BG requires an explicit qualification `#schema`

NT for BG can be read off the cluster name (`"LAMP5-LHX6 GABA"`,
`"CN GABA-Glut"`) or off the CL target's KG labels. **Both are inferences from
annotation, not measurements at cluster level**, and per discussion with the
taxonomy authors, NT is genuinely harder to establish from snRNA-seq than it
was from the scRNA-seq that WMBv1's `nt_type_label` rests on — nuclear
transcript capture gives weaker signal on the transporter/synthesis genes
(`Slc17a6`, `Slc32a1`, `Gad1/2`) that the WMB assignment used.

This collides with a schema convention. `NeurotransmitterType.sources` says:

> Leave empty on ATLAS_TRANSCRIPTOMIC nodes (provenance implicit).

That rule is safe only when the atlas NT is itself assayed — the WMBv1 case it
was written for. For BG it would silently present a name-derived, untested
assignment as if it carried the same standing as WMBv1's. Downstream this
matters concretely: `property_comparisons` on mapping edges compare
`nt_type` between a classical node (often IHC- or ephys-backed) and the atlas
node, and `gen-report` renders that comparison as supporting evidence.

Proposed handling — **needs schema discussion before implementation**
(`CLAUDE.md` § Hitting a wall: schema changes are discussed and reviewed, never
driven by an ingest convenience):

1. **Narrow the "leave empty" rule** from "ATLAS_TRANSCRIPTOMIC nodes" to
   "ATLAS_TRANSCRIPTOMIC nodes whose NT is assayed in the source atlas", and
   require a `PropertySource` otherwise.
2. **Emit one `nt_type.sources` entry on every BG node** at ingest, identical
   across the taxonomy, e.g.:
   - `method`: `"inferred from cluster label; not assayed at cluster level
     (snRNA-seq — NT marker capture weaker than the scRNA-seq basis used for
     WMBv1)"`
   - `scope`: `"taxonomy-wide (CCN20250428)"`
   - `ref`: the taxonomy's own citation once available
3. **Record the caveat once in `taxonomy_meta.yaml`** so it is stated at the
   taxonomy level and not only replicated per node.
4. **Carry it into reports** — `gen-report` should not let a name-derived NT
   match read as corroborating evidence without the qualification visible.

If the schema discussion stalls, the fallback is option 1 from gap 2 — leave
`nt_type` null and rely on `cl_id`. An absent value is honest; an unqualified
one is not. That is a real cost to candidate scoring, but it is the safe
default, and it is reversible once the provenance route is agreed.


---

## Workstream 1 — Parameterise the anatomy-ontology loader `#dev`

**Required.** The 2026-10-25 re-probe confirms BG anatomy is DHBA, arriving
through the source export, so `anatomical_location` is an `INGEST_FIELD` — no
`ENRICHMENT_FIELDS` concern, and `just reingest` will refresh it normally.

The prefix is settled: `DHBA`, ontology file `dhbao-full.json`. Only the five
BG nuclei are actually referenced, but the closure table still earns its place
— it is what lets a classical node annotated to a *subregion* (or to a UBERON
term) match a Group annotated to the containing nucleus. Without it, anatomy
scoring is exact-ID-match only, and most classical BG nodes are annotated below
nucleus level.

The KG itself carries a 233-term DHBA subset with `part_of` (230) and
`SUBCLASSOF` (31) edges plus 212 DHBA→UBERON links — enough for a fallback
closure, but `dhbao-full.json` (3,317 terms) is the better source for resolving
arbitrary classical-node UBERON IDs. Use the file; keep the KG subset in mind
only if the download path is unavailable.

Code change, `src/evidencell/` — out of scope in curation mode; file as a
dev-request issue.

Current coupling (all in `taxonomy_db.py`):

| Location | Coupling |
|---|---|
| `MBA_ONTOLOGY_URL`, `MBA_RELEASES_API` (:29-36) | Hardcoded mouse repo |
| `_parse_mba_obograph()` (:1380-1426) | Literal `"MBA:"` prefix ×3; `MBA:ENTITY` root guard |
| `build_anat_closure(mba_json)` (:2141) | Parameter name only; logic is prefix-agnostic |
| `_resolve_mba_by_name()` (:3073) | Name only; logic is prefix-agnostic |
| `find_candidates` UBERON→atlas resolution (:3261-3313) | Comments/messages say MBA; logic reads `anat_terms` |
| `just fetch-mba-ontology` / `just build-anat-closure` | Hardcoded `conf/mba/mbao-full.json` |

Proposed surface:

```python
ANATOMY_ONTOLOGIES = {
    "MBA":  {"repo": "brain-bican/mouse_brain_atlas_ontology",             "file": "mbao-full.json"},
    "DHBA": {"repo": "brain-bican/developing_human_brain_atlas_ontology",  "file": "dhbao-full.json"},
    "HBA":  {"repo": "brain-bican/human_brain_atlas_ontology",             "file": "hbao-full.json"},
}
```

- `_parse_obograph(path, prefix)` — prefix passed in, `{prefix}:ENTITY` guard
  retained generically.
- `fetch_ontology(prefix, dest)` → `conf/anatomy/{prefix.lower()}/{file}`.
  Keep `conf/mba/mbao-full.json` working (symlink or fallback lookup) so
  existing WMBv1 runs don't break.
- `build_anat_closure()` resolves its prefix from
  `read_taxonomy_meta(taxonomy_id).anatomy_ontology` — the field already exists
  and is already populated per taxonomy — so `just build-anat-closure {id}`
  needs no new argument.
- New recipe `just fetch-anat-ontology {PREFIX}`; keep `fetch-mba-ontology` as
  a thin alias.

Note: DHBA is sourced from the repo root / release assets. The
`purl.brain-bican.org/ontology/dhbao/dhbao-full.json` PURL currently returns a
GitHub HTML page, not JSON — use the GitHub release-asset URL pattern that
`fetch-mba` already uses, and verify the asset list per ontology (the dhbao
latest release lists no assets via the API, so fall back to
`raw.githubusercontent.com/.../main/dhbao-full.json`).

**Acceptance:** `just fetch-anat-ontology DHBA` then
`just build-anat-closure CCN20250428` populates `anat_terms` (~3,300 rows),
`anat_hierarchy` (~3,500), and a non-empty `anat_closure`; WMBv1's existing
closure rebuilds byte-identically.

---

## Workstream 2 — Cypher export + field mapping `#ingest-taxonomy`

Step 1 (inspect the KG) is **done** — see the probe section. Remaining:

**Step 2 — write `inputs/taxonomies/CCN20250428.cypher`.** Use the verified
query in the *Anatomy re-probe* section — it supersedes the anatomy-free draft
shown here. Retained for contrast; the 2026-10-22 version was:

```cypher
MATCH (node:Individual)-[:has_labelset]->(labelset)
WHERE node.curie STARTS WITH "BG:"
OPTIONAL MATCH (node)-[:subcluster_of]->(parent:Individual)
  WHERE parent.curie STARTS WITH "BG:"
OPTIONAL MATCH (node)-[:composed_primarily_of]->(cl:Cell)
  WHERE cl.curie =~ "CL:\\d{7}"
RETURN cl, node, parent.curie AS parent_curie,
       labelset.short_form AS level,
       [] AS anat
```

Head-comment the real file with the BG specifics as `CCN20230722.cypher` does:
the two-hop anatomy path, the Group-level gate, the `ns3:` prefix workaround,
the `CASE WHEN` null guard, ratios that do not sum to 1, and MERFISH/CCF-broad
provenance. Add an `nt_type` column once gap 2 is resolved.

**Step 3 —** `uv sync --extra kg`, then
`just fetch-taxonomy-kg inputs/taxonomies/CCN20250428.cypher CCN20250428`.
(`neo4j` is not currently installed in this worktree's venv; the probe went via
the HTTP endpoint. The bolt endpoint needs no auth.)

**Step 4 — field mapping** via `workflows/ingest-taxonomy.md`. The non-default
entries are few:

```json
{
  "taxonomy_id": "CCN20250428",
  "anatomy_ontology": "DHBA",
  "row_keys": { "node": "node", "parent_curie": "parent_curie",
                "cl": "cl", "anat": "anat", "level": "level" },
  "field_mappings": {
    "defining_markers": ["marker_gene_evidence"],
    "_anat_note": "anat is two-hop via exemplar_data_of; Group level only",
    "nt_type": [],
    "np_markers": [], "tf_markers": [], "merfish_markers": [],
    "defining_markers_scoped": [], "neighborhood": []
  }
}
```

Everything else falls through to the shared defaults. Set `"confirmed": true`
only after the ingest gate shows the expected level counts (61/36/12/4).

## Workstream 3 — Levels from the graph `#ingest-taxonomy`

Already supported, no code change expected:

- `level` comes from `labelset.short_form` in the Cypher (`_extract_node`,
  `taxonomy_db.py:417-419`) — no level names are hardcoded on this path.
- `_build_level_hierarchy()` (:570-655) derives ranks **topologically from
  parent edges**: leaves get rank 0, parents rank+1. Integer ranks (S1) flow
  through `find-candidates` / `emit-stage-b` unchanged, so an unfamiliar
  hierarchy (Class > Group > …) needs no registration anywhere.

Two items:

1. **Cross-check against curator-supplied level names.** The ingest gate should
   print the derived `level_hierarchy` (name, rank, count, is_terminal) and
   diff it against the names the curator provides. Divergence means either a
   missing labelset edge or an unexpected parent edge — investigate, don't
   override.
2. **`_ACCESSION_LEVEL_MAP` (:662-669)** needs the BG type-codes —
   `GROUP`, `SUBCL`, `CLASS`, `NEIGH` (note `SUBCL`, not WMBv1's `SUBC`, and
   `CLASS`, not `CLAS`). It is only the *fallback* used when `level` is absent,
   and the probe confirms all 113 BG nodes carry `has_labelset`, so it will
   never be reached on this path. Add it anyway for cached-export safety —
   one-line change, bundle into the WS1 dev request.

---

## Workstream 4 — Species / taxon `#schema` `#dev`

Decision: single taxon, `NCBITaxon:9443` Primates.

This needs **no schema refactor**. `TaxonomyMeta.species_id`/`species_label`
are free-text CURIE + label (`taxonomy_db.py:66-68`), and `_node_to_dict`
stamps `{id, label, name_in_source}` onto every node from meta — a
higher-rank taxon is as valid as a species there. The existing BG stub already
uses exactly `{id: NCBITaxon:9443, label: Primates, name_in_source: Primates}`,
so ingested nodes will match the hand-authored ones.

Minor consistency items:

- The field is *named* `species_*` while holding an order-rank taxon. Leave as
  is for this ingest; if it bothers us later, an aliased `taxon_*` rename is a
  separate schema chore, not a blocker.
- `NCBITaxon:9443` must resolve via the OAK semsql term check in the pre-write
  hook — it already does, since the existing BG graph passes validation.
- `annotation_transfer/src/annotation_transfer/taxonomies.py:92` records
  `CCN20250428` with `species="mouse"`. Wrong; fix to primate when touching
  that file for the stats URLs (WS5).

**Cross-species gene symbols — flag, not a blocker.** BG consensus marker
symbols will be human-style (`VIP`), while classical BG nodes in the KB were
authored mouse-style (`Vip`). Marker matching in `find_candidates` is a
SQL `symbol IN (...)` test (`taxonomy_db.py:2029, 2066`) — case-sensitive in
SQLite without `COLLATE NOCASE`. Expect silent zero-marker matches on the first
mapping run. Case-insensitive matching (or the symbol normalisation in
`planning/gene_id_normalisation_plan.md`) should land before BG mapping, and is
worth its own dev-request issue.

---

## Workstream 5 — MapMyCells + precomputed expression `#at` `#map-cell-type`

Available locally, as for WMBv1. Mirror the WMBv1 chain:

1. Record the stats + markers paths in `inputs/taxonomies/CCN20250428_meta.yaml`
   under `mapmycells:` (`at_taxonomy_id: CCN20250428`, plus
   `local_stats_path` / `local_markers_path` — these fields already exist on
   `MapMyCellsMeta`). Fill `stats_s3_url` / `markers_s3_url` if the files have
   public S3 equivalents; local paths are sufficient otherwise.
2. `just generate-gene-mapping {stats_h5} conf/gene_mapping_CCN20250428.tsv`
3. `just enrich-marker-union CCN20250428 {stats_h5} {gene_mapping}` — populates
   `precomputed_expression` across levels, which `build-taxonomy-db` then
   propagates into `node_expression`. Without this, `find-candidates` falls
   back to binary marker scoring (it warns on stderr).
4. Fill `stats_s3_url` / `markers_s3_url` and fix `species` in
   `annotation_transfer/.../taxonomies.py` for the `CCN20250428` spec so local
   MapMyCells runs resolve.

Note the open ROADMAP item on HDF5 path standardisation — put the BG HDF5
wherever that decision lands, not wherever the first run happens to write it.

---

## Workstream 6 — KB wiring (deferred; content edits, separate session)

Not part of this plan's execution. Listed so it isn't lost:

- Backfill `taxonomy_id: CCN20250428` onto the HMBA stubs in
  `kb/graphs/BG/GPi_shell_neuron.yaml` (they currently carry `atlas:
  HMBA_BG_Consensus` and an accession but no `taxonomy_id`).
- Pending rename `GPi_shell_neuron.yaml` → `BG_HMBA.yaml`
  (`planning/content-notes/kb_restructure.md`).
- Re-run `map-cell-type` for the BG nodes against the real taxonomy DB — the
  existing edges were authored by hand against atlas metadata, before any
  taxonomy store existed.

---

## Sequence

```
[HOLD]  wait for brain_cell_KG refactoring to land, then re-run both probes
        to confirm the findings still hold                           [GATE]
   │
WS2.1  inspect KG                           ✔ 2026-10-22, anatomy ✔ 2026-10-25
   │
WS1    just fetch-anat-ontology DHBA        (needs the loader parameterisation)
   │
WS2.2  write inputs/taxonomies/CCN20250428.cypher
         └─ verified query from the Anatomy re-probe section
   │
WS2.3  uv sync --extra kg
       just fetch-taxonomy-kg inputs/taxonomies/CCN20250428.cypher CCN20250428
   │
WS2.4  workflows/ingest-taxonomy.md
         │  meta gate — name, NCBITaxon:9443, anatomy_ontology: DHBA,
         │              mapmycells local paths, source_query          [GATE]
         │  field-mapping gate — defining_markers ← marker_gene_evidence [GATE]
         │  level cross-check — Group 61 / Subclass 36 / Class 12 /
         │                      Neighborhood 4, ranks 0-3             [GATE]
         │  anatomy check — 86 location entries, all on Group nodes,
         │                  all with cell_ratio, 5 distinct DHBA regions,
         │                  zero null anat_id                         [GATE]
         ▼
       just ingest-taxonomy-db  →  kb/taxonomy/CCN20250428/{group,subclass,
                                     class,neighborhood}.yaml + .db
   │
       just build-anat-closure CCN20250428        (DHBA, via WS1)
   │
WS5    just generate-gene-mapping {stats_h5} conf/gene_mapping_CCN20250428.tsv
       just enrich-marker-union CCN20250428 {stats_h5} {gene_mapping}
       just build-taxonomy-db CCN20250428          ← the real marker panel
   │
smoke  just find-candidates kb/graphs/BG/GPi_shell_neuron.yaml \
         classical_gpi_shell CCN20250428 0
       └─ expect CS20250428_GROUP_0016 "GPi Shell" top-ranked, now with a
          *non-zero anatomy component* — the classical node's DHBA:10344
          should match the Group's 0.6-ratio GPi entry directly, and reach
          striatum/GPe through the DHBA closure. NT still reads zero (gap 2).

[pending] NT provenance — schema discussion before any nt_type is written
[later]   WS6 KB rewiring — separate session, content edits
```

## Dev-request issues to file

1. **Map `field_mapping.json` targets to top-level row columns** (gap 2) —
   unblocks `nt_type` for BG and makes any derived Cypher column mappable.
   Bundle the `_ACCESSION_LEVEL_MAP` BG type-codes (`GROUP`/`SUBCL`/`CLASS`/
   `NEIGH`) into the same issue.
2. **Case-insensitive / normalised gene-symbol matching** (WS4) — blocks marker
   scoring across mouse↔primate symbol conventions. Needed before BG mapping,
   not before BG ingest.
3. **Parameterise the anatomy-ontology loader** (WS1) — now firmly required;
   DHBA confirmed as the target ontology.
3b. **KG bug report (upstream, not an evidencell issue):** DHBA terms carry
   `curie = "ns3:DHBA_10344"` — the `dhbao` namespace is missing from the KG
   prefix map. Worked around in Cypher by deriving the CURIE from the IRI.
4. **Schema discussion, not an issue: NT provenance on atlas nodes.** Narrowing
   the `NeurotransmitterType.sources` "leave empty" rule is a schema change and
   must be discussed and reviewed first — it is exactly the case `CLAUDE.md`
   warns against resolving unilaterally from inside an ingest.

All four wait on the KG refactor; file them when implementation starts, so the
proposed surfaces are written against the post-refactor code.

## Open questions for the curator

1. ~~**BG anatomy**~~ — **answered 2026-10-25.** DHBA, two-hop via the CL/PCL
   term, Group level only, five BG nuclei, `cell_ratio` present on every entry,
   MERFISH evidence binned to CCF broad regions. Residual sub-questions:
   (a) are the un-normalised ratios (sums 0.1–1.0) the intended published form,
   or is a region cut-off being applied upstream? (b) should ancestor levels
   get rolled-up anatomy from their Groups, or stay empty? (c) is the
   non-level-matched `exemplar_data_of` at Class/Neighborhood intended, or an
   export artefact worth reporting?
2. **`nt_type` route and its provenance** — recommend the
   `field_mapping.json` top-level-column change (gap 2, option 2) *plus* the
   mandatory qualification. The schema side needs a discussion before anything
   is implemented; see the NT provenance section.
3. **Paths to the local precomputed stats HDF5 and summary expression files.**
   WS5 is on the critical path for BG — rationale markers cover only 42 of 61
   Groups and nothing above Group level. More markers may be available
   upstream; curator decision is to **proceed without them for now**, so treat
   any additional marker source as a later enrichment via
   `just add-expression` / `enrich-marker-union` rather than an ingest input.
4. **The 58 curated BG↔WMBv1 SKOS correspondences** — ingest them as
   `MappingEdge` records, keep them as a validation oracle for a cross-species
   methods audit, or leave them in the KG for now? They are cross-taxonomy
   assertions, so they touch the parked multi-taxonomy-DB decision.
5. **`CL:0020004` (KG) vs `CL:4310096` (KB)** on GPi Shell — which is
   authoritative for the ingested stub? (See reconciliation note.)
6. Confirm `CCN20250428` is the taxonomy_id of record, with `CS20250428_*`
   accessions — matching the WMBv1 CCN/CS precedent, and what the AT registry
   already uses.

# AT evidence must be gated on a node-declared source-annotation → lit-type correspondence

**Status:** dev-request (draft for a branch off `main`)
**Surfaced by:** MTL/amygdala regeneration, PR #117 (`bla_vip_calretinin_interneuron` pilot)
**Related:** #61, #53, #100, #120

## Summary

In refactoring candidate selection to be programmatic (issue #96), we lost a key
**agentic judgement**: deciding *which annotated cell set in an external dataset
corresponds to which classical (literature) cell type*. That judgement requires
reading the dataset's describing paper / supplementary material — it cannot be
inferred from transcriptomic overlap alone.

Today, annotation-transfer (AT) evidence is attached to a mapping edge **by shared
atlas target cluster**: for a candidate atlas cluster, whatever source cluster best
lands on it in the AT run becomes the edge's AT evidence, presented as
`supports: SUPPORT`. The source cluster is never checked against the classical type.
So an edge can cite AT from a biologically wrong source population as positive support,
silently.

## Concrete failure

Classical type `bla_vip_calretinin_interneuron` — "BLA VIP/**calretinin (Calb2)**
interneuron-selective interneuron". Its regenerated edge to `CS20230722_CLUS_0628`
carries:

```yaml
- evidence_type: ANNOTATION_TRANSFER
  supports: SUPPORT
  run_ref: at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1
  source_cluster_label: GABA-51-Vip-Crh      # Vip/CRH — not the calretinin population
```

The Hochgerner 2023 source dataset (ArrayExpress:E-MTAB-12096) contains multiple
relevant GABAergic annotations — `GABA-50-Chat-Vip`, `GABA-51-Vip-Crh`,
`GABA-52-Calb2-Rgs12` (the calretinin one), `GABA-55-Sncg-Vip`. `GABA-51-Vip-Crh`
was attached only because its cells land on `CLUS_0628`; the calretinin cluster
(`GABA-52`) was never considered. Vip/CRH and Vip/calretinin-ISI are plausibly
different types.

## Root cause (one derivation)

`src/evidencell/stage_b_emit.py:128`:

```python
at_source_label = at_artifact.get("source_cluster_label")   # from the atlas-cluster hit
...
compute_edge_metrics(run_ref, source_label=at_source_label, edge_target=candidate)
```

The source label comes from the **atlas-keyed AT hit** (`_at_hits_from_artifact`
builds `hits[target_accession] → hit`, `taxonomy_db.py:2875`). The classical node's
identity is used only for the marker/region scoring channel; it plays no role in
choosing the AT source cluster. `compute_edge_metrics` itself already takes an
**explicit `source_label`** and is lineage-aware (missing rows above the edge
target's level are treated as negative signal).

## Fix: node-declared AT source correspondence

Put the correspondence **on the node** (consistent with "properties live on nodes;
edges compare"), then AT becomes one more edge property comparison alongside markers
and location.

### 1. New multivalued node field `at_source_sets`

The result of the agentic judgement: which annotated cell set(s), in which
dataset(s), correspond to this classical type. Authored by lit-ingest /
evidence-extraction *after* the dataset's annotations are available. Carries its
own provenance (why this label = this type).

Each entry carries a **`sources[]` list with `quote_key`**, using the *same*
`PropertySource`/`MarkerSource` machinery as `defining_markers`,
`anatomical_location`, etc. The correspondence is thereby quote-backed,
hook-validated against `references.json`, renderer-surfaced, and covered by the
anti-hallucination guard — real evidence, not an unexplained assertion. (This is
the "just like markers" model; see design-options note at the end for why we chose
a node **property** over a first-class node+edge.)

Example (JSON):

```json
{
  "id": "amygdala_intercalated_cell",
  "name": "Amygdala intercalated cell",
  "at_source_sets": [
    {
      "dataset_accession": "ArrayExpress:E-MTAB-12096",
      "source_label": "GABA-3-Foxp2_Col6a1",
      "correspondence": "SUBSET",
      "sources": [
        {
          "ref": "PMID:37884748",
          "method": "scRNA-seq cluster annotation",
          "scope": "mouse amygdala, Hochgerner 2023",
          "quote_key": "37884748_xxxxxxxx"
        }
      ],
      "notes": "One of four Foxp2 ITC clusters (GABA-1..4); molecular subtype within the classical intercalated cell."
    },
    {
      "dataset_accession": "ArrayExpress:E-MTAB-12096",
      "source_label": "GABA-1-Foxp2_Fmod",
      "correspondence": "SUBSET",
      "sources": [
        {
          "ref": "PMID:37884748",
          "method": "scRNA-seq cluster annotation",
          "scope": "mouse amygdala, Hochgerner 2023",
          "quote_key": "37884748_xxxxxxxx"
        }
      ],
      "notes": "Foxp2/Tshz1 ITC cluster; see also GABA-2, GABA-4."
    }
  ]
}
```

- **Multivalued**: a type may correspond to several source clusters (lumping) or
  span datasets. Each `source_label`'s transfer profile becomes an independent AT
  evidence item on the edge. (The `amygdala_intercalated_cell` ↔ GABA-1/2/3/4-Foxp2
  case above is the `SUBSET`×4 lumping example.)
- **`dataset_accession` + `source_label` = biology** (stable, from the paper).
- **`correspondence`** (enum: `EXACT` / `PARTIAL` / `SUPERSET` / `SUBSET`) records
  the nature of the source→type match, so a lumped/partial correspondence is not read
  as a clean identity. (`SUBSET` = source cluster is one molecular subtype within the
  classical type; `SUPERSET` = source cluster is broader than the classical type.)
- **`sources[]` (with `quote_key`) = provenance.** The verbatim paper quote(s)
  justifying "this annotated cell set corresponds to this classical type". Same shape
  and validation as marker/anatomy sources. `notes` remains free-text colour, but the
  load-bearing justification lives in `sources[]`, not `notes`.

Do **not** reuse `prior_dataset_accession` / `prior_cluster_label`: those mean
"this node *is* that prior transcriptomic cluster" (`PRIOR_TRANSCRIPTOMIC`
definition basis) — a different claim.

### 2. Repoint the source label in `emit-stage-b`

Instead of deriving `at_source_label` from the atlas hit, iterate the node's
`at_source_sets`. For each declared `source_label` and each candidate cluster:

```python
for src in node.get("at_source_sets", []):
    run_ref = resolve_run(src["dataset_accession"], target_taxonomy)   # operational lookup
    metrics = compute_edge_metrics(run_ref, source_label=src["source_label"],
                                   edge_target=candidate)
    # emit one ANNOTATION_TRANSFER evidence item per declared source set
```

Everything downstream of `compute_edge_metrics` is unchanged — the property
comparison, F1 table, and evidence item all already exist.

### 3. Keep `run_ref` operational, not on the node

The node declares `(dataset_accession, source_label)` only. Which AT **run** (target
atlas / version / tool) supplies the numbers is resolved at map time by matching
`(dataset_accession, target_taxonomy)`. Re-running AT against a new atlas version
must not churn the node.

### 4. Implementation note — surface the negative signal

When a declared source set does **not** transfer to a candidate cluster, emit an
AT evidence item with `supports: AGAINST` (or `NO_EVIDENCE`), **not** nothing.
Today `_at_evidence` returns `None` for a (run, label, target) combo with no rows
(`stage_b_emit.py:595`), which would silently drop exactly the negative evidence we
want: "the calretinin source population does not land on this candidate." AT should
be able to come out CONSISTENT / APPROXIMATE / DISCORDANT / absent, symmetric with
marker and location comparisons.

### 5. `supports:` must respect the edge's own level (secondary fix)

Separately: the mechanical `supports:` default is set from the best F1 across **all**
levels, so `SUPPORT` can be earned by a coarse-level match (e.g. subclass) that is
weaker at the edge's own cluster level. Make `supports_default` level-aware —
`SUPPORT` only when the qualifying F1 is at or below the edge target's own rank.

## Consequences / migration

- **Schema**: add `AtSourceSet` class (fields: `dataset_accession`, `source_label`,
  `correspondence`, `sources` [range `PropertySource`, reusing the existing class],
  `notes`) + `CellTypeNode.at_source_sets` (multivalued); add `CorrespondenceType`
  enum (`EXACT`/`PARTIAL`/`SUPERSET`/`SUBSET`). Additive, no breaking change.
- **Graph-level `annotation_transfer_datasets[].cell_types`** becomes derivable
  (union over nodes' `at_source_sets`) rather than a hand-maintained parallel list.
- **Workflow**: lit-ingest / evidence-extraction gains a step that, once the dataset's
  annotations are available, authors `at_source_sets` on the node. This is the
  home for the agentic judgement lost in #96.
- **Ordering dependency**: the correspondence needs the dataset pulled (or at least its
  annotation labels + describing paper queried) before it can be authored.

## Design options considered (why a node property, not a node+edge)

Three ways to represent the source-annotation → lit-type correspondence, in
increasing rigor/cost:

1. **Free-text `notes`** — rejected. Unstructured, not validated against
   `references.json`, invisible to the renderer and the anti-hallucination hook,
   lost on YAML round-trip (the pattern CLAUDE.md explicitly discourages). Only a
   throwaway placeholder.
2. **Node property with quote-backed `sources[]`** — **chosen** (this ticket).
   Minimal change consistent with the KB's provenance conventions; keeps AT as
   **one-hop** direct evidence on the lit→atlas edge; unblocks the pipeline fix as
   scoped.
3. **Source cell sets as first-class nodes + edges** — the north-star (below), but a
   larger change deferred to its own ticket.

### North-star (separate ticket): source cell sets as `PRIOR_TRANSCRIPTOMIC` stub nodes

The uniform end-state: each referenced external annotated cell set becomes a **thin
`PRIOR_TRANSCRIPTOMIC` stub node** (id = `dataset:source_label`,
`prior_dataset_accession` / `prior_cluster_label` — fields that already exist),
mirroring the thin-stub pattern used for atlas targets and cross-type reconciliation.
The lit-type ↔ source-cluster correspondence then becomes a proper `MappingEdge` with
quote-backed evidence, confidence, and a SKOS predicate.

Why it's deferred, not chosen now: AT metrics are inherently **source→atlas**, so under
this model AT attaches to a *source↔atlas* edge and lit→atlas becomes a **two-hop**
derived claim (lit→source→atlas). `find-candidates`, `emit-stage-b`, and `gen-report`
all reason over lit→atlas edges today, so this ripples much wider than the current fix.

**Migration is non-lossy: option 2 → option 3 is a strict superset.** An
`at_source_sets` entry `(dataset_accession, source_label, correspondence, sources[])`
is exactly the data needed to later mint the stub node and convert the entry into a
lit→source edge. Choosing option 2 now forecloses nothing.

## Repro

```
just build-taxonomy-db CCN20230722 && just build-anat-closure CCN20230722
just find-candidates kb/graphs/medial_temporal_lobe_amygdala/bla_vip_calretinin_interneuron.yaml \
  bla_vip_calretinin_interneuron CCN20230722 0 5
just emit-stage-b  kb/graphs/medial_temporal_lobe_amygdala/bla_vip_calretinin_interneuron.yaml \
  bla_vip_calretinin_interneuron CCN20230722 0 5
# CLUS_0628 edge's ANNOTATION_TRANSFER: source_cluster_label = GABA-51-Vip-Crh,
# attached with no check that it corresponds to the VIP/calretinin ISI type.
```

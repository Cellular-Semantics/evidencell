# Annotation Transfer Feedback Orchestrator

> **STATUS: Pipeline implemented; KB import orchestrator pending**
> The `annotation_transfer/` proto-repo provides dataset retrieval, MapMyCells
> mapping, and F1 scoring. The orchestrator steps below for importing results
> into the KB are not yet automated.

---

## Purpose

Closes the experimental feedback loop. Annotation transfer experiments proposed
in M4 reports (MapMyCells, Seurat label transfer, scANVI) return results that
are imported as `AnnotationTransferEvidence` items, potentially upgrading mapping
confidence from MODERATE to HIGH.

---

## Pipeline tools (`annotation_transfer/`)

The annotation transfer proto-repo provides three stages:

| Stage | Tool | Description |
|-------|------|-------------|
| **Preflight** | `just at-preflight FILE` | Estimate memory, gate large datasets |
| **Convert** | `just at-convert INPUT OUTPUT [--cluster-col COL]` | Sanitise h5ad for MapMyCells (raw counts, sparse CSR, minimal obs/var) |
| **Score** | `just at-score MMC_CSV LABELS OUTPUT` | Compute F1 matrix from MapMyCells CSV + source labels |

For dataset retrieval from heterogeneous sources, use the **retrieve_dataset** skill
(`.claude/skills/retrieve_dataset.md`), which handles format detection, R conversion,
annotation inspection, and the preflight gate.

MapMyCells itself is run via `annotation-transfer map` (requires `cell_type_mapper`
optional dependency).

---

## Steps

```
Step 0  Dataset retrieval
        Use .claude/skills/retrieve_dataset.md to obtain and convert the source
        dataset to MapMyCells-ready h5ad + source labels JSON.
        [GATE] Human confirms annotation column and any cell subset filters.

Step 1  Run MapMyCells
        annotation-transfer map <input.h5ad> <taxonomy_stats> <markers> <output.json>
        Target taxonomy: WMB Yao 2023 (CCN20230722) for mouse.

Step 2  Score
        annotation-transfer score <mmc_output.csv> <labels.json> <f1_matrix.csv>
        Produces: F1 matrix CSV + best-mappings summary.
        [GATE] Human reviews F1 matrix, confirms results are sensible.

Step 3  Parsing subagent (PENDING — not yet automated)
        Extracts per-taxonomy-level F1, purity, n_cells from the scoring output.
        Maps results to KB node IDs.
        Produces: proposed AnnotationTransferEvidence YAML block.

Step 4  [GATE] Human confirms
        Reviews proposed evidence block. Confirms node mappings are correct.

Step 5  Append to KB
        AnnotationTransferEvidence appended to relevant MappingEdge.

Step 5b Direct expression analysis
        When raw count data is available (h5ad or TSV), assess expression of
        key markers and neuropeptides from the source dataset. For each marker
        in the classical node's defining_markers and neuropeptides:
        - Compute detection rate (% cells > 0) and mean counts, split by
          source label if multiple subtypes exist.
        - Add a source entry (marker_type: TRANSCRIPT, method: "scRNA-seq raw
          counts ({accession}, re-analysis)") to the relevant marker on the
          classical node.
        - Update `node_a_value` on all edge property_comparisons that reference
          the marker, to include the quantitative detection rate.
        Also check negative markers (Pvalb, Calb1, Vip, etc.) — sparse or
        absent expression confirms the negative marker status.
        [GATE] Human reviews expression summary before KB update.

Step 5c Target-side expression analysis (OPTIONAL — future)
        When WMB h5ad files (by taxonomy class or dissection region) are
        available locally, assess target-side expression of the same markers
        in the candidate atlas clusters. This would upgrade property comparisons
        from NOT_ASSESSED to a concrete alignment (e.g., Grm1 present/absent
        in cluster 0769). See note below on WMB expression files.

Step 6  Confidence re-assessment
        Re-evaluate MappingConfidence per decision guide given new experimental
        evidence. Flag edges where confidence may upgrade.

Step 7  Report regeneration
        Run `just gen-report` on the updated graph file. Biologist reviews
        updated confidence levels and evidence chain.
```

---

## Key design decisions (from ROADMAP)

- **Source and target species are explicit**: `source_species` and
  `target_species` fields on `AnnotationTransferEvidence` (cross-species by
  design — typically primate → mouse WMBv1).
- **Discordance handling**: if annotation transfer reports LOW confidence but
  literature strongly supports the mapping, experimental evidence takes
  precedence, but the conflict must be documented as a caveat.
- **Confidence upgrade path**: HIGH requires ≥2 independent evidence types
  including ≥1 experimental. Annotation transfer is the primary route to
  HIGH confidence for atlas mappings.
- **Preflight gate**: Large datasets (>available RAM) require explicit human
  confirmation before loading. The preflight module estimates memory from
  HDF5 metadata without loading the matrix.

---

## WMB expression files for target-side marker assessment (Step 5c)

The Allen Brain Cell Atlas provides h5ad expression matrices partitioned by
major taxonomy class and/or dissection region. These can be used to directly
assess marker expression in candidate atlas clusters — resolving NOT_ASSESSED
property comparisons (e.g. Grm1 in cluster 0769).

**Potential approach:**
- Download the relevant class-level h5ad (e.g. `WMB-10X/20230830/expression_matrices/
  WMB-10Xv3-CTX-MGE-GABA/`) — much smaller than the full WMB matrix.
- Subset to cells in the candidate clusters (0767–0774 for Sst Gaba_3).
- Compute detection rate and mean expression for each marker of interest.
- Update `node_b_value` on the relevant property comparisons with quantitative data.
- This would turn mGluR1/Grm1 NOT_ASSESSED → CONSISTENT or DISCORDANT with real numbers.

**Status:** Not yet implemented. Files are available on the Allen S3 bucket.
This is a high-value addition because it removes the largest remaining gap in
the property comparison matrix without requiring new experiments.

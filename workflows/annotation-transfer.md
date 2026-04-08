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

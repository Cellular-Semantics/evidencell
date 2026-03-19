# Annotation Transfer Feedback Orchestrator

> **STATUS: PENDING — M5 work**
> This orchestrator is not yet implemented. See `planning/ROADMAP.md §M5` for
> the full design. The stub below documents the intended structure.

---

## Purpose

Closes the experimental feedback loop. Annotation transfer experiments proposed
in M4 reports (MapMyCells, Seurat label transfer, scANVI) return results that
are imported as `AnnotationTransferEvidence` items, potentially upgrading mapping
confidence from MODERATE to HIGH.

---

## Intended steps

```
Step 0  Input
        Raw annotation transfer output file (CSV or JSON) provided by user.
        Specifies: which atlas, which tool, which taxonomy levels evaluated.

Step 1  Parsing subagent
        Extracts per-taxonomy-level F1, purity, n_cells from the raw output.
        Maps results to KB node IDs.
        Produces: proposed AnnotationTransferEvidence YAML block.

Step 2  [GATE] Human confirms
        Reviews proposed evidence block. Confirms node mappings are correct.

Step 3  Append to KB
        AnnotationTransferEvidence appended to relevant MappingEdge.

Step 4  Confidence re-assessment
        Re-evaluate MappingConfidence per decision guide given new experimental
        evidence. Flag edges where confidence may upgrade.

Step 5  Report regeneration
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

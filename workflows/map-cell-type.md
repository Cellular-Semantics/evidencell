# Mapping Hypothesis Orchestrator

> **STATUS: PENDING — M3 work**
> This orchestrator is not yet implemented. See `planning/ROADMAP.md §M3` for
> the full design. The stub below documents the intended structure.

---

## Purpose

From the literature evidence base (M2) and taxonomy-derived atlas metadata (M1),
proposes mapping edges and confidence assessments. The curator's initial
hypothesis (which classical types map to which atlas types, and at what
relationship type) is the primary intellectual input — the orchestrator
substantiates, tests, and documents it.

**Prerequisites**:
- `CellTypeNode` stubs for both classical and atlas types (from M1 ingestion or
  hand-curation)
- Literature evidence items populated on nodes (from M2 extraction or manual)
- Curator's explicit initial mapping hypothesis

---

## Intended steps

```
Step 0  Curator states hypothesis
        Which classical type(s) → which atlas cluster(s)?
        What relationship type is hypothesised?
        (EQUIVALENT / PARTIAL_OVERLAP / CROSS_CUTTING / SUBSET / etc.)

Step 1  [OPTIONAL] Property-combination snippet searches
        Targeted ASTA searches for specific property combinations where M2
        evidence has gaps. Scoped to paper_catalogue.json from M2 — no new
        traversal. Queries: "{type} {marker} expression", "{type} {anatomy}
        location", "{type} GABA glutamate neurotransmitter", etc.

Step 2  Mapping hypothesis subagent
        M2 evidence + atlas metadata + curator hypothesis →
        proposed MappingEdge YAML:
          - MappingRelationship
          - MappingConfidence (per decision guide — HIGH requires ≥2 independent
            types incl. ≥1 experimental)
          - property_comparisons[] (PropertyComparison per marker/NT/location)
          - caveats[]
          - evidence item list with corpus IDs

Step 3  [GATE] Expert reviews proposed edges
        Reviews relationship type, confidence rationale, caveats.
        Cross-cutting types (one atlas type spanning multiple classical types)
        require explicit expert assessment.

Step 4  Append to KB
        Approved edges appended to kb/mappings/{region}/{graph}.yaml
```

---

## Key design decisions (from ROADMAP)

- **Single Sonnet call** for small graphs (≤5 edges). Spawn sub-agents per
  candidate edge for complex multi-type regions.
- **CB MLI example must be in-context** — the MLI1/MLI2 cross-cutting case is
  the canonical worked demonstration of non-trivial inference.
- **No HIGH confidence from literature alone**: agent is explicitly instructed
  to check the decision guide. Annotation transfer or electrophysiology/
  morphology data required for HIGH.
- **No literature found**: propose `UNCERTAIN` confidence and document the
  evidence gap explicitly. Do not guess.

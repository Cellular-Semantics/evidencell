# Mapping schema — glossary preamble

**Date:** 2026-05-12
**Schema:** [`schema/celltype_mapping.yaml`](../schema/celltype_mapping.yaml)
**Plan:** [`planning/phase_2_schema_overhaul_plan.md`](../planning/phase_2_schema_overhaul_plan.md)
**Tracks:** [#30](https://github.com/Cellular-Semantics/evidencell/issues/30)

How to read a `MappingEdge` after the Phase 2 schema overhaul.
Refresh + restamp when the schema changes materially.

---

## Direction convention

Mapping edges are read from the `lit_type` (subject) to the
`taxonomy_type` (object). The `relationship` slot describes how the
two relate, **not** which is "primary".

`skos:broadMatch` and `skos:narrowMatch` are easy to misread because
the match goes *to* the broader / narrower thing, not *from* it. A
curator who reads "narrowMatch" as "narrowly mapped" encodes the
wrong direction.

> **`skos:broadMatch` — the lit_type is *narrower* than the
> taxonomy_type.** Read
> `lit_OLM --skos:broadMatch--> Sst_Gaba_3_supertype`
> as "OLM has a broad match — the supertype is the broader thing."
>
> **`skos:narrowMatch` — the lit_type is *broader* than the
> taxonomy_type.** Read
> `lit_classical_basket --skos:narrowMatch--> mli2_cluster`
> as "classical basket has a narrow match — this specific cluster is
> the narrower thing."

## Relationship value set

| Value | Use when |
|---|---|
| `skos:exactMatch` | One-to-one identity. Convergent multi-source evidence; AT F1 ≥ ~0.8 plus matching markers + anatomy. |
| `skos:closeMatch` | Same-type judgement under partial information (F1 ~0.65–0.8, or non-AT evidence converges but does not yet rise to exactMatch). Conservative default for candidate-synonym-style cases. |
| `skos:broadMatch` | The lit_type is narrower than the taxonomy_type. Pair with `mapping_cardinality`. |
| `skos:narrowMatch` | The lit_type is broader than the taxonomy_type. Pair with `mapping_cardinality`. |
| `evidencell:PartialOverlapMatch` | Genuinely incomplete overlap; precision or recall below ~0.65, partial-set semantics. No SKOS equivalent. |
| `evidencell:CrossCuttingMatch` | The taxonomy_type cross-cuts the boundary of the lit_type (and usually at least one other lit_type). No SKOS equivalent. |
| `evidencell:NoCorrespondence` | Explicitly documents that no corresponding type exists in the target taxonomy. No SKOS equivalent. |

## Cardinality (`mapping_cardinality`)

Required when `relationship` is `skos:broadMatch` or
`skos:narrowMatch`. Recommended otherwise. Values are literal
strings (matches the SSSOM column convention; no upstream ontology):

| Value | Meaning |
|---|---|
| `1:1` | One lit_type maps to one taxonomy_type. The default for `skos:exactMatch` and `skos:closeMatch`. With `skos:broadMatch` it means "specific match suspected but not yet identifiable" (hidden 1:1). |
| `1:n` | One lit_type splits across multiple taxonomy_types. Used with `skos:broadMatch` for split cases. |
| `n:1` | Multiple lit_types collapse onto one taxonomy_type. Used with `skos:narrowMatch` for merge cases. |

## Justification (`mapping_justification`)

Tracks the provenance of the mapping decision. Bound to
[`semapv`](https://w3id.org/semapv/vocab/) — SSSOM-compatible.

| Value | Use when |
|---|---|
| `semapv:ManualMappingCuration` | Reviewed and approved by a human curator. |
| `semapv:UnreviewedManualMapping` | Manually proposed (typically agent-emitted) but not yet curator-reviewed. **Default for new edges in this KB.** |
| `semapv:LexicalMatching` | Mapping derived from name / synonym lexical match. |
| `semapv:CompositeMatching` | Multi-source evidence integration (anatomy + markers + AT F1 all converging). |
| `semapv:LogicalReasoning` | Derived by logical reasoning over schema-encoded relations. |
| `semapv:UnspecifiedMatching` | Provenance not recorded. Used sparingly. |

## Worked examples

### Exact one-to-one

```yaml
- id: edge_lugaro_to_pli3
  lit_type: classical_lugaro
  taxonomy_type: CS20230722_SUPT_1145
  relationship: skos:exactMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:CompositeMatching
  confidence: HIGH
  confidence_score: 0.96
  evidence: [...]
```

### Split (one lit_type, many atlas targets)

Each split arm is a separate edge with the same `lit_type` and
`relationship: skos:broadMatch + 1:n`:

```yaml
- id: edge_classical_int_to_mli1
  lit_type: classical_interneuron_K
  taxonomy_type: CS20230722_CLUS_5177
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:CompositeMatching
  confidence: MODERATE
  evidence: [...]

- id: edge_classical_int_to_mli2
  lit_type: classical_interneuron_K
  taxonomy_type: CS20230722_CLUS_5178
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:CompositeMatching
  confidence: MODERATE
  evidence: [...]
```

### Hidden one-to-one at higher rank

When the lit_type is suspected to equal a specific cluster but the
cluster cannot be identified from available evidence, encode at the
supertype with `skos:broadMatch + 1:1` and a note. The "1:1" carries
the hidden-but-specific reading; later evidence can split into a
cluster-level edge.

```yaml
- id: edge_olm_to_sst_gaba_3
  lit_type: olm_cell_ca1
  taxonomy_type: CS20230722_SUPT_0216
  relationship: skos:broadMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:CompositeMatching
  confidence: MODERATE
  reconciliation_note: >
    Specific cluster TBD; AT F1 fragments across Sst Gaba_3 children.
  evidence: [...]
```

### Cross-cutting (one taxonomy_type, many lit_types)

```yaml
- id: edge_basket_to_mli1
  lit_type: classical_basket
  taxonomy_type: CS20230722_CLUS_5170
  relationship: evidencell:CrossCuttingMatch
  confidence: MODERATE
  evidence: [...]

- id: edge_stellate_to_mli1
  lit_type: classical_stellate
  taxonomy_type: CS20230722_CLUS_5170
  relationship: evidencell:CrossCuttingMatch
  confidence: MODERATE
  evidence: [...]
```

## Phase 2 transition window

The schema retains `type_a` / `type_b` slots and the old ALL_CAPS
`MappingRelationship` values (`EQUIVALENT`, `TYPE_A_SPLITS`, ...) as
deprecated entries so existing KB YAML validates during PR1. The PR2
KB sweep rewrites every edge to the new field names + CURIE values,
and the deprecated entries are then removed from the schema. Until
PR2 lands, reads in `src/evidencell/` go through
`src/evidencell/_mapping_compat.py`, which normalises both shapes.

## Related

- [`planning/phase_2_decisions_2026-05-12.md`](../planning/phase_2_decisions_2026-05-12.md) — Phase 0 decisions.
- [`planning/map_cell_type_redesign_roadmap.md`](../planning/map_cell_type_redesign_roadmap.md) § 4 — roadmap entry.
- Issue [#30](https://github.com/Cellular-Semantics/evidencell/issues/30) — schema discussion.
- Issue [#56](https://github.com/Cellular-Semantics/evidencell/issues/56) — SSSOM exporter follow-up.
- Issue [#57](https://github.com/Cellular-Semantics/evidencell/issues/57) — confidence binning follow-up.
- Issue [#58](https://github.com/Cellular-Semantics/evidencell/issues/58) — TOC glossary follow-up.

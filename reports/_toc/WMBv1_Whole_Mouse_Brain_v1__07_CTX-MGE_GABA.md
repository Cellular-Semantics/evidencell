# WMBv1 (Whole Mouse Brain v1) — mapping contents

Taxonomy ID: `CCN20230722` · Species: Mus musculus
Source: `CCN20230722.json`
Minimum mapping confidence: **MODERATE**

## Glossary

**Direction convention.** Mapping relationships are read from the `lit_type` (subject) to the `taxonomy_type` (object). `skos:broadMatch` and `skos:narrowMatch` describe the *match target*, not the subject — e.g. `skos:broadMatch` means the taxonomy_type is broader than the lit_type.

**Worked example.** `OLM --skos:broadMatch--> Sst Gaba_3 supertype` reads as *"OLM has a broad match — the supertype is the broader thing"*. OLM is one of several types within the supertype; cardinality is `1:n`.

See [`docs/mapping_schema_2026-05-12.md`](../docs/mapping_schema_2026-05-12.md) for worked examples and cardinality interaction.

### Mapping relationship

- **`evidencell:CrossCuttingMatch`** — The taxonomy_type cross-cuts the boundary of the lit_type (and usually at least one other lit_type). The transcriptomic type captures cells that the classical taxonomy would assign to multiple distinct types. E.g. MLI1 cuts across classical basket and stellate cells. Apply only when no higher rank rescues the relationship to a clean broadMatch — if cross-cutting at rank N collapses to a single broader type at rank N+1, prefer broadMatch at N+1. No SKOS equivalent.
- **`evidencell:NoCorrespondence`** — No corresponding type exists in the target taxonomy. Use to explicitly document failures of correspondence (e.g. a curated literature type that the atlas does not resolve at any rank). No SKOS equivalent.
- **`evidencell:PartialOverlapMatch`** — DEPRECATED (2026-05-26). Absorbed into closeMatch (1:1-ish with contradictions) + broadMatch / narrowMatch / CrossCuttingMatch per the new predicate rubric. Retained transitionally so the KB validates against the deprecated value during migration; the re-run will re-predicate the existing 42 edges. Do not emit on new edges. Will be removed after migration.
- **`evidencell:UncertainRelationship`** — The kind of correspondence is not yet determinable from available evidence. Distinct from `evidencell:NoCorrespondence` (which asserts no mapping exists). Pair with `mapping_justification: semapv:UnspecifiedMatching` and a `reconciliation_note` describing what additional evidence would resolve the question. No SKOS equivalent.
- **`skos:broadMatch`** — The lit_type is **narrower** than the taxonomy_type; the match goes *to* the broader thing. Read `lit_OLM --skos:broadMatch--> Sst_Gaba_3_supertype` as "OLM has a broad match — the supertype is the broader thing." Apply when: the taxonomy_type is located in regions distant from the classical region + adjacent set; or the relationship is cross-cutting at rank N but collapses to a clean broader relation at rank N+1 (pick the higher rank); or multiple lit_types map to a single taxonomy_type at this rank. AT must be consistent with the broader reading when present. Always paired with `mapping_cardinality: 1:n` (the hidden-1:1 case collapses: if the specific sub-cluster is TBD, map at the next rank up).
- **`skos:closeMatch`** — Same 1:1-style correspondence as exactMatch but with one or more contradictions: marker mismatch with no resolving heterogeneity in the lit, soft AT (F1 in a borderline band or coverage/purity asymmetry), location edge case, or other partial-information caveat. Pair with mapping_justification: semapv:UnreviewedManualMapping when not curator-confirmed.
- **`skos:exactMatch`** — The lit_type and taxonomy_type describe the same cell population (one-to-one identity). Required: cardinality 1:1; location consistent (classical region + adjacent only, not distant); AT supports 1:1 (F1 > 0.75) when AT is present; no major contradictions. AT-absent cases may still be exactMatch on converging location + markers + literature, but confidence ceiling drops to MODERATE. Numeric AT gate lives in the report-time prompt + rationale, not in this description.
- **`skos:narrowMatch`** — The lit_type is **broader** than the taxonomy_type; the match goes *to* the narrower thing. Read `lit_classical_basket --skos:narrowMatch--> mli2_cluster` as "classical basket has a narrow match — this specific cluster is the narrower thing." Symmetric inverse of broadMatch. Always paired with `mapping_cardinality: n:1`.

### Mapping confidence

- **HIGH** — Strong experimental anchor with no major contradictions. Two standard paths: (a) patch-seq annotation-transfer F1 > 0.75 with marker confirmation; (b) bridging or bulk RNA-seq with strong structure/function convergence at similar strength. Default for a clean exactMatch where AT is present and supportive.
- **MODERATE** — Two or more independent evidence items with consistent support
- **LOW** — Single evidence item or consistent but weak/indirect evidence
- **UNCERTAIN** — Evidence is contradictory, ambiguous, or minimal
- **REFUTED** — Preponderance of evidence argues against this mapping

## Class — 07 CTX-MGE GABA

### Subclass — 050 Lamp5 Lhx6 Gaba

#### Supertype — 0203 Lamp5 Lhx6 Gaba_1

- [ivy_cell_hippocampus](../hippocampus/ivy_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE
- [neurogliaform_cell_hippocampus](../hippocampus/neurogliaform_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

### Subclass — 051 Pvalb chandelier Gaba

#### Supertype — 0204 Pvalb chandelier Gaba_1

- [axo_axonic_cell_hippocampus](../hippocampus/axo_axonic_cell_hippocampus_summary.md) — skos:exactMatch · MODERATE

##### Cluster — 0732 Pvalb chandelier Gaba_1

- [axo_axonic_cell_hippocampus](../hippocampus/axo_axonic_cell_hippocampus_summary.md) — skos:exactMatch · MODERATE
- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

### Subclass — 052 Pvalb Gaba

- [sst_tac1_subfamily_chamberland](../hippocampus/sst_tac1_subfamily_chamberland_summary.md) — skos:closeMatch · MODERATE

#### Supertype — 0206 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE
- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — skos:broadMatch · MODERATE
- [sst_tac1_subfamily_chamberland](../hippocampus/sst_tac1_subfamily_chamberland_summary.md) — skos:closeMatch · MODERATE

##### Cluster — 0737 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

##### Cluster — 0739 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

#### Supertype — 0212 Pvalb Gaba_8

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

### Subclass — 053 Sst Gaba

#### Supertype — 0216 Sst Gaba_3

- [chrna2_olm_subfamily_chamberland](../hippocampus/chrna2_olm_subfamily_chamberland_summary.md) — skos:broadMatch · MODERATE
- [hippocampo_septal_cell_ca1](../hippocampus/hippocampo_septal_cell_ca1_summary.md) — skos:broadMatch · MODERATE
- [olm_cell_ca1](../hippocampus/olm_cell_ca1_summary.md) — skos:broadMatch · MODERATE
- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — skos:broadMatch · MODERATE

##### Cluster — 0768 Sst Gaba_3

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [olm_cell_ca1](../hippocampus/olm_cell_ca1_summary.md) — skos:closeMatch · MODERATE
- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — skos:closeMatch · MODERATE

##### Cluster — 0772 Sst Gaba_3

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

#### Supertype — 0219 Sst Gaba_6

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

# WMBv1 (Whole Mouse Brain v1) — mapping contents

Taxonomy ID: `CCN20230722` · Species: Mus musculus
Source: `CCN20230722.json`
Minimum mapping confidence: **MODERATE**

## Glossary

**Direction convention.** Mapping relationships are read from the `lit_type` (subject) to the `taxonomy_type` (object). `skos:broadMatch` and `skos:narrowMatch` describe the *match target*, not the subject — e.g. `skos:broadMatch` means the taxonomy_type is broader than the lit_type. See [`docs/mapping_schema_2026-05-12.md`](../docs/mapping_schema_2026-05-12.md) for worked examples and cardinality interaction.

### Mapping relationship

- **`evidencell:CrossCuttingMatch`** — The taxonomy_type cross-cuts the boundary of the lit_type (and usually at least one other lit_type). The transcriptomic type captures cells that the classical taxonomy would assign to multiple distinct types. E.g. MLI1 cuts across classical basket and stellate cells. No SKOS equivalent.
- **`evidencell:NoCorrespondence`** — No corresponding type exists in the target taxonomy. Use to explicitly document failures of correspondence (e.g. a curated literature type that the atlas does not resolve at any rank). No SKOS equivalent.
- **`evidencell:PartialOverlapMatch`** — Genuinely incomplete overlap between lit_type and taxonomy_type. Precision OR recall below ~0.65, or partial-set semantics that cannot be expressed as a clean subset / superset relation. No SKOS equivalent — distinguished from skos:closeMatch (which asserts same-type-under-partial- information) by the explicit non-equivalence claim. E.g. Globular (PLI2) → cluster 5177 (precision 83%, recall 93%, also distributed across other clusters).
- **`evidencell:UncertainRelationship`** — The kind of correspondence is not yet determinable from available evidence. Distinct from `evidencell:NoCorrespondence` (which asserts no mapping exists). Pair with `mapping_justification: semapv:UnspecifiedMatching` and a `reconciliation_note` describing what additional evidence would resolve the question. No SKOS equivalent.
- **`skos:broadMatch`** — The lit_type is **narrower** than the taxonomy_type; the match goes *to* the broader thing. Read `lit_OLM --skos:broadMatch--> Sst_Gaba_3_supertype` as "OLM has a broad match — the supertype is the broader thing." Pair with `mapping_cardinality: 1:1` when a specific cluster is suspected to equal the lit_type but cannot yet be identified (hidden 1:1); with `1:n` when the lit_type genuinely subsumes multiple taxonomy_types within the broader node (split case).
- **`skos:closeMatch`** — The lit_type and taxonomy_type are judged to describe the same cell population under partial information (typically F1 ~0.65–0.8, or non-AT evidence that converges but does not yet rise to exactMatch). Conservative default for candidate- synonym-style cases per #30 amendment 1 — pair with mapping_justification: semapv:UnreviewedManualMapping when the evidence has not been curator-confirmed.
- **`skos:exactMatch`** — The lit_type and taxonomy_type describe the same cell population (one-to-one identity). Clean 1:1 correspondence backed by convergent multi-source evidence (e.g. F1 >= 0.8 AT + matching markers + matching anatomy). E.g. Lugaro → WMBv1 supertype 1145 (F1=0.96).
- **`skos:narrowMatch`** — The lit_type is **broader** than the taxonomy_type; the match goes *to* the narrower thing. Read `lit_classical_basket --skos:narrowMatch--> mli2_cluster` as "classical basket has a narrow match — this specific cluster is the narrower thing." Pair with `mapping_cardinality: n:1` for merge cases where multiple lit_types collapse onto one taxonomy_type.

### Mapping confidence

- **HIGH** — Multiple independent convergent evidence types; at least one experimental
- **MODERATE** — Two or more independent evidence items with consistent support
- **LOW** — Single evidence item or consistent but weak/indirect evidence
- **UNCERTAIN** — Evidence is contradictory, ambiguous, or minimal
- **REFUTED** — Preponderance of evidence argues against this mapping

## Class — 07 CTX-MGE GABA

### Subclass — 050 Lamp5 Lhx6 Gaba

#### Supertype — 0203 Lamp5 Lhx6 Gaba_1

- [ivy_cell_hippocampus](../hippocampus/ivy_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE
- [neurogliaform_cell_hippocampus](../hippocampus/neurogliaform_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

### Subclass — 051 Pvalb chandelier Gaba

#### Supertype — 0204 Pvalb chandelier Gaba_1

- [axo_axonic_cell_hippocampus](../hippocampus/axo_axonic_cell_hippocampus_summary.md) — skos:exactMatch · verdict pending

##### Cluster — 0732 Pvalb chandelier Gaba_1

- [axo_axonic_cell_hippocampus](../hippocampus/axo_axonic_cell_hippocampus_summary.md) — skos:exactMatch · verdict pending

### Subclass — 052 Pvalb Gaba

- sst_tac1_subfamily_chamberland — evidencell:PartialOverlapMatch · verdict pending _(no report file)_

#### Supertype — 0206 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE
- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE
- [trilaminar_cell_hippocampus](../hippocampus/trilaminar_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

##### Cluster — 0737 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE

##### Cluster — 0739 Pvalb Gaba_2

- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE

### Subclass — 053 Sst Gaba

#### Supertype — 0216 Sst Gaba_3

- [hippocampo_septal_cell_ca1](../hippocampus/hippocampo_septal_cell_ca1_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- ndnf_nkx2_1_olm_subfamily_chamberland — evidencell:UncertainRelationship · verdict pending _(no report file)_
- [olm_cell_ca1](../hippocampus/olm_cell_ca1_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- [r_lm_cell_hippocampus](../hippocampus/r_lm_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

##### Cluster — 0769 Sst Gaba_3

- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — skos:broadMatch · MODERATE

##### Cluster — 0771 Sst Gaba_3

- chrna2_olm_subfamily_chamberland — evidencell:PartialOverlapMatch · verdict pending _(no report file)_

#### Supertype — 0219 Sst Gaba_6

- [lth_cell_hippocampus](../hippocampus/lth_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [oriens_oriens_cell_hippocampus](../hippocampus/oriens_oriens_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [p_lm_cell_hippocampus](../hippocampus/p_lm_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

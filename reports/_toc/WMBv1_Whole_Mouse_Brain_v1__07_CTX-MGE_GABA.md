# WMBv1 (Whole Mouse Brain v1) — mapping contents

Taxonomy ID: `CCN20230722` · Species: Mus musculus
Source: `CCN20230722.json`
Minimum mapping confidence: **MODERATE**

## Glossary

### Mapping relationship

- **PARTIAL_OVERLAP** — Some cells from type_a map to type_b, but the mapping is incomplete in precision, recall, or both. E.g. Globular (PLI2) → cluster 5177 (precision 83%, recall 93%: high precision, limited recall — also distributed across other clusters).
- **TYPE_A_SPLITS** — type_a (typically classical) corresponds to multiple type_b nodes. Use one edge per split, all with TYPE_A_SPLITS relationship. E.g. one classical interneuron type splits into MLI1 + MLI2 in transcriptomics.

### Mapping confidence

- **MODERATE** — Two or more independent evidence items with consistent support

## Class — 07 CTX-MGE GABA

### Subclass — 050 Lamp5 Lhx6 Gaba

#### Supertype — 0203 Lamp5 Lhx6 Gaba_1

- ivy_cell_hippocampus — PARTIAL_OVERLAP · MODERATE _(no report file)_

### Subclass — 052 Pvalb Gaba

#### Supertype — 0206 Pvalb Gaba_2

- pv_basket_cell_hippocampus — PARTIAL_OVERLAP · MODERATE _(no report file)_

##### Cluster — 0739 Pvalb Gaba_2

- pv_basket_cell_hippocampus — PARTIAL_OVERLAP · MODERATE _(no report file)_

### Subclass — 053 Sst Gaba

#### Supertype — 0216 Sst Gaba_3

- olm_cell_ca1 — PARTIAL_OVERLAP · MODERATE _(no report file)_

##### Cluster — 0769 Sst Gaba_3

- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — TYPE_A_SPLITS · MODERATE

# Taxonomy-indexed mapping reports

Minimum mapping confidence: **MODERATE**

## Glossary

### Mapping relationship

- **CROSS_CUTTING** — type_b cross-cuts the boundary of type_a (and usually at least one other node). The transcriptomic type captures cells that the classical taxonomy would assign to multiple distinct types. E.g. MLI1 cuts across classical basket and stellate cells.
- **PARTIAL_OVERLAP** — Some cells from type_a map to type_b, but the mapping is incomplete in precision, recall, or both. E.g. Globular (PLI2) → cluster 5177 (precision 83%, recall 93%: high precision, limited recall — also distributed across other clusters).
- **TYPE_A_SPLITS** — type_a (typically classical) corresponds to multiple type_b nodes. Use one edge per split, all with TYPE_A_SPLITS relationship. E.g. one classical interneuron type splits into MLI1 + MLI2 in transcriptomics.

### Mapping confidence

- **MODERATE** — Two or more independent evidence items with consistent support

## WMBv1 (Whole Mouse Brain v1)

`CCN20230722` · Mus musculus

### Class — 06 CTX-CGE GABA

#### Subclass — 046 Vip Gaba

##### Supertype — 0179 Vip Gaba_7

- is_interneuron_hippocampus — PARTIAL_OVERLAP · MODERATE _(no report file)_

#### Subclass — 048 RHP-COA Ndnf Gaba

##### Supertype — 0193 RHP-COA Ndnf Gaba_1

- neurogliaform_cell_hippocampus — PARTIAL_OVERLAP · MODERATE _(no report file)_

### Class — 07 CTX-MGE GABA

#### Subclass — 050 Lamp5 Lhx6 Gaba

##### Supertype — 0203 Lamp5 Lhx6 Gaba_1

- ivy_cell_hippocampus — PARTIAL_OVERLAP · MODERATE _(no report file)_

#### Subclass — 052 Pvalb Gaba

##### Supertype — 0206 Pvalb Gaba_2

- pv_basket_cell_hippocampus — PARTIAL_OVERLAP · MODERATE _(no report file)_

###### Cluster — 0739 Pvalb Gaba_2

- pv_basket_cell_hippocampus — PARTIAL_OVERLAP · MODERATE _(no report file)_

#### Subclass — 053 Sst Gaba

##### Supertype — 0216 Sst Gaba_3

- olm_cell_ca1 — PARTIAL_OVERLAP · MODERATE _(no report file)_

###### Cluster — 0769 Sst Gaba_3

- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — TYPE_A_SPLITS · MODERATE

### Class — 12 HY GABA

#### Subclass — 106 PVpo-VMPO-MPN Hmx2 Gaba

##### Supertype — 0486 PVpo-VMPO-MPN Hmx2 Gaba_5

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE
- [avpv_th_neuron](../sexually_dimorphic/avpv_th_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE
- [mpoa_esr1_neuron](../sexually_dimorphic/mpoa_esr1_neuron_summary.md) — CROSS_CUTTING · MODERATE

###### Cluster — 1915 PVpo-VMPO-MPN Hmx2 Gaba_5

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE
- [avpv_th_neuron](../sexually_dimorphic/avpv_th_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE

### Class — 13 CNU-HYa Glut

#### Subclass — 116 AVPV-MEPO-SFO Tbr1 Glut

##### Supertype — 0521 AVPV-MEPO-SFO Tbr1 Glut_3

- [mpoa_esr1_neuron](../sexually_dimorphic/mpoa_esr1_neuron_summary.md) — CROSS_CUTTING · MODERATE

### Class — 14 HY Glut

#### Subclass — 128 VMH Fezf1 Glut

##### Supertype — 0563 VMH Fezf1 Glut_1

- [vmhvl_esr1_pr_neuron](../sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md) — CROSS_CUTTING · MODERATE

##### Supertype — 0564 VMH Fezf1 Glut_2

- [vmhvl_esr1_pr_neuron](../sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md) — CROSS_CUTTING · MODERATE

#### Subclass — 133 PVH-SO-PVa Otp Glut

##### Supertype — 0585 PVH-SO-PVa Otp Glut_1

- [pvn_crfr1_neuron](../sexually_dimorphic/pvn_crfr1_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE

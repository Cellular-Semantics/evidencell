# WMBv1 (Whole Mouse Brain v1) — mapping contents

Taxonomy ID: `CCN20230722` · Species: Mus musculus
Source: `CCN20230722.json`
Minimum mapping confidence: **MODERATE**

## Glossary

### Mapping relationship

- **CROSS_CUTTING** — type_b cross-cuts the boundary of type_a (and usually at least one other node). The transcriptomic type captures cells that the classical taxonomy would assign to multiple distinct types. E.g. MLI1 cuts across classical basket and stellate cells.
- **EQUIVALENT** — type_a and type_b describe the same cell population. Clean 1:1 correspondence. E.g. Lugaro → WMBv1 supertype 1145 (F1=0.96).
- **PARTIAL_OVERLAP** — Some cells from type_a map to type_b, but the mapping is incomplete in precision, recall, or both. E.g. Globular (PLI2) → cluster 5177 (precision 83%, recall 93%: high precision, limited recall — also distributed across other clusters).
- **TYPE_A_SPLITS** — type_a (typically classical) corresponds to multiple type_b nodes. Use one edge per split, all with TYPE_A_SPLITS relationship. E.g. one classical interneuron type splits into MLI1 + MLI2 in transcriptomics.

### Mapping confidence

- **HIGH** — Multiple independent convergent evidence types; at least one experimental
- **MODERATE** — Two or more independent evidence items with consistent support

## Class — 01 IT-ET Glut

### Subclass — 008 L2/3 IT ENT Glut

#### Supertype — 0036 L2/3 IT ENT Glut_4

- [ec_layer3_pyramidal_cell_hippocampus](../hippocampus/ec_layer3_pyramidal_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

### Subclass — 009 L2/3 IT PIR-ENTl Glut

#### Supertype — 0042 L2/3 IT PIR-ENTl Glut_4

- [ec_layer2_stellate_cell_hippocampus](../hippocampus/ec_layer2_stellate_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

### Subclass — 011 L2 IT ENT-po Glut

#### Supertype — 0052 L2 IT ENT-po Glut_2

- [ec_layer2_pyramidal_cell_hippocampus](../hippocampus/ec_layer2_pyramidal_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

### Subclass — 016 CA1-ProS Glut

#### Supertype — 0069 CA1-ProS Glut_1

- [ca1_pc_hippocampus](../hippocampus/ca1_pc_hippocampus_summary.md) — TYPE_A_SPLITS · MODERATE

### Subclass — 017 CA3 Glut

#### Supertype — 0078 CA3 Glut_4

- [ca3_pc_hippocampus](../hippocampus/ca3_pc_hippocampus_summary.md) — TYPE_A_SPLITS · MODERATE
- [hilar_mossy_cell_hippocampus](../hippocampus/hilar_mossy_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

#### Supertype — 0079 CA3 Glut_5

- [hilar_mossy_cell_hippocampus](../hippocampus/hilar_mossy_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

### Subclass — 023 SUB-ProS Glut

#### Supertype — 0096 SUB-ProS Glut_1

- [subicular_pyramidal_cell_hippocampus](../hippocampus/subicular_pyramidal_cell_hippocampus_summary.md) — TYPE_A_SPLITS · MODERATE

### Subclass — 025 CA2-FC-IG Glut

#### Supertype — 0100 CA2-FC-IG Glut_1

- [ca2_pc_hippocampus](../hippocampus/ca2_pc_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

## Class — 04 DG-IMN Glut

### Subclass — 037 DG Glut

#### Supertype — 0137 DG Glut_2

- [dg_granule_cell_hippocampus](../hippocampus/dg_granule_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

##### Cluster — 0506 DG Glut_2

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — TYPE_A_SPLITS · MODERATE

#### Supertype — 0138 DG Glut_3

- [dg_semilunar_granule_cell_hippocampus](../hippocampus/dg_semilunar_granule_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

### Subclass — 038 DG-PIR Ex IMN

#### Supertype — 0140 DG-PIR Ex IMN_1

##### Cluster — 0511 DG-PIR Ex IMN_1

- [dg_type2b_progenitor](../dentate_gyrus/dg_type2b_progenitor_summary.md) — PARTIAL_OVERLAP · MODERATE

## Class — 06 CTX-CGE GABA

### Subclass — 046 Vip Gaba

#### Supertype — 0179 Vip Gaba_7

- [is_interneuron_hippocampus](../hippocampus/is_interneuron_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

### Subclass — 048 RHP-COA Ndnf Gaba

#### Supertype — 0193 RHP-COA Ndnf Gaba_1

- [neurogliaform_cell_hippocampus](../hippocampus/neurogliaform_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

## Class — 07 CTX-MGE GABA

### Subclass — 050 Lamp5 Lhx6 Gaba

#### Supertype — 0203 Lamp5 Lhx6 Gaba_1

- [ivy_cell_hippocampus](../hippocampus/ivy_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

### Subclass — 052 Pvalb Gaba

- sst_tac1_subfamily_chamberland — PARTIAL_OVERLAP · MODERATE _(no report file)_

#### Supertype — 0206 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE
- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · HIGH

##### Cluster — 0737 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · MODERATE

##### Cluster — 0739 Pvalb Gaba_2

- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — PARTIAL_OVERLAP · HIGH

### Subclass — 053 Sst Gaba

#### Supertype — 0216 Sst Gaba_3

- [olm_cell_ca1](../hippocampus/olm_cell_ca1_summary.md) — PARTIAL_OVERLAP · MODERATE

##### Cluster — 0769 Sst Gaba_3

- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — TYPE_A_SPLITS · MODERATE

##### Cluster — 0771 Sst Gaba_3

- chrna2_olm_subfamily_chamberland — PARTIAL_OVERLAP · MODERATE _(no report file)_

## Class — 08 CNU-MGE GABA

### Subclass — 056 Sst Chodl Gaba

#### Supertype — 0241 Sst Chodl Gaba_4

##### Cluster — 0859 Sst Chodl Gaba_4

- sst_nos1_subfamily_chamberland — EQUIVALENT · HIGH _(no report file)_

## Class — 12 HY GABA

### Subclass — 106 PVpo-VMPO-MPN Hmx2 Gaba

#### Supertype — 0486 PVpo-VMPO-MPN Hmx2 Gaba_5

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE
- [avpv_th_neuron](../sexually_dimorphic/avpv_th_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE
- [mpoa_esr1_neuron](../sexually_dimorphic/mpoa_esr1_neuron_summary.md) — CROSS_CUTTING · MODERATE

##### Cluster — 1915 PVpo-VMPO-MPN Hmx2 Gaba_5

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE
- [avpv_th_neuron](../sexually_dimorphic/avpv_th_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE

## Class — 13 CNU-HYa Glut

### Subclass — 116 AVPV-MEPO-SFO Tbr1 Glut

#### Supertype — 0521 AVPV-MEPO-SFO Tbr1 Glut_3

- [mpoa_esr1_neuron](../sexually_dimorphic/mpoa_esr1_neuron_summary.md) — CROSS_CUTTING · MODERATE

## Class — 14 HY Glut

### Subclass — 128 VMH Fezf1 Glut

#### Supertype — 0563 VMH Fezf1 Glut_1

- [vmhvl_esr1_pr_neuron](../sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md) — CROSS_CUTTING · MODERATE

#### Supertype — 0564 VMH Fezf1 Glut_2

- [vmhvl_esr1_pr_neuron](../sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md) — CROSS_CUTTING · MODERATE

### Subclass — 133 PVH-SO-PVa Otp Glut

#### Supertype — 0585 PVH-SO-PVa Otp Glut_1

- [pvn_crfr1_neuron](../sexually_dimorphic/pvn_crfr1_neuron_summary.md) — PARTIAL_OVERLAP · MODERATE

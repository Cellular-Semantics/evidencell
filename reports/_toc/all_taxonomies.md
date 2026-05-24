# Taxonomy-indexed mapping reports

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

## WMBv1 (Whole Mouse Brain v1)

`CCN20230722` · Mus musculus

### Class — 01 IT-ET Glut

#### Subclass — 008 L2/3 IT ENT Glut

##### Supertype — 0036 L2/3 IT ENT Glut_4

- [ec_layer3_pyramidal_cell_hippocampus](../hippocampus/ec_layer3_pyramidal_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

##### Supertype — 0037 L2/3 IT ENT Glut_5

- [ec_layer3_pyramidal_cell_hippocampus](../hippocampus/ec_layer3_pyramidal_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 009 L2/3 IT PIR-ENTl Glut

##### Supertype — 0042 L2/3 IT PIR-ENTl Glut_4

- [ec_layer2_stellate_cell_hippocampus](../hippocampus/ec_layer2_stellate_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 011 L2 IT ENT-po Glut

##### Supertype — 0052 L2 IT ENT-po Glut_2

- [ec_layer2_pyramidal_cell_hippocampus](../hippocampus/ec_layer2_pyramidal_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 012 MEA Slc17a7 Glut

##### Supertype — 0055 MEA Slc17a7 Glut_1

- [mea_esr1_neuron](../sexually_dimorphic/mea_esr1_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 016 CA1-ProS Glut

##### Supertype — 0069 CA1-ProS Glut_1

- [ca1_pc_hippocampus](../hippocampus/ca1_pc_hippocampus_summary.md) — skos:broadMatch · MODERATE
- [hpc_glu_dopa_receptor_pyramidal_hippocampus](../hippocampus/hpc_glu_dopa_receptor_pyramidal_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 017 CA3 Glut

##### Supertype — 0078 CA3 Glut_4

- [ca3_pc_hippocampus](../hippocampus/ca3_pc_hippocampus_summary.md) — skos:broadMatch · verdict pending
- [hilar_mossy_cell_hippocampus](../hippocampus/hilar_mossy_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

##### Supertype — 0079 CA3 Glut_5

- [hilar_mossy_cell_hippocampus](../hippocampus/hilar_mossy_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 023 SUB-ProS Glut

##### Supertype — 0096 SUB-ProS Glut_1

- [subicular_pyramidal_cell_hippocampus](../hippocampus/subicular_pyramidal_cell_hippocampus_summary.md) — skos:broadMatch · verdict pending

#### Subclass — 025 CA2-FC-IG Glut

##### Supertype — 0100 CA2-FC-IG Glut_1

- [ca2_pc_hippocampus](../hippocampus/ca2_pc_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

### Class — 03 OB-CR Glut

#### Subclass — 036 HPF CR Glut

##### Supertype — 0135 HPF CR Glut_1

- [hpc_calretinin_glu_neuron_hippocampus](../hippocampus/hpc_calretinin_glu_neuron_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

### Class — 04 DG-IMN Glut

#### Subclass — 037 DG Glut

##### Supertype — 0136 DG Glut_1

###### Cluster — 0502 DG Glut_1

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0503 DG Glut_1

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0504 DG Glut_1

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

##### Supertype — 0137 DG Glut_2

- [dg_granule_cell_hippocampus](../hippocampus/dg_granule_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- [dg_semilunar_granule_cell_hippocampus](../hippocampus/dg_semilunar_granule_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

###### Cluster — 0505 DG Glut_2

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0506 DG Glut_2

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0507 DG Glut_2

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

##### Supertype — 0138 DG Glut_3

- [dg_semilunar_granule_cell_hippocampus](../hippocampus/dg_semilunar_granule_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

###### Cluster — 0508 DG Glut_3

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0509 DG Glut_3

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

##### Supertype — 0139 DG Glut_4

###### Cluster — 0510 DG Glut_4

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

#### Subclass — 038 DG-PIR Ex IMN

##### Supertype — 0140 DG-PIR Ex IMN_1

###### Cluster — 0511 DG-PIR Ex IMN_1

- [dg_neuroblast](../dentate_gyrus/dg_neuroblast_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- [dg_type2b_progenitor](../dentate_gyrus/dg_type2b_progenitor_summary.md) — evidencell:PartialOverlapMatch · verdict pending

##### Supertype — 0141 DG-PIR Ex IMN_2

###### Cluster — 0514 DG-PIR Ex IMN_2

- [dg_immature_granule_neuron](../dentate_gyrus/dg_immature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0515 DG-PIR Ex IMN_2

- [dg_immature_granule_neuron](../dentate_gyrus/dg_immature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

### Class — 06 CTX-CGE GABA

#### Subclass — 046 Vip Gaba

##### Supertype — 0179 Vip Gaba_7

- [cck_basket_cell_hippocampus](../hippocampus/cck_basket_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [is_interneuron_hippocampus](../hippocampus/is_interneuron_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- [vip_basket_cell_hippocampus](../hippocampus/vip_basket_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

#### Subclass — 047 Sncg Gaba

##### Supertype — 0187 Sncg Gaba_3

- [cck_basket_cell_hippocampus](../hippocampus/cck_basket_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 048 RHP-COA Ndnf Gaba

##### Supertype — 0193 RHP-COA Ndnf Gaba_1

- [neurogliaform_cell_hippocampus](../hippocampus/neurogliaform_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

### Class — 07 CTX-MGE GABA

#### Subclass — 050 Lamp5 Lhx6 Gaba

##### Supertype — 0203 Lamp5 Lhx6 Gaba_1

- [ivy_cell_hippocampus](../hippocampus/ivy_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE
- [neurogliaform_cell_hippocampus](../hippocampus/neurogliaform_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 051 Pvalb chandelier Gaba

##### Supertype — 0204 Pvalb chandelier Gaba_1

- [axo_axonic_cell_hippocampus](../hippocampus/axo_axonic_cell_hippocampus_summary.md) — skos:exactMatch · verdict pending

###### Cluster — 0732 Pvalb chandelier Gaba_1

- [axo_axonic_cell_hippocampus](../hippocampus/axo_axonic_cell_hippocampus_summary.md) — skos:exactMatch · verdict pending

#### Subclass — 052 Pvalb Gaba

- sst_tac1_subfamily_chamberland — evidencell:PartialOverlapMatch · verdict pending _(no report file)_

##### Supertype — 0206 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE
- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE
- [trilaminar_cell_hippocampus](../hippocampus/trilaminar_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · verdict pending

###### Cluster — 0737 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE

###### Cluster — 0739 Pvalb Gaba_2

- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — evidencell:PartialOverlapMatch · MODERATE

#### Subclass — 053 Sst Gaba

##### Supertype — 0216 Sst Gaba_3

- [hippocampo_septal_cell_ca1](../hippocampus/hippocampo_septal_cell_ca1_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- ndnf_nkx2_1_olm_subfamily_chamberland — evidencell:UncertainRelationship · verdict pending _(no report file)_
- [olm_cell_ca1](../hippocampus/olm_cell_ca1_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- [r_lm_cell_hippocampus](../hippocampus/r_lm_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

###### Cluster — 0769 Sst Gaba_3

- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — skos:broadMatch · MODERATE

###### Cluster — 0771 Sst Gaba_3

- chrna2_olm_subfamily_chamberland — evidencell:PartialOverlapMatch · verdict pending _(no report file)_

##### Supertype — 0219 Sst Gaba_6

- [lth_cell_hippocampus](../hippocampus/lth_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [oriens_oriens_cell_hippocampus](../hippocampus/oriens_oriens_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [p_lm_cell_hippocampus](../hippocampus/p_lm_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

### Class — 08 CNU-MGE GABA

#### Subclass — 056 Sst Chodl Gaba

##### Supertype — 0241 Sst Chodl Gaba_4

###### Cluster — 0859 Sst Chodl Gaba_4

- sst_nos1_subfamily_chamberland — skos:exactMatch · verdict pending _(no report file)_

### Class — 11 CNU-HYa GABA

#### Subclass — 076 MEA-BST Lhx6 Nfib Gaba

##### Supertype — 0358 MEA-BST Lhx6 Nfib Gaba_2

- [bnst_crf_neuron](../sexually_dimorphic/bnst_crf_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 083 CEA-BST Rai14 Pdyn Crh Gaba

##### Supertype — 0393 CEA-BST Rai14 Pdyn Crh Gaba_2

- [bnst_crf_neuron](../sexually_dimorphic/bnst_crf_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 090 BST-MPN Six3 Nrgn Gaba

##### Supertype — 0423 BST-MPN Six3 Nrgn Gaba_4

- [sdn_poa_calbindin_neuron](../sexually_dimorphic/sdn_poa_calbindin_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

###### Cluster — 1550 BST-MPN Six3 Nrgn Gaba_4

- [sdn_poa_calbindin_neuron](../sexually_dimorphic/sdn_poa_calbindin_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending

### Class — 12 HY GABA

#### Subclass — 106 PVpo-VMPO-MPN Hmx2 Gaba

##### Supertype — 0486 PVpo-VMPO-MPN Hmx2 Gaba_5

- [arc_aromatase_neuron](../sexually_dimorphic/arc_aromatase_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending
- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- [avpv_th_neuron](../sexually_dimorphic/avpv_th_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- [mpoa_esr1_neuron](../sexually_dimorphic/mpoa_esr1_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

###### Cluster — 1915 PVpo-VMPO-MPN Hmx2 Gaba_5

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending
- [avpv_th_neuron](../sexually_dimorphic/avpv_th_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending

### Class — 13 CNU-HYa Glut

#### Subclass — 116 AVPV-MEPO-SFO Tbr1 Glut

##### Supertype — 0521 AVPV-MEPO-SFO Tbr1 Glut_3

- [mpoa_esr1_neuron](../sexually_dimorphic/mpoa_esr1_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

### Class — 14 HY Glut

#### Subclass — 128 VMH Fezf1 Glut

##### Supertype — 0563 VMH Fezf1 Glut_1

- [vmhvl_esr1_pr_neuron](../sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

##### Supertype — 0564 VMH Fezf1 Glut_2

- [vmhvl_esr1_pr_neuron](../sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

#### Subclass — 133 PVH-SO-PVa Otp Glut

##### Supertype — 0585 PVH-SO-PVa Otp Glut_1

- [pvn_crfr1_neuron](../sexually_dimorphic/pvn_crfr1_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending

#### Subclass — 136 PMv-TMv Pitx2 Glut

##### Supertype — 0607 PMv-TMv Pitx2 Glut_3

- [pmv_otr_neuron](../sexually_dimorphic/pmv_otr_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

###### Cluster — 2470 PMv-TMv Pitx2 Glut_3

- [pmv_otr_neuron](../sexually_dimorphic/pmv_otr_neuron_summary.md) — evidencell:PartialOverlapMatch · verdict pending

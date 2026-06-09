# Taxonomy-indexed mapping reports

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

## WMBv1 (Whole Mouse Brain v1)

`CCN20230722` · Mus musculus

### Class — 01 IT-ET Glut

#### Subclass — 008 L2/3 IT ENT Glut

##### Supertype — 0036 L2/3 IT ENT Glut_4

- [ec_layer3_pyramidal_cell_hippocampus](../hippocampus/ec_layer3_pyramidal_cell_hippocampus_summary.md) — skos:closeMatch · HIGH

##### Supertype — 0037 L2/3 IT ENT Glut_5

- [ec_layer3_pyramidal_cell_hippocampus](../hippocampus/ec_layer3_pyramidal_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

#### Subclass — 009 L2/3 IT PIR-ENTl Glut

##### Supertype — 0042 L2/3 IT PIR-ENTl Glut_4

- [ec_layer2_stellate_cell_hippocampus](../hippocampus/ec_layer2_stellate_cell_hippocampus_summary.md) — skos:broadMatch · MODERATE

###### Cluster — 0155 L2/3 IT PIR-ENTl Glut_4

- [ec_layer2_stellate_cell_hippocampus](../hippocampus/ec_layer2_stellate_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

#### Subclass — 011 L2 IT ENT-po Glut

##### Supertype — 0052 L2 IT ENT-po Glut_2

- [ec_layer2_pyramidal_cell_hippocampus](../hippocampus/ec_layer2_pyramidal_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

##### Supertype — 0054 L2 IT ENT-po Glut_4

- [ec_layer2_pyramidal_cell_hippocampus](../hippocampus/ec_layer2_pyramidal_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

#### Subclass — 012 MEA Slc17a7 Glut

##### Supertype — 0055 MEA Slc17a7 Glut_1

- [mea_esr1_neuron](../sexually_dimorphic/mea_esr1_neuron_summary.md) — skos:closeMatch · verdict pending

#### Subclass — 016 CA1-ProS Glut

##### Supertype — 0069 CA1-ProS Glut_1

###### Cluster — 0262 CA1-ProS Glut_1

- [ca1_pc_hippocampus](../hippocampus/ca1_pc_hippocampus_summary.md) — skos:closeMatch · MODERATE

#### Subclass — 017 CA3 Glut

##### Supertype — 0078 CA3 Glut_4

- [hilar_mossy_cell_hippocampus](../hippocampus/hilar_mossy_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

##### Supertype — 0079 CA3 Glut_5

###### Cluster — 0317 CA3 Glut_5

- [hilar_mossy_cell_hippocampus](../hippocampus/hilar_mossy_cell_hippocampus_summary.md) — skos:closeMatch · HIGH

#### Subclass — 025 CA2-FC-IG Glut

##### Supertype — 0100 CA2-FC-IG Glut_1

###### Cluster — 0399 CA2-FC-IG Glut_1

- [ca2_pc_hippocampus](../hippocampus/ca2_pc_hippocampus_summary.md) — skos:closeMatch · MODERATE

### Class — 02 NP-CT-L6b Glut

#### Subclass — 031 CT SUB Glut

##### Supertype — 0121 CT SUB Glut_2

- [subicular_pyramidal_cell_hippocampus](../hippocampus/subicular_pyramidal_cell_hippocampus_summary.md) — skos:broadMatch · MODERATE

#### Subclass — 033 NP SUB Glut

##### Supertype — 0128 NP SUB Glut_2

- [subicular_pyramidal_cell_hippocampus](../hippocampus/subicular_pyramidal_cell_hippocampus_summary.md) — skos:broadMatch · MODERATE

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

###### Cluster — 0505 DG Glut_2

- [dg_granule_cell_hippocampus](../hippocampus/dg_granule_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE
- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0506 DG Glut_2

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0507 DG Glut_2

- [dg_mature_granule_neuron](../dentate_gyrus/dg_mature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

##### Supertype — 0138 DG Glut_3

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

- [dg_neuroblast](../dentate_gyrus/dg_neuroblast_summary.md) — skos:closeMatch · verdict pending
- [dg_type2b_progenitor](../dentate_gyrus/dg_type2b_progenitor_summary.md) — skos:closeMatch · verdict pending

##### Supertype — 0141 DG-PIR Ex IMN_2

###### Cluster — 0514 DG-PIR Ex IMN_2

- [dg_immature_granule_neuron](../dentate_gyrus/dg_immature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

###### Cluster — 0515 DG-PIR Ex IMN_2

- [dg_immature_granule_neuron](../dentate_gyrus/dg_immature_granule_neuron_summary.md) — skos:broadMatch · verdict pending

### Class — 06 CTX-CGE GABA

#### Subclass — 046 Vip Gaba

##### Supertype — 0179 Vip Gaba_7

- [is_interneuron_hippocampus](../hippocampus/is_interneuron_hippocampus_summary.md) — skos:broadMatch · MODERATE

#### Subclass — 047 Sncg Gaba

##### Supertype — 0187 Sncg Gaba_3

- [cck_basket_cell_hippocampus](../hippocampus/cck_basket_cell_hippocampus_summary.md) — skos:broadMatch · MODERATE

##### Supertype — 0189 Sncg Gaba_5

###### Cluster — 0681 Sncg Gaba_5

- [cck_basket_cell_hippocampus](../hippocampus/cck_basket_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

#### Subclass — 048 RHP-COA Ndnf Gaba

##### Supertype — 0196 RHP-COA Ndnf Gaba_4

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

### Class — 07 CTX-MGE GABA

#### Subclass — 050 Lamp5 Lhx6 Gaba

##### Supertype — 0203 Lamp5 Lhx6 Gaba_1

- [ivy_cell_hippocampus](../hippocampus/ivy_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE
- [neurogliaform_cell_hippocampus](../hippocampus/neurogliaform_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

#### Subclass — 051 Pvalb chandelier Gaba

##### Supertype — 0204 Pvalb chandelier Gaba_1

- [axo_axonic_cell_hippocampus](../hippocampus/axo_axonic_cell_hippocampus_summary.md) — skos:exactMatch · MODERATE

###### Cluster — 0732 Pvalb chandelier Gaba_1

- [axo_axonic_cell_hippocampus](../hippocampus/axo_axonic_cell_hippocampus_summary.md) — skos:exactMatch · MODERATE
- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

#### Subclass — 052 Pvalb Gaba

- [sst_tac1_subfamily_chamberland](../hippocampus/sst_tac1_subfamily_chamberland_summary.md) — skos:closeMatch · MODERATE

##### Supertype — 0206 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE
- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — skos:broadMatch · MODERATE
- [sst_tac1_subfamily_chamberland](../hippocampus/sst_tac1_subfamily_chamberland_summary.md) — skos:closeMatch · MODERATE

###### Cluster — 0737 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

###### Cluster — 0739 Pvalb Gaba_2

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [pv_basket_cell_hippocampus](../hippocampus/pv_basket_cell_hippocampus_summary.md) — skos:closeMatch · MODERATE

##### Supertype — 0212 Pvalb Gaba_8

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

#### Subclass — 053 Sst Gaba

##### Supertype — 0216 Sst Gaba_3

- [chrna2_olm_subfamily_chamberland](../hippocampus/chrna2_olm_subfamily_chamberland_summary.md) — skos:broadMatch · MODERATE
- [hippocampo_septal_cell_ca1](../hippocampus/hippocampo_septal_cell_ca1_summary.md) — skos:broadMatch · MODERATE
- [olm_cell_ca1](../hippocampus/olm_cell_ca1_summary.md) — skos:broadMatch · MODERATE
- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — skos:broadMatch · MODERATE

###### Cluster — 0768 Sst Gaba_3

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending
- [olm_cell_ca1](../hippocampus/olm_cell_ca1_summary.md) — skos:closeMatch · MODERATE
- [olm_hippocampus](../hippocampus/olm_hippocampus_summary.md) — skos:closeMatch · MODERATE

###### Cluster — 0772 Sst Gaba_3

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

##### Supertype — 0219 Sst Gaba_6

- [bistratified_cell_hippocampus](../hippocampus/bistratified_cell_hippocampus_summary.md) — evidencell:UncertainRelationship · verdict pending

### Class — 08 CNU-MGE GABA

#### Subclass — 056 Sst Chodl Gaba

##### Supertype — 0241 Sst Chodl Gaba_4

- [sst_nos1_subfamily_chamberland](../hippocampus/sst_nos1_subfamily_chamberland_summary.md) — skos:broadMatch · HIGH

###### Cluster — 0859 Sst Chodl Gaba_4

- [sst_nos1_subfamily_chamberland](../hippocampus/sst_nos1_subfamily_chamberland_summary.md) — skos:closeMatch · HIGH

#### Subclass — 057 NDB-SI-MA-STRv Lhx8 Gaba

##### Supertype — 0249 NDB-SI-MA-STRv Lhx8 Gaba_6

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

### Class — 11 CNU-HYa GABA

#### Subclass — 076 MEA-BST Lhx6 Nfib Gaba

##### Supertype — 0358 MEA-BST Lhx6 Nfib Gaba_2

- [bnst_crf_neuron](../sexually_dimorphic/bnst_crf_neuron_summary.md) — skos:closeMatch · verdict pending

##### Supertype — 0360 MEA-BST Lhx6 Nfib Gaba_4

###### Cluster — 1301 MEA-BST Lhx6 Nfib Gaba_4

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

#### Subclass — 083 CEA-BST Rai14 Pdyn Crh Gaba

##### Supertype — 0393 CEA-BST Rai14 Pdyn Crh Gaba_2

- [bnst_crf_neuron](../sexually_dimorphic/bnst_crf_neuron_summary.md) — skos:closeMatch · verdict pending

#### Subclass — 089 PVR Six3 Sox3 Gaba

##### Supertype — 0411 PVR Six3 Sox3 Gaba_1

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

###### Cluster — 1507 PVR Six3 Sox3 Gaba_1

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

#### Subclass — 090 BST-MPN Six3 Nrgn Gaba

##### Supertype — 0423 BST-MPN Six3 Nrgn Gaba_4

- [sdn_poa_calbindin_neuron](../sexually_dimorphic/sdn_poa_calbindin_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

###### Cluster — 1550 BST-MPN Six3 Nrgn Gaba_4

- [sdn_poa_calbindin_neuron](../sexually_dimorphic/sdn_poa_calbindin_neuron_summary.md) — skos:closeMatch · verdict pending

### Class — 12 HY GABA

#### Subclass — 106 PVpo-VMPO-MPN Hmx2 Gaba

##### Supertype — 0482 PVpo-VMPO-MPN Hmx2 Gaba_1

###### Cluster — 1876 PVpo-VMPO-MPN Hmx2 Gaba_1

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

##### Supertype — 0483 PVpo-VMPO-MPN Hmx2 Gaba_2

###### Cluster — 1891 PVpo-VMPO-MPN Hmx2 Gaba_2

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

###### Cluster — 1895 PVpo-VMPO-MPN Hmx2 Gaba_2

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

##### Supertype — 0486 PVpo-VMPO-MPN Hmx2 Gaba_5

- [arc_aromatase_neuron](../sexually_dimorphic/arc_aromatase_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending
- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending
- [avpv_th_neuron](../sexually_dimorphic/avpv_th_neuron_summary.md) — skos:closeMatch · verdict pending
- [mpoa_esr1_neuron](../sexually_dimorphic/mpoa_esr1_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

###### Cluster — 1915 PVpo-VMPO-MPN Hmx2 Gaba_5

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — skos:closeMatch · verdict pending
- [avpv_th_neuron](../sexually_dimorphic/avpv_th_neuron_summary.md) — skos:closeMatch · verdict pending

#### Subclass — 108 ARH-PVp Tbx3 Gaba

##### Supertype — 0494 ARH-PVp Tbx3 Gaba_2

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

### Class — 13 CNU-HYa Glut

#### Subclass — 116 AVPV-MEPO-SFO Tbr1 Glut

##### Supertype — 0521 AVPV-MEPO-SFO Tbr1 Glut_3

- [mpoa_esr1_neuron](../sexually_dimorphic/mpoa_esr1_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

### Class — 14 HY Glut

#### Subclass — 124 MPN-MPO-PVpo Hmx2 Glut

##### Supertype — 0550 MPN-MPO-PVpo Hmx2 Glut_5

- [avpv_kiss1_neuron](../sexually_dimorphic/avpv_kiss1_neuron_summary.md) — evidencell:UncertainRelationship · verdict pending

#### Subclass — 128 VMH Fezf1 Glut

##### Supertype — 0563 VMH Fezf1 Glut_1

- [vmhvl_esr1_pr_neuron](../sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

##### Supertype — 0564 VMH Fezf1 Glut_2

- [vmhvl_esr1_pr_neuron](../sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

#### Subclass — 133 PVH-SO-PVa Otp Glut

##### Supertype — 0585 PVH-SO-PVa Otp Glut_1

- [pvn_crfr1_neuron](../sexually_dimorphic/pvn_crfr1_neuron_summary.md) — skos:closeMatch · verdict pending

#### Subclass — 136 PMv-TMv Pitx2 Glut

##### Supertype — 0607 PMv-TMv Pitx2 Glut_3

- [pmv_otr_neuron](../sexually_dimorphic/pmv_otr_neuron_summary.md) — evidencell:CrossCuttingMatch · verdict pending

###### Cluster — 2470 PMv-TMv Pitx2 Glut_3

- [pmv_otr_neuron](../sexually_dimorphic/pmv_otr_neuron_summary.md) — skos:closeMatch · verdict pending

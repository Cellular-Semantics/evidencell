# Literature Review: amygdala_specific_report_ingest_20260528 — Amygdala Cell Types

> **Query:** amygdala cell types basolateral central medial intercalated paralaminar PKC-delta SST CRF FOXP2 PV CCK VIP NPY fear extinction morphology electrophysiology markers
> **Node context:** 28 amygdala cell types (BLA, CeA, MeA, intercalated, paralaminar, functional ensembles)
> **Evidence:** 36 summaries from 28 unique papers (35 papers in catalogue; 7 papers had no summaries returned)
> **Sources:** 30 asta_snippet, 6 europepmc_fulltext, 0 asta_report

---

## Theme 1 — Macro-organisation: cortical-like BLA vs. striatal-like CeA/MeA

Reviews and primary literature consistently partition the amygdala into a cortical-like basolateral complex (BLA = LA + BA/BL + BM), a striatal-like centromedial complex (CeA, MeA), intercalated cell masses (ITCs) at the BLA–CeA interface, and a paralaminar (PL) nucleus. The BLA is dominated by glutamatergic pyramidal-like principal cells; CeA/MeA by GABAergic neurons.

> "The BLA has a more cortical-like profile, primarily containing excitatory neurons, whereas the CeA and MeA have a striatal-like composition of largely inhibitory neurons" [35]

> "Developmentally, the BLA is a cortical-like structure consisting of 80% glutamatergic principal neurons and approximately 20% GABAergic inhibitory neurons" [11]

> "In contrast, CeA is a striatum-like structure that primarily comprises GABAergic inhibitory neurons" [11]

> "the corticobasolateral nuclei, whose cell types resemble those of the cerebral cortex, with glutamatergic, calcium-calmodulin dependent (CaM) kinase-positive principal cells that bear morphological resemblance to cortical pyramidal neurons" [18]

BL nucleus parcellation differs across species: in primates BL splits into magnocellular/intermediate/parvicellular; in rodents parcellation is inconsistent [2]:

> "The basolateral nuclear group contains three major nuclei, and these include lateral (La), basolateral (BL) (or basal [B]) and basomedial (BM) (or accessory basal [AB]) nuclei" [2]

> "In human and non-human primate, the BL (or B) is further parcellated into magnocellular (Bmc), intermediate (Bi) and parvicellular (Bpc) subdivisions" [2]

ITCs and PL fall outside the basolateral/centromedial/cortical groupings [9]:

> "Three other amygdalar nuclei [the anterior amygdala area (AAA), the amygdalo-hippocampal interface (AHi), and the intercalated cells (ITCs)] do not belong to any of these major groups." [9]

---

## Theme 2 — BLA principal cells and GABAergic interneuron diversity

The BLA principal cell (`bla_glutamatergic_principal_neuron`) is identified as a spiny, pyramidal-like VGluT1+/CaMKII+ glutamatergic projection neuron forming ~80–85% of BLA neurons — consistent with the curated node's SLC17A7/CAMK2A markers and abundance estimate [7, 22, 18]:

> "glutamatergic excitatory projection cells expressing vesicular glutamate transporter type 1 (VGluT1; Andrasi et al., 2017) are the most numerous neurons in this amygdala region (80-85%; Vereczki et al., 2021)." [7]

> "The dendrites of the principal cells (PC) are densely decorated with spines and their axon arborizes within the nucleus, giving rise to local collaterals, but they also project to other amygdala regions and remote cortical and/or subcortical areas" [7]

> "The most common type is a spiny multipolar neuron that often has a dominant dendrite giving it a pyramidal appearance. These cells are excitatory projection neurons because they have long axons that emit numerous collaterals" [22]

> "The second cell type consists of a morphologically heterogeneous group of sparsely spiny neurons that have a locally ramifying axon, are immunopositive for GABA" [22]

GABAergic interneurons form ~20% of BLA neurons and are as diverse as cortical/hippocampal interneurons [7]:

> "GABAergic inhibitory cells in the BLA comprise only 20% of the entire neuronal population, they provide essential control over proper network operation." [7]

> "Previous studies have uncovered that GABAergic cells in the basolateral amygdala are as diverse as those present in other cortical regions, including the hippocampus and neocortex." [7]

Bienvenu 2012 establishes four in-vivo identified classes that anchor `bla_pv_axo_axonic_cell`, `bla_axo_axonic_cell`, `bla_pv_basket_cell`, `bla_calbindin_dendrite_targeting_interneuron`, and a long-range projection class [27]:

> "Twenty eight GABAergic cells could be classified in four types: axo-axonic, parvalbumin-expressing basket, calbindin-expressing dendrite-targeting, and \"AStria-projecting\" cells." [27]

> "All axo-axonic cells expressed parvalbumin (PV), sometimes weakly (Figure 1F), but were never calbindin (CB)-positive." [27]

> "Calbindin-Expressing Dendrite-Targeting Cells Fire Synchronously with Hippocampal Theta Oscillations" [27]

### Theme 2a — Parallel PV vs. CCK basket networks

Andrási 2017 demonstrates two non-overlapping perisomatic basket cell networks, supporting the curated distinction between `bla_pv_basket_cell` and `bla_cck_basket_cell`/`bla_cck_cb1_basket_cell` [26]:

> "2 parallel basket cell networks expressing either parvalbumin or cholecystokinin. While the 2 basket cell types are mutually interconnected within their own category via synapses and gap junctions, they avoid innervating each other, but form synaptic contacts with axo-axonic cells." [26]

> "a monosynaptic connection from CCKBCs to CCKBCs and from PVBCs to PVBCs could be detected with high probability" [26]

> "both basket cell types have the similar potency to control principal neuron spiking, but they receive excitatory input from principal neurons with entirely diverse features." [26]

CCK interneurons further split into CCK-L (calbindin+/VGluT3+, large soma) and CCK-S (NPY+, small soma) [10]:

> "In rodent BA, CCK INs with large soma (CCK-L) express either vesicular glutamate transporter type 3 (VGluT3) or Ca 2+ binding protein, calbindin (Calb) and are distingushed from NPY-expressing CCK INs with small soma (CCK-S)" [10]

Rovira-Esteban 2019 confirms four BA CCK-targeted interneuron classes with NPY (29%) and PV (17%) co-expression but no SOM co-expression [10]:

> "Further morphological and electrophysiological analyses showed that four IN types could be identified among the EYFP-expressing cells: CCK/cannabinoid receptor type 1 (CB1R)-expressing basket cells, neurogliaform cells, PV+ basket cells, and PV+ axo-axonic cells." [10]

> "immunostaining showed that subsets of the genetically-targeted cells expressed either neuropeptide Y (NPY; 29%) or parvalbumin (PV; 17%), but not somatostatin (SOM) or Ca2+/calmodulin-dependent protein kinase II (CaMKII)-α." [10]

### Theme 2b — VIP+/calretinin/CCK interneurons in primates

Totty 2024 primate snRNA-seq identifies two VIP+ clusters (13% of inhibitory neurons) co-expressing CALB2 (calretinin), CCK, CRH, CNR1 — consistent with `bla_vip_calretinin_interneuron` and `bla_vip_cr_interneuron_selective_interneuron` [3]:

> "both clusters showed increased expression of genes (Fig. 3B) encoding calretinin (CALB2), cholecystokinin (CCK), corticotropin releasing hormone (CRH), cannabinoid receptor 1 (CNR1)" [3]

> "A third cluster of CCK+ neurons (CCK+/CNR1+) consisted of 5.28% of all inhibitory neurons analyzed... This CCK+/CNR1+ cluster is likely homologous to mouse CCK+ basket cells, which synapse onto the soma and proximal dendrites of excitatory neurons" [3]

---

## Theme 3 — Central amygdala: PKC-δ vs. SST dichotomy, CRF, and a novel Isl1+ projection cell

Haubensak 2010 established PKC-δ+ CeL cells as the inhibitory CeL-OFF class gating CeM output, supporting `cea_pkc_delta_neuron` [24]:

> "PKC-δ+ neurons inhibit output neurons in the medial central amygdala (CEm), and also make reciprocal inhibitory synapses with PKC-δ− neurons in CEl." [24]

> "Electrical silencing of PKC-δ+ neurons in vivo suggests that they correspond to physiologically identified units that are inhibited by the conditioned stimulus, called CEloff units." [24]

Li 2013 establishes the complementary SST+ CeL-ON role supporting `cea_som_neuron` [23]:

> "preventing synaptic potentiation onto somatostatin-positive neurons impaired fear memory formation." [23]

> "activation of these neurons was necessary for fear memory recall and was sufficient to drive fear responses." [23]

Adke 2019 confirms electrophysiology and largely non-overlapping populations [15]:

> "Two genetically identified cell types, protein kinase C-expressing (PKCd+) neurons and somatostatin-expressing (Som+) neurons, constitute most CeLC neurons and are largely non-overlapping" [15]

> "The activity of PKCd+ cells, for example, is reduced following exposure to a conditioned stimulus after fear conditioning (Haubensak et al., 2010) but increased following nerve injury" [15]

Nisbett 2025 reaffirms the ephys split (late-firing PKC-δ vs. later/regular-spiking SST) [1]:

> "One population expresses protein kinase Cδ and comprises predominantly late-firing neurons (Li et al., 2013). They are referred as CeL OFF neurons because they respond to fear-conditioned stimuli with reduced activity" [1]

> "The other population instead expresses somatostatin, which can be later firing or regular spiking" [1]

Yeh 2024 enumerates the broader CeA marker complement — PKC-δ, CRF, Calcrl, SOM, Htr2a, Tac2, Drd1/Drd2 [4]:

> "Key markers include protein kinase C-δ (PKC-δ) (Haubensak et al., 2010), corticotropin-releasing factor (CRF) (Pitts et al., 2009; Sanford et al., 2017), calcitonin receptor-like (Calcrl) (Han et al., 2005), somatostatin (SOM) (Penzo et al., 2014), serotonin receptor 2a (Htr2a) (Isosaka et al., 2015), and tachykinin 2 (Tac2) (Andero et al., 2014)" [4]

**O'Leary 2022 is the most important novelty for the curated CeA nodes:** an Isl1+ medial-CeA cell type accounts for many long-range CeA projections, and PKC-δ/SST are themselves transcriptomically heterogeneous [19]:

> "we identify two major cell types, encompassing one-third of all CEA neurons, that have gone unresolved in previous studies" [19]

> "we identify a non-canonical CEA subdomain associated with Nr2f2 expression and uncover an Isl1-expressing medial cell type that accounts for many long-range CEA projections" [19]

> "Prkcd and Sst each exhibited mixed expression across multiple scRNA-seq-clusters" [19]

---

## Theme 4 — Intercalated cell masses: conserved TSHZ1+/FOXP2+ inhibitory pairs

Totty 2024 (primate) and Yu 2023 (cross-species) converge on two TSHZ1+/FOXP2+ inhibitory clusters as the conserved ITC populations, sub-distinguished by DRD1±, D3, and HTR7 expression and by spiny vs. aspiny morphology [3, 36]:

> "We identified two distinct clusters of TSHZ1+/FOXP2+ interneurons that were highly conserved across nonhuman primates and humans and that differed in their expression of the D3 dopamine receptor and 5-HT7 serotonin receptor" [3]

> "suggesting that the D3-enriched population was spiny and the HTR7-enriched population was aspiny, confirming a prior morphological analysis of ITC neurons" [3]

> "the IA subnuclei were highly conserved, and all mammals in our datasets contained two types of TSHZ1+ neurons, i.e., DRD1+ and DRD1−." [36]

These directly map onto `intercalated_cell_mass_neuron` (FOXP2+, DRD1+, OPRM1+). The Sarowar review independently notes the OPRM1+ characterisation [12]:

> "The majority of BLA neurons are spiny glutamatergic neurons (with a minority of GABAergic interneurons). CEl and CEm mainly contain GABAergic neurons. The ICMs are small cell clusters and consist of more dopamine type-1 and µ-opioid-receptor expressing cells" [12]

Totty 2024 also places ITC neurons developmentally in the LGE-derived (MEIS2+, ZFHX3+) lineage alongside PKC-δ+ CeA cells, parallel to MGE (SST/PVALB/LAMP5) and CGE (VIP/CCK) lineages:

> "We identified 18 different types of inhibitory neurons in the primate amygdala (Fig. 3A) with representation of all major interneuron classes (SST, PVALB, VIP, CCK, and LAMP5)." [3]

> "We also identified clusters corresponding to protein kinase C-δ+ (PKRCD+/SST−) interneurons in the central nucleus" [3]

---

## Theme 5 — Medial amygdala: dual origin, Lhx6/Lhx9, and a radial pallial model

Carney 2010 establishes the developmental Lhx9/Lhx6 dichotomy underpinning `medial_amygdala_lhx9_glutamatergic_neuron` and `medial_amygdala_gabaergic_neuron` [25]:

> "the posterior portion of the MeA is divided into dorsal (medial posterodorsal nucleus (MePD)) and ventral (medial posteroventral nucleus (MePV)) subdivisions, which via their projections to distinct hypothalamic nuclei regulate reproductive and defensive behaviors, respectively" [25]

> "the anatomical segregation of efferent projections that regulate reproductive or defensive behaviors is differentially marked by the LIM-containing homeodomain genes Lhx6 and Lhx9" [25]

Yeh 2024 confirms MeA's mixed pallial/subpallial origin [4]:

> "The MeA, deriving from both ventral pallial and subpallial origins, presents a diverse neuronal population" [4]

Fernández 2025 provides molecular evidence for two super-radial pallial-amygdala domains aligning with the BLA vs. MeA glutamatergic split [5]:

> "at low resolution, the whole pallial amygdala was found to divide into two super-radial domains distinguished by differential expression of Slc17a6 and Slc17a7; the former partly imitates molecularly the subpallial (output) amygdalar regions" [5]

This supports `mea_glutamatergic_projection_neuron` (Slc17a6-leaning) vs. `bla_glutamatergic_principal_neuron` (Slc17a7) as molecularly distinct excitatory classes.

---

## Theme 6 — Paralaminar immature neurons and whole-amygdala single-cell atlases

Yu 2023 provides cross-species evidence for `paralaminar_immature_neuron` as a primate-expanded population expressing SOX11 and BCL2 [36]:

> "humans and macaques contained a neuronal cluster with high expression of immature markers, such as SOX11 and BCL2, which were likely derived from the PL" [36]

> "LAMP5+ interneurons were much more abundant in primates, while DRD2+ inhibitory neurons and LAMP5+SATB2+ excitatory neurons were dominant in the human central amygdalar nucleus (CEA) and basolateral amygdalar complex (BLA)" [36]

Two foundational atlases underlie multiple nodes:

- **Hochgerner 2022** (mouse, scRNA-seq, 130 neuronal types, fear conditioning) [20]:

> "We performed single-cell RNA-seq on naïve and fear conditioned mice, inferred the 130 neuronal cell types distributions in silico using orthogonal spatial transcriptomic datasets" [20]

> "Only a fraction of cells, within a subset of all neuronal types, were transcriptionally responsive to fear learning, memory and retrieval." [20]

- **Zhou 2023** (rat snRNA-seq atlas, 7 inhibitory subtypes including Cck+/Vip+ and Nos1+) [21]:

> "we identified seven subtypes of inhibitory neurons based on the expression of known cell marker genes" [21]

> "the pathway enrichment analysis of the transcriptomic data suggest that GABAergic synapse-related genes may be specific to Cck+/Vip+ and Nos1+ subtypes of inhibitory neurons" [21]

---

## Theme 7 — Functional fear/extinction ensembles

`basal_amygdala_fear_neuron` and `basal_amygdala_extinction_neuron` are activity-defined, not molecularly defined. PV+SOM BLA interneurons cooperate during fear acquisition; BA CCK interneurons facilitate extinction when activated [10]:

> "an elegant series of studies has shown that PV-containing and SOM-containing BA INs act in concert to gate the responses of PNs to conditioned stimulus (CS) and un-conditioned stimulus (US) during fear memory acquisition" [10]

> "The current findings add to a growing literature by describing a unique population of INs in the BA that, when activated, exert strong modulatory effects on extinction." [10]

> "The resultant research has defined the amygdala as a central node within a distributed neural system comprising cortical, hippocampal, and midbrain structures, among others." [10]

---

## Evidence gaps for amygdala KB nodes

- **defining_markers: partial.**
  - Well-supported: `bla_glutamatergic_principal_neuron` (VGluT1/SLC17A7, CAMK2A); `bla_pv_basket_cell`/`bla_pv_axo_axonic_cell`/`bla_axo_axonic_cell` (PV±CB); `bla_cck_basket_cell` (CCK, CB, VGluT3); `bla_cck_cb1_basket_cell` (CCK, CNR1); `bla_vip_calretinin_interneuron` and `bla_vip_cr_interneuron_selective_interneuron` (VIP, CALB2, CCK, CRH, CNR1); `cea_pkc_delta_neuron` (PRKCD); `cea_som_neuron` (SST); `cea_crf_neuron` (CRH); `intercalated_cell_mass_neuron` (FOXP2, TSHZ1, DRD1 in subsets); `paralaminar_immature_neuron` (SOX11, BCL2, DCX, NCAM1); `medial_amygdala_lhx9_glutamatergic_neuron` (LHX9).
  - Gaps: `bla_sst_interneuron` vs `bla_som_dendrite_targeting_interneuron` not distinguished in corpus; `bla_calbindin_dendrite_targeting_interneuron` (CB+ no SST) only weakly separable from SST+/CALB1+ cells; `bla_gabaergic_projection_neuron` (curated as SST+/NOS1+) conflicts with Bienvenu's PV+/CB+ AStria-projecting class — needs reconciliation; `cea_medium_spiny_neuron`, `cea_large_aspiny_neuron`, `cea_small_aspiny_neuron` have no molecular markers in this corpus; `central_amygdala_gabaergic_projection_neuron` markers unspecified (Isl1+ O'Leary 2022 is a strong candidate); `medial_amygdala_gabaergic_neuron` anchored only to Lhx6; `mea_glutamatergic_projection_neuron` only anchored to Slc17a6.
- **anatomical_location: yes.** BLA/LA/BM, CeC/CeL/CeM, MePD/MePV, ITCs at the BLA–CeA interface, and PL all explicitly described.
- **nt_type: yes.** All 28 nodes have unambiguous GABAergic vs glutamatergic assignments.
- **electrophysiology_class: partial.**
  - Well-supported: `cea_pkc_delta_neuron` (late-firing, CeL-OFF), `cea_som_neuron` (later-firing or regular spiking), `bla_pv_basket_cell` (fast-spiking, perisomatic), `bla_glutamatergic_principal_neuron` (regular spiking with accommodation, Washburn 1992).
  - Gaps: `bla_axo_axonic_cell` only described as "fired dramatically on noxious stimuli" in vivo; `bla_calbindin_dendrite_targeting_interneuron` is theta-synchronous, not fast-spiking; CeA classical ephys classes (`cea_medium_spiny_neuron`, `cea_large_aspiny_neuron`, `cea_small_aspiny_neuron`) absent from corpus; ITC ephys not separately quantified — only D3-spiny vs HTR7-aspiny morphology.
- **morphology_notes: partial.**
  - Well-supported: BLA principal cells (spiny pyramidal-like, multipolar); `bla_pv_basket_cell`/`bla_cck_basket_cell` perisomatic targeting; `bla_pv_axo_axonic_cell`/`bla_axo_axonic_cell` AIS targeting; `bla_calbindin_dendrite_targeting_interneuron` dendrite-targeting, theta-synchronous; ITC D3-spiny vs HTR7-aspiny.
  - Gaps: `cea_medium_spiny_neuron`, `cea_large_aspiny_neuron`, `cea_small_aspiny_neuron` classical morphology descriptions likely require targeted retrieval of McDonald 1982 / Sun & Cassell 1993; `medial_amygdala_gabaergic_neuron` and `mea_glutamatergic_projection_neuron` morphology mentioned only as "heterogeneous" by Niimi 2012 metadata.

---

## New classical types encountered

1. **Isl1+ medial-CeA projection cell** (O'Leary 2022, CorpusId:253356112). Accounts for many long-range CEA projections; distinct from PKC-δ+ and SST+. **Suggested action: add stub** (`cea_isl1_projection_neuron`); likely refines or replaces `central_amygdala_gabaergic_projection_neuron`.
2. **Nr2f2+ CeA subdomain cells** (O'Leary 2022). Non-canonical lateral-intermediate CeA subdomain. **Suggested action: defer** until replicated.
3. **Tac2 CeA neurons** (Yeh 2024 review, Andero 2014). Implicated in fear conditioning. **Suggested action: defer**.
4. **Calcrl CeA neurons** (Yeh 2024 review, Han 2005). **Suggested action: defer.**
5. **Htr2a CeA neurons** (Yeh 2024 review, Isosaka 2015). **Suggested action: defer.**
6. **DRD1+ vs DRD1− TSHZ1+ ITC subtypes** (Yu 2023, Totty 2024). Two-subtype split within `intercalated_cell_mass_neuron`. **Suggested action: refine existing node** to encode DRD1±/D3±/HTR7± distinction, or split into `itc_drd1_spiny_neuron` and `itc_htr7_aspiny_neuron`.
7. **LAMP5+ amygdala interneurons** (Totty 2024, Yu 2023). A major canonical interneuron class abundant in primates, not represented in the 28-node set. **Suggested action: add stub** as `bla_lamp5_interneuron`.
8. **LAMP5+SATB2+ excitatory neurons** (Yu 2023). Dominant in human CEA and BLA. **Suggested action: defer** (primate/human-specific; revisit during human-atlas mapping).
9. **PV+/CB+ AStria-projecting BLA GABAergic cells** (Bienvenu 2012, CorpusId:10647550). Conflicts with curated `bla_gabaergic_projection_neuron` (SST+/NOS1+). **Suggested action: investigate** — may be two distinct long-range GABAergic projection populations within BLA.

---

## References

[1] Nisbett & Koob (2025). Neuronal Colocalization of μ-Opioid Receptor, κ-Opioid Receptor, and Oxytocin Receptor mRNA in the Central Nucleus of the Amygdala in Male and Female Mice. *eNeuro*. CorpusId:280558687
[2] Zhu et al. (2025). Brain-wide connections of the parvicellular subdivision of the basolateral and basomedial amygdaloid nuclei in the rats. *Frontiers in Neural Circuits*. CorpusId:278109019
[3] Totty et al. (2024). Transcriptomic diversity of amygdalar subdivisions across humans and nonhuman primates. *bioRxiv*. CorpusId:273531817
[4] Yeh et al. (2024). Molecular diversity and functional dynamics in the central amygdala. *Frontiers in Molecular Neuroscience*. CorpusId:267685584
[5] Fernández et al. (2025). Transcriptomic Analysis Corroborates the New Radial Model of the Mouse Pallial Amygdala. *Biomolecules*. CorpusId:280713728
[6] Gui et al. (2025). The left amygdala is genetically sexually-dimorphic: multi-omics analysis of structural MRI volumes. *Translational Psychiatry*. CorpusId:275818530
[7] Hájos (2021). Interneuron Types and Their Circuits in the Basolateral Amygdala. *Frontiers in Neural Circuits*. CorpusId:235382885
[8] McDonald (2024). Functional neuroanatomy of basal forebrain projections to the basolateral amygdala: transmitters, receptors, and neuronal subpopulations. *Journal of Neuroscience Research*. CorpusId:268497805
[9] Aerts & Seuntjens (2021). Novel Perspectives on the Development of the Amygdala in Rodents. *Frontiers in Neuroanatomy*. CorpusId:244956947
[10] Rovira-Esteban et al. (2019). Excitation of Diverse Classes of Cholecystokinin Interneurons in the Basal Amygdala Facilitates Fear Extinction. *eNeuro*. CorpusId:204835327
[11] Hu et al. (2022). New Insights into the Pivotal Role of the Amygdala in Inflammation-Related Depression and Anxiety Disorder. *International Journal of Molecular Sciences*. CorpusId:252477669
[12] Sarowar & Grabrucker (2020). Rho GTPases in the Amygdala—A Switch for Fears? *Cells*. CorpusId:221366115
[13] Pineda et al. (2021). Extrahypothalamic Control of Energy Balance and Its Connection with Reproduction: Roles of the Amygdala. *Metabolites*. CorpusId:244936719
[14] (see [10])
[15] Adke et al. (2019). Cell-Type Specificity of Neuronal Excitability and Morphology in the Central Amygdala. *eNeuro*. CorpusId:209598438
[16] (see [5])
[17] Vereczki et al. (2016). Synaptic Organization of Perisomatic GABAergic Inputs onto the Principal Cells of the Mouse Basolateral Amygdala. *Frontiers in Neuroanatomy*. CorpusId:16327247
[18] Wilson et al. (2015). Stress as a one-armed bandit: Differential effects of stress paradigms on the morphology, neurochemistry and behavior in the rodent amygdala. *Neurobiology of Stress*. CorpusId:31039293
[19] O'Leary et al. (2022). Neuronal cell types, projections, and spatial organization of the central amygdala. *iScience*. CorpusId:253356112
[20] Hochgerner et al. (2022). Cell types in the mouse amygdala and their transcriptional response to fear conditioning. *bioRxiv*. CorpusId:253206255
[21] Zhou et al. (2023). Single-nucleus genomics in outbred rats with divergent cocaine addiction-like behaviors reveals changes in amygdala GABAergic inhibition. *Nature Neuroscience*. CorpusId:263704470
[22] Paré & Gaudreau (1996). Projection Cells and Interneurons of the Lateral and Basolateral Amygdala. *Journal of Neuroscience*. CorpusId:17655278
[23] Li et al. (2013). Experience-dependent modification of a central amygdala fear circuit. *Nature Neuroscience*. CorpusId:10650261
[24] Haubensak et al. (2010). Genetic dissection of an amygdala microcircuit that gates conditioned fear. *Nature*. CorpusId:2270983
[25] Carney et al. (2010). Sonic hedgehog expressing and responding cells generate neuronal diversity in the medial amygdala. *Neural Development*. CorpusId:627853
[26] Andrási et al. (2017). Differential excitatory control of 2 parallel basket cell networks in amygdala microcircuits. *PLoS Biology*. CorpusId:13486665
[27] Bienvenu et al. (2012). Cell-Type-Specific Recruitment of Amygdala Interneurons to Hippocampal Theta Rhythm and Noxious Stimuli In Vivo. *Neuron*. CorpusId:10647550
[28] Niimi et al. (2012). Heterogeneous electrophysiological and morphological properties of neurons in the mouse medial amygdala in vitro. *Brain Research*. CorpusId:15738241
[29] Bzdok et al. (2012). An Investigation of the Structural, Connectional, and Functional Subspecialization in the Human Amygdala. *Human Brain Mapping*. CorpusId:19021055
[30] Chareyron et al. (2011). Stereological Analysis of the Rat and Monkey Amygdala. *The Journal of comparative neurology*. CorpusId:16013850
[31] Gilpin et al. (2014). The Central Amygdala as an Integrative Hub for Anxiety and Alcohol Use Disorders. *Biological Psychiatry*. CorpusId:442779
[32] Beyeler & Dabrowska (2020). Neuronal diversity of the amygdala and the bed nucleus of the stria terminalis. *Handbook of Behavioral Neuroscience*. CorpusId:216440056
[33] McDonald (2020). Functional neuroanatomy of the basolateral amygdala. *Handbook of Behavioral Neuroscience*. CorpusId:216417665
[34] Nikolenko et al. (2020). Amygdala: Neuroanatomical and Morphophysiological Features. *Brain Science*. CorpusId:220976356
[35] Zhang et al. (2021). Amygdala Circuit Substrates for Stress Adaptation and Adversity. *Biological Psychiatry*. CorpusId:230972365
[36] Yu et al. (2023). Molecular and cellular evolution of the amygdala across species. *Cell Discovery*. CorpusId:256832817
[37] Washburn & Moises (1992). Electrophysiological and morphological properties of rat basolateral amygdaloid neurons in vitro. *Journal of Neuroscience*. CorpusId:6078957

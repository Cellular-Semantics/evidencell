# Literature Review: Amygdala Cell Types — ASTA Corpus Traverse

> **Query:** amygdala cell types basolateral central medial intercalated paralaminar GABAergic interneuron PV SST CCK VIP NPY fear extinction
> **Node context:** 15 amygdala cell type nodes (BLA principal + 6 BLA interneuron types + BLA GABAergic projection, CeA, MeA GABAergic + Lhx9+ Glu, intercalated cells, paralaminar immature neurons, fear/extinction neurons)
> **Evidence:** 58 summaries from 15 unique papers
> **Sources:** 57 asta_snippet, 1 europepmc_fulltext

## BLA interneuron census and the seven cardinal GABAergic cell types

The most quantitatively complete characterisation of basolateral amygdala (BLA) inhibitory cell composition in this corpus comes from Vereczki et al. 2021 [14], whose stereological census of mouse lateral (LA) and basal (BA) amygdala anchors the seven cardinal GABAergic node types under study.

> "axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%)" [14]

The same paper establishes that overall GABAergic proportions differ between the two BLA subdivisions: "the ratio of GABAergic neurons in the BA (22 %) is significantly higher than in the LA (16 %) in both male and female mice" [14]. The completeness of the inventory is confirmed by summing across all seven types: "the vast majority of GABAergic cells in the LA and BA belong to the seven cardinal inhibitory cell categories examined in this study" [14] and "Adding up the fractions of each GABAergic cell type resulted in a sum, which is close to the ratios of GABAergic cells obtained by unbiased stereological analysis" [14], with only a minor additional M2-receptor-expressing population beyond the seven cardinal types.

Independent corroboration comes from earlier literature. Woodruff & Sah 2007 [38] describes: "Four populations of interneurons have been described in the BLA: those expressing parvalbumin (McDonald, 1992;McDonald and Betette, 2001), those expressing somatostatin (McDonald and Mascagni, 2002), those expressing cholecystokinin and either cal" [38]. McDonald et al. 2012 [37] parallels this: "four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide" [37]. The PV+ basket vs. axo-axonic cell distinction is supported by Perumal & Sah 2021 [13]: "PV+ cells have been separated into basket cells, axo-axonic chandelier cells and AStria cells" [13], with quantification from Ünal et al. 2020 [19]: "PV+ interneurons form perisomatic baskets or axoaxonic synapses on principal neurons and constitute around 50% of the total interneuron population" [19].

The BLA glutamatergic principal neuron fraction: "local microcircuits are formed by excitatory glutamatergic neurons that make ~80% of total neuronal population and GABAergic interneurons" [13]; "Principal neurons, which are similar to pyramidal neurons in the hippocampus and cortex, constitute the majority (85-90%) of the BLA neuronal population" [38]; "In the basolateral group, approximately 70% of neurons are thought to be glutamatergic (pyramidal, spiny, or class I neurons)" [31]. The range reflects species and method differences.

## SST+ interneurons and the SST/nNOS GABAergic projection neuron

SST+ cells in BLA serve a dual identity mapping to two distinct nodes (`bla_sst_interneuron` vs. `bla_gabaergic_projection_neuron`). Vereczki et al. 2021 [14] provides the dendrite-targeting connectivity profile: "SST+ inhibitory cells target predominantly the dendritic shaft and to a lesser extent, the spines of principal cells" [14], and distinguishes the SST+/nNOS+ projection subpopulation:

> "SST+ GABAergic cells that project to the basal forebrain or entorhinal cortex (McDonald et al., 2012;McDonald and Zaric, 2015) were found to be immunopositive for nNOS" [14]

McDonald et al. 2012 [37] supplies primary retrograde tracing evidence: "a subpopulation of non-pyramidal SOM+ neurons, termed 'long-range non-pyramidal neurons' (LRNP neurons), in the external capsule, basolateral amygdala, and cortical and medial amygdalar nuclei were FG+" [37] and "Virtually all of the non-pyramidal neurons in the amygdala that had long-range projections to the BF (LRNP neurons) expressed SOM" [37]. About one-third co-express calbindin or NPY: "About one-third of the SOM+ LRNP neurons were CB+ or NPY+, and one-half were GAD+" [37].

Functional characterisation of local SST+ interneurons from Ünal et al. 2020 [19]: "This study concludes that LTS interneurons, most of which are putatively SOM+, mediate feedback inhibition in the LA" [19]. SST/NPY/calbindin co-expression: "SOM positive interneurons constitute the other common interneuron population and they co-express markers such as neuropeptide Y (NPY) and calbindin" [19], targeting: "SOM+ interneurons selectively target the dendrites of BLA principal neurons" [19].

## Axo-axonic (chandelier) cells: amygdala-wide distribution and PN dependence

Raudales et al. 2024 [5] (Results, europepmc_fulltext) provides the brain-wide reference for `bla_axo_axonic_cell`:

> "we found AACs or pAACs in all the amygdala nuclei containing GLU PNs, that is except CeA" [5]

> "The density of AACs in amygdala appears to correlate with the known abundance of GLU PNs: densities in BLA, CoA, and BMA were much higher than those in MeA and BST" [5]

AIS-targeting verified: "Sparse labeling and immunohistochemical co-staining with AnkG confirmed that the labeled cells in these compartments were nearly exclusively AIS-targeting (97.2%, n = 36 cells, 6 mice)" [5]. Nucleus-NT logic: "PNs are exclusively glutamatergic in BLA, CoA, BMA, exclusively GABAergic in CeA, and predominantly GABAergic in MeA and BST" [5] — directly predicts AAC absence from CeA. Functional separation from Perumal & Sah 2021 [13]: "basket type PV+ cells form the main subtype of GABAergic neurons that provide strong somatic inhibition on principal neurons and tightly control spike discharge" [13] and "some PV+ chandelier cells have been reported to recruit principal neurons and drive feedback and feedforward circuits in vitro" [13].

## NPY neurogliaform, CCK basket, and VIP/calretinin interneurons

Vereczki et al. 2021 [14] resolves NPY+ population heterogeneity: "a significant fraction (~ 25 %) of these neurons was immunoreactive for PV" [14], "a similarly large portion (~ 27 %) of EYFP-expressing GABAergic neurons showed immunoreactivity against SST" [14], and "about half of the NPY+ GABAergic neurons (~ 45% in both amygdalar nuclei) was immunoreactive neither for PV nor for SST, a group of neurons that should correspond to neurogliaform cells" [14]. The pure neurogliaform subset is confirmed: "NPY has been shown to be expressed often in neurogliaform cells" [14], supporting `bla_npy_neurogliaform_cell` as ~45% of NPY+ GABAergic cells.

The CCK basket vs. VIP interneuron-selective distinction, from Vereczki et al. 2021 [14] Results: "the vast majority of GFP-expressing interneurons was CCK+/CB1+ basket cell (71.1 %, n = 38 recorded green neurons)" [14] and "The minority of recorded neurons (28.9 %, n = 38 recorded green cells) was found to be immunonegative for CB1 (8 out of 8 tested for axon terminals), but showed immunopositivity for VIP in the soma" [14]. This Results-grade evidence directly supports the molecular separation of `bla_cck_basket_cell` and `bla_vip_calretinin_interneuron`.

## Single-cell transcriptomic taxonomy of mouse amygdala

Hochgerner et al. 2023 [6] provides primary-evidence molecular taxonomy spanning BLA, CEA, IA, and MEA. Local interneuron markers: "Local/interneuron markers Nfib, Nfix, Tcf4, Satb1 and Prox1 were expressed among canonical medial ganglionic eminences (MGE)-and caudal ganglionic eminences (CGE)-derived interneuron types (for example, Sst, Pvalb, Vip or Sncg)" [6]. CEA inhibitory diversity: "Most CEA cells (GABA-5 to GABA-21) expressed Six3, and Ano3, axon guidance-encoding gene Epha4" [6] and "The Ppp1r1b types correlated with the lateral CEA" [6]. ITC-related types: "GABA-5 to GABA-7 were related to ITCs and expressed the tachykinin receptor Tacr3, specifically Tshz2 and Enpp2, Nts and Th or Cyp26a1" [6]. MEA-projecting neuropeptide-rich types: "GABA-22 coexpressed neuropeptides galanin and vasopressin (Gal and Avp) and was located to the MEA-ad" [6]. LA glutamatergic subtypes: "Grp-expressing pyramidal neurons were previously identified in the LA, where a local circuitry with Grpr-expressing LA interneurons influenced certain aspects of fear memory" [6].

## Functional roles in fear learning, expression, and extinction

From Perumal & Sah 2021 [13]:

> "activating PV+ cells during associative fear learning (i.e., CS-US pairing) reduced learning to the CS+, showing that the activity of PV+ interneurons is necessary for effective learning" [13]

> "manipulation of SST+ interneurons had the opposite effect. Driving these cells during CS+ presentation reduced learning" [13]

> "VIP cells drive disinhibitory circuit operations in the BLA in the fear conditioning paradigm" [13]

CEA's role via descending GABAergic projections, from Vicario et al. 2014 [32]: "the central amygdala was considered responsible of the expression of conditioned fear responses, by way of descending GABAergic projections to hypothalamic and brainstem targets" [32]. Intercalated cells in extinction: "The intercalated amygdalar cells constitute an interface between the infralimbic prefrontal cortex and the lateral-basolateral pallial amygdala on the one hand, and the central amygdala on the other, and are involved in extinction of fear memories" [32]. These Introduction-level statements support `basal_amygdala_fear_neuron`, `basal_amygdala_extinction_neuron`, `central_amygdala_gabaergic_projection_neuron`, and `amygdala_intercalated_cell` at a conceptual level but provide no molecular markers for the fear/extinction functional types.

## Intercalated, central, and medial amygdala GABAergic landscape

Pitkänen & Amaral 1994 [43] is the primate-anatomical anchor: "GABAergic neurons were distributed throughout the amygdaloid complex and accounted for approximately 20% of the neuronal population, at least in the lateral nucleus" [43] and "In some regions, such as the intercalated nuclei, virtually all of the resident neurons appeared to be GABAergic" [43]. CeA density paradox: "despite the low number of GABA-immunoreactive neurons, the terminal density in the central nucleus was among the highest in the amygdala" [43].

Veinante et al. 2013 [35]: "a few nuclei of the amygdala remain unclassified, among them the intercalated cell masses which are small clusters of densely packed GABAergic neurons" [35] and "The CeA has three subdivisions: capsular (CeLC), central (CeL) and medial (CeM), that are defined based on cytoarchitecture, neurochemistry and connectivity" [35].

Gerlach & Wullimann 2021 [12] for medial amygdala mosaic: "the mammalian/rodent medial amygdala is a mosaic of GABAergic subpallial cells complemented by glutamatergic neuron types from extrinsic sources (ventral pallium, SPV, EmT)" [12] and "excitatory glutamatergic cells migrate tangentially into the mouse medial amygdala from nearby brain structures, such as ventral pallium (VP), the hypothalamic supraopto-paraventricular region (SPV), and the eminentia thalami (EmT)" [12].

## Paralaminar nucleus and immature excitatory neurons in primate amygdala

Sorrells et al. 2019 [21] (Nature Communications Results) anchors `paralaminar_immature_neuron`:

> "In the adult human amygdala the PL is located near the dorsal wall of the tLV, next to the caudal ganglionic eminence (CGE), a site of birth of GABAergic inhibitory interneurons during embryonic and fetal development that expresses the transcription factors SP8, PROX1, and COUP-TFII (Nr2f2)" [21]

> "In rodents, dense clusters of GABAergic cells are located around the basolateral amygdala (BLA) and these clusters, called the intercalated nuclei, are similar in location and appearance to the PL, but do not express DCX and PSA-NCAM" [21]

Markers DCX, BCL2, NCAM1, SP8, NR2F2/COUP-TFII, and PROX1 explicitly supported. This grounding distinguishes the human/primate PL excitatory immature neuron from the GABAergic ITC despite historical anatomical confusion.

## Evidence gaps for amygdala node set

- **defining_markers:**
  - `bla_pv_basket_cell`: PVALB — well-supported [13][14][19][37][38]
  - `bla_axo_axonic_cell`: PVALB + AIS-targeting — supported [5][13][14]
  - `bla_sst_interneuron`: SST, CALB1 — supported [14][19][37]
  - `bla_cck_basket_cell`: CCK, CALB1, CB1 — supported [14][37][38]
  - `bla_vip_calretinin_interneuron`: VIP, CALB2, CCK — supported [14][37][38]
  - `bla_npy_neurogliaform_cell`: NPY (with PV/SST/CB absence) — supported [14]
  - `bla_gabaergic_projection_neuron`: SST + NOS1/nNOS — supported [14][37]
  - `bla_glutamatergic_principal_neuron`: no specific gene marker quoted; Grp subtype [6] — partial
  - `central_amygdala_gabaergic_projection_neuron`: Six3/Ano3/Epha4/Ppp1r1b/Crym from scRNA-seq [6] — partial, no canonical marker
  - `medial_amygdala_gabaergic_neuron`: Lhx6 + galanin/vasopressin [6]; MGE-derived SST/Nkx2.1 [32] — partial
  - `medial_amygdala_lhx9_glutamatergic_neuron`: **LHX9 not mentioned in any snippet** — major gap
  - `amygdala_intercalated_cell`: GABAergic confirmed [21][32][35][43]; Tacr3/Tshz2 from scRNA-seq [6] — partial
  - `paralaminar_immature_neuron`: DCX, BCL2, NCAM1, SP8, NR2F2, PROX1 — well-supported [21]
  - `basal_amygdala_fear_neuron`: no canonical molecular marker — major gap
  - `basal_amygdala_extinction_neuron`: no canonical molecular marker — major gap
- **electrophysiology:** SST+/LTS in LA [19]; PV+ somatic inhibition [13]; six discharge-property groups in LA/BA [18]. No quantitative biophysical values — gap for all nodes.
- **morphology:** Per-node morphometry absent across all nodes.
- **species homology:** No primary human BLA interneuron census available in this corpus.

## New classical types encountered

| Type | Papers | Action |
|---|---|---|
| PV+ AStria cells (amygdalostriatal transition area) | [13] | defer |
| CEA Ppp1r1b/DARPP-32 lateral MSN-like neurons | [6] | consider adding stub |
| CEA-located ITC-related types (GABA-5–7, Tacr3+) | [6] | already covered by `amygdala_intercalated_cell` |
| MEA-projecting Lhx6+ galanin/vasopressin inhibitory cells | [6] | consider adding stub |
| CEA enkephalinergic LGEd Pax6+ cells | [32] | defer |
| CEA CRF+/dynorphin+/calbindin+ LGEv Islet1+ cells | [32] | defer |
| CEA MGE-derived Nkx2.1+/SST+ medial cells | [32] | defer (overlaps with `central_amygdala_gabaergic_projection_neuron`) |
| LA-Grp glutamatergic pyramidal (BLA-Rspo2/VGLUT1 type 2) | [6] | consider adding stub or refining parent |
| M2 muscarinic receptor-expressing minor BLA GABAergic type | [14] | defer |

## References

[1] Benavides Ignacio et al. (2025). The medial amygdala's neural circuitry: Insights into social processing and sex differences. *Frontiers in neuroendocrinology*. CorpusId:278095530
[2] Sina Mackay et al. (2024). Concept and location neurons in the human brain provide the 'what' and 'where' in memory formation. *Nature Communications*. CorpusId:272553238
[3] Domiziana Nardelli et al. (2024). Pain in Parkinson's disease: a neuroanatomy-based approach. *Brain Communications*. CorpusId:270614391
[4] Giulia Poggi et al. (2024). Pathophysiology in cortico-amygdala circuits and excessive aversion processing. *Brain Communications*. CorpusId:269255369
[5] Ricardo Raudales et al. (2024). Specific and comprehensive genetic targeting reveals brain-wide distribution and synaptic input patterns of GABAergic axo-axonic interneurons. *eLife*. CorpusId:271240390
[6] Hannah Hochgerner et al. (2023). Neuronal types in the mouse amygdala and their transcriptional response to fear conditioning. *Nature Neuroscience*. CorpusId:264517392
[7] R. Kinkead et al. (2023). Estrogens, age, and neonatal stress. *Frontiers in Physiology*. CorpusId:258718681
[8] Camillo Porcaro et al. (2023). Seeking the Amygdala: Novel Use of Diffusion Tensor Imaging. *Biomedicines*. CorpusId:256859534
[9] Justine Villard et al. (2023). Structural plasticity in the entorhinal and perirhinal cortices following hippocampal lesions in rhesus monkeys. *Hippocampus*. CorpusId:259201574
[10] Alek H. Metwalli et al. (2022). Distinct Subdivisions in the Transition Between Telencephalon and Hypothalamus Produce Otp and Sim1 Cells for the Extended Amygdala in Sauropsids. *Frontiers in Neuroanatomy*. CorpusId:248700803
[11] Loïc J. Chareyron et al. (2021). Life and Death of Immature Neurons in the Juvenile and Adult Primate Amygdala. *International Journal of Molecular Sciences*. CorpusId:235715856
[12] G. Gerlach et al. (2021). Neural pathways of olfactory kin imprinting and kin recognition in zebrafish. *Cell and Tissue Research*. CorpusId:231758452
[13] M. B. Perumal et al. (2021). Inhibitory Circuits in the Basolateral Amygdala in Aversive Learning and Memory. *Frontiers in Neural Circuits*. CorpusId:233450033
[14] V. Vereczki et al. (2021). Total Number and Ratio of GABAergic Neuron Types in the Mouse Lateral and Basal Amygdala. *Journal of Neuroscience*. CorpusId:232283078
[15] Mushfa Yousuf et al. (2021). Functional coupling between CA3 and laterobasal amygdala supports schema dependent memory formation. *NeuroImage*. CorpusId:237541151
[16] E. Garcia-Calero et al. (2020). Histogenetic Radial Models as Aids to Understanding Complex Brain Structures. *Frontiers in Neuroanatomy*. CorpusId:226283312
[17] M. Nolan et al. (2020). Hippocampal and Amygdalar Volume Changes in Major Depressive Disorder. *Chronic Stress*. CorpusId:222092617
[18] Jai S. Polepalli et al. (2020). Diversity of interneurons in the lateral and basal amygdala. *npj Science of Learning*. CorpusId:220930580
[19] Çağrı Temuçin Ünal et al. (2020). Low-threshold spiking interneurons perform feedback inhibition in the lateral amygdala. *Brain Structure and Function*. CorpusId:212579559
[20] Adriana L. Ruiz-Rizzo et al. (2019). Human subsystems of medial temporal lobes extend locally to amygdala nuclei. *bioRxiv*. CorpusId:195404074
[21] S. Sorrells et al. (2019). Immature excitatory neurons develop during adolescence in the human amygdala. *Nature Communications*. CorpusId:195246702
[22] Vassilis Cutsuridis et al. (2017). Memory Processes in Medial Temporal Lobe. *Frontiers in Systems Neuroscience*. CorpusId:2026905
[23] Ying Yang et al. (2017). From Structure to Behavior in Basolateral Amygdala-Hippocampus Circuits. *Frontiers in Neural Circuits*. CorpusId:1397717
[24] Dhananjay Huilgol et al. (2016). Cell migration in the developing rodent olfactory system. *Cellular and Molecular Life Sciences*. CorpusId:9742927
[25] S. Juran et al. (2016). Unilateral Resection of the Anterior Medial Temporal Lobe Impairs Odor Identification. *Frontiers in Psychology*. CorpusId:2088724
[26] A. Loonen et al. (2016). Circuits Regulating Pleasure and Happiness. *Frontiers in Neuroscience*. CorpusId:18703800
[27] A. J. McDonald et al. (2016). Functional Neuroanatomy of Amygdalohippocampal Interconnections. *Journal of Neuroscience Research*. CorpusId:3460849
[28] Alba Vicario et al. (2016). Genoarchitecture of the extended amygdala in zebra finch. *Brain Structure and Function*. CorpusId:11582390
[29] Maxime Carrere et al. (2015). A pavlovian model of the amygdala. *Frontiers in Systems Neuroscience*. CorpusId:14375617
[30] G. Miyoshi et al. (2015). Prox1 Regulates the Subtype-Specific Development of CGE-Derived GABAergic Cortical Interneurons. *Journal of Neuroscience*. CorpusId:8070111
[31] C. Ignacio et al. (2014). Effects of Acute Prenatal Exposure to Ethanol on microRNA Expression. *Frontiers in Pediatrics*. CorpusId:1229611
[32] Alba Vicario et al. (2014). Genetic identification of the central nucleus and other components of the central extended amygdala in chicken during development. *Frontiers in Neuroanatomy*. CorpusId:10856039
[33] David V. Hansen et al. (2013). Non-epithelial stem cells and cortical interneuron production in the human ganglionic eminences. *Nature Neuroscience*. CorpusId:8042525
[34] A. Rubin et al. (2013). PROX1: A Lineage Tracer for Cortical Interneurons. *PLoS ONE*. CorpusId:17126269
[35] P. Veinante et al. (2013). The amygdala between sensation and affect: a role in pain. *Journal of Molecular Psychiatry*. CorpusId:15449738
[36] J. Kiernan (2012). Anatomy of the Temporal Lobe. *Epilepsy Research and Treatment*. CorpusId:5837589
[37] A. J. McDonald et al. (2012). Subpopulations of somatostatin-immunoreactive non-pyramidal neurons in the amygdala project to the basal forebrain. *Frontiers in Neural Circuits*. CorpusId:11544073
[38] A. Woodruff et al. (2007). Networks of Parvalbumin-Positive Interneurons in the Basolateral Amygdala. *Journal of Neuroscience*. CorpusId:161407
[39] A. Preston et al. (2002). Different functions for different medial temporal lobe structures? *Learning & Memory*. CorpusId:16969256
[40] S. Heckers (2000). Neural models of schizophrenia. *Dialogues in Clinical Neuroscience*. CorpusId:5246583
[41] P. Bernier et al. (1998). Bcl-2 Protein as a Marker of Neuronal Immaturity in Postnatal Primate Brain. *Journal of Neuroscience*. CorpusId:15638357
[42] A. Pitkänen et al. (1997). Organization of intra-amygdaloid circuitries in the rat. *Trends in Neurosciences*. CorpusId:10539464
[43] A. Pitkānen et al. (1994). The distribution of GABAergic cells, fibers, and terminals in the monkey amygdaloid complex. *Journal of Neuroscience*. CorpusId:14068807
[44] H. Nishijo et al. (1988). Topographic distribution of modality-specific amygdalar neurons in alert monkey. *Journal of Neuroscience*. CorpusId:18678121

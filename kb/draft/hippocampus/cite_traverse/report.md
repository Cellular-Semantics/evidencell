# Literature Review: Hippocampal GABAergic Interneurons -- Citation Traversal

> **Query:** hippocampal GABAergic interneuron types: soma location, markers, morphology, electrophysiology, transcriptomic correspondence, patch-seq and MERFISH bridging datasets, IS-1/IS-2/IS-3 subtypes, ivy cell vs neurogliaform boundary, hippocampo-septal cell characterisation
> **Node context:** 9 classical hippocampal GABAergic interneuron types (PV basket, CCK basket, axo-axonic, bistratified, OLM, hippocampo-septal, neurogliaform, ivy, IS interneuron)
> **Evidence:** 59 summaries from 38 unique papers
> **Sources:** 48 asta_snippet, 11 europepmc_fulltext, 0 asta_report

## Soma location and laminar identity across types

Multiple papers converge on clear laminar distributions for most of the nine classical types, though a few remain under-documented.

**PV basket cells** reside in stratum pyramidale. They are described as perisomatic-targeting, with axons forming basket-like structures around pyramidal cell somata:

> "basket cells extend their axonal arbor to the stratum pyramidale. In fact, pyramidal neuron somata are contacted extensively by GABAergic synapses from these cells forming characteristic basket-like structures" [26]

Bocchio et al. confirm that PV-expressing basket and bistratified cells are found in the pyramidal layer during in vivo two-photon imaging:

> "the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin" [2]

**CCK basket cells** similarly reside in stratum pyramidale and provide perisomatic inhibition. VGLUT3-positive CCK terminals form axo-somatic synapses:

> "VGLUT3-immunogold puncta were present over synaptic vesicle clusters in axon terminals forming axo-somatic symmetrical synapses" [19]

> "CCK positive basket cells target the soma and proximal dendrites of cortical and hippocampal pyramidal cells, and do not appear to innervate the AIS" [15]

**Axo-axonic (chandelier) cells** share the PV+ fast-spiking profile and reside in stratum pyramidale, targeting the axon initial segment. Their soma location is grouped with PV basket cells in the transcriptomic literature [5, 11].

**Bistratified cells** have somata in stratum oriens, close to the pyramidal layer. Chamberland et al. (2024) show that Sst;;Tac1-INs (bistratified cells) are positioned closer to the pyramidal layer than OLM cells:

> "While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A" [3]

> "Sst;;Tac1-INs strongly targeted strata oriens and radiatum, a bilaminar morphology reminiscent of classically defined bistratified INs" [3]

The subcellular sequencing study also places basket-bistratified cell somata in stratum pyramidale:

> "The hippocampal cells they most resemble, Basket-bistratified, HS and OLM interneurons, have their somata in the stratum pyramidale (sp) of the hippocampus" [13]

**OLM cells** are the most consistently documented: fusiform somata in stratum oriens of CA1, with horizontally oriented dendrites and axons projecting to stratum lacunosum-moleculare.

> "All cells had a fusiform cell soma residing in stratum oriens of hippocampal CA1 with horizontally spanning dendritic branches. Their axon frequently originated from a primary dendrite and projected towards the stratum lacunosum moleculare" [16]

> "Tomato+ cells in the hippocampus were almost exclusively located in the SO of CA1 and subiculum" [31]

> "these CA1 GABAergic, somatostatin (Som)-expressing interneurons are named for their distinctive morphology: their soma and dendritic trees are located in the stratum oriens and their axons extend directly out to arborize in the stratum lacunosum-moleculare" [18]

> "Type I interneurons had large horizontally oriented cell somata located at the border of stratum oriens and the alveus" [38]

**Hippocampo-septal cells** share the stratum oriens soma location with OLM cells:

> "GABAergic neurons in the hippocampus, which project to the medial septum, are located in the stratum oriens of the hippocampus" [20]

**Neurogliaform cells** are most dense in stratum lacunosum-moleculare:

> "mClover-GluN3A labeled cells co-expressed Sst in stratum oriens and neuronal nitric oxide synthase (nNOS) in putative NGFCs that comprise the dominant interneuron subtype in stratum lacunosum moleculare" [1]

The subcellular sequencing study locates neurogliaform somata at the sr/slm border:

> "their transcriptomes were closest to RLMb and Neuroglialform interneurons whose somata are located at the border between the stratum radiatum (sr) and the slm and exhibit short dendrites" [13]

**Ivy cells** have somata in stratum pyramidale, with extensive axonal arborizations spanning multiple layers. Bezaire et al. note that new morphological data had to be collected for ivy and neurogliaform cells:

> "As there were no data available for ivy and neurogliaform cells, we performed the necessary experiments in our lab by filling ivy and neurogliaform cells in hippocampal CA1 slices from Wistar rats and then measuring their somatic area and dendrites" [22]

The Tzilivaki review describes ivy cells as the most common interneuron type in CA1:

> "Lamp5 interneurons include ivy and neurogliaform cells (NGFCs). The ivy cell is the most common interneuron type in CA1; it has a distinct morphology with a relatively extensive axonal cloud extending over several hippocampal layers and co-expresses neuronal nitric oxide synthase (nNOS)" [5]

**IS interneurons** have somata in stratum pyramidale or radiatum. IS3 cells specifically:

> "The somas of these cells are located in the stratum pyramidale (PYR) or radiatum (RAD) and send their axons to the oriens-alveus (O/A) to contact other interneurons located in this area, preferentially metabotropic glutamate receptor 1a (mGluR1a)-positive oriens-lacunosum moleculare interneurons (OLMs)" [28]

## Molecular markers, neuropeptides, and marker conflicts (P4)

**PV+ interneuron transcriptomic continuity.** A key finding from the patch-seq literature is that PV+ interneurons (basket, axo-axonic, bistratified) show remarkably high transcriptomic similarity despite profound morphological and functional divergence:

> "we find high transcriptomic similarity among PV-INs, with few genes showing divergent expression between morphologically different types" [11]

> "while PV-INs differ in anatomy and in vivo activity, their continuous transcriptomic and homogenous biophysical landscapes are not predictive of these distinct identities" [11]

This is a critical conflict for the KB: PV basket cells and axo-axonic cells cannot be distinguished transcriptomically despite being functionally separable.

**Tac1 as bistratified cell marker.** The Sst;;Tac1 intersectional strategy marks bistratified cells:

> "the bistratified and oriens-oriens categories were disproportionately and almost exclusively represented by Sst;;Tac1-INs (n = 13/25) and Sst;;Nos1-INs (n = 12/15), respectively" [3]

> "the Sst;;Tac1 intersection revealed a population of bistratified INs that preferentially synapsed onto fast-spiking interneurons (FS-INs) and were both necessary and sufficient to interrupt their firing" [7]

**SOM+PV co-expression.** Bistratified and OLM cells have been reported to co-express SOM and PV [asta_snippet, 5]:

> "These two interneuron types have been reported to co-express SOM and PV" [5]

This is flagged as a potential conflict for PV basket cell nodes, as the PV marker is traditionally considered exclusive to fast-spiking perisomatic cells.

**Ndnf;;Nkx2-1 for OLM cells.** The intersectional approach identifies OLM cells through Ndnf;;Nkx2-1:

> "the Ndnf;;Nkx2-1 intersection identified a population of oriens lacunosum-moleculare (OLM) INs that predominantly targeted CA1 pyramidal neurons, avoiding FS-INs" [7]

**Chrna2 as specific OLM marker.** Multiple papers confirm Chrna2 specificity:

> "the nicotinic acetylcholine receptor Chrna2 was identified as a specific genetic marker for CA1 OLM interneurons" [18]

> "the vast majority (95.1%, 214/225 cells) of Tomato+ cells were also som+ and comprised a subpopulation (35.2%, 214/608) of CA1 som+ interneurons" [31]

**Unexpected Npy in OLM cells.** Patch-seq of OLM interneurons revealed consistent Npy expression:

> "we found a surprisingly consistent expression of Npy in OLMs, which was previously not associated with the identity of this type" [16]

**CCK basket cell markers.** VGLUT3, CB1 (Cnr1), and CCK define the population:

> "VGLUT3 is expressed by CCK-positive and more rarely by calbindin-positive interneurons" [19]

> "Proportions of CCK basket cells express the ionotropic serotonin receptor (5-HT3) and the metabotropic Cannabinoid receptor type 1 (CB1), which modulate GABA release from the presynaptic terminal" [15]

CCK+ interneurons in str. radiatum also co-express Eps8 and calbindin [asta_snippet, 27]:

> "all Eps8-expressing cells were positive for calbindin" [27]

**Comprehensive marker taxonomy.** CA1 contains >21 interneuron types classified by traditional molecular markers:

> "GABAergic INs have been traditionally categorized as parvalbumin (PV), vasoactive intestinal peptide (VIP), cholecystokinin (CCK), somatostatin (SST), neuropeptide Y (NPY), and neuron-derived neurotrophic factor (NDNF) and/or nitric oxide synthase (nNOS), among others" [6]

## Electrophysiology

**Fast-spiking PV+ cells.** Both basket and axo-axonic cells display fast-spiking responses:

> "Both display FS responses to depolarizing input and fire at high rates in vivo. In contrast, SOM cells typically have lower firing rates despite their low firing threshold" [5]

Wild-type PV+ interneurons comprise 80% fast-spiking and 20% non-fast-spiking subtypes [PMC fulltext, 14]:

> "WT PV+INTs consist of two physiological subtypes (80% fast-spiking (FS), 20% non-fast-spiking (NFS)) and four morphological subtypes" [14]

**Basket vs bistratified feedforward inhibition.** A key functional distinction separates perisomatic basket cells (fast-spiking) from dendritic bistratified cells (regular-spiking):

> "FFI in CA1PCs is mediated by two physiologically and morphologically distinct GABAergic interneurons: fast-spiking, perisomatic-targeting basket cells and regular-spiking, dendritic-targeting bistratified cells" [24]

> "Separate FFI by basket and bistratified respectively modulated CA1PC threshold and gain" [24]

**CCK+ interneuron firing diversity.** Two distinct firing phenotypes exist within CCK+ interneurons in CA3, determined by alternative splicing rather than gene expression differences:

> "Two firing phenotypes of CCK+INs in rat hippocampal CA3 area; either possessing a previously undetected membrane potential-dependent firing or regular firing phenotype, due to different low-voltage-activated potassium currents" [17]

> "the firing phenotypes were correlated with the presence of distinct isoforms of Kv4 auxiliary subunits (KChIP1 vs. KChIP4e and DPP6S)" [17]

**Late-spiking in Ivy and NGC.** Both ivy cells and neurogliaform cells exhibit late-spiking (LS) phenotype:

> "both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR" [35]

**Stratum oriens heterogeneity.** Within stratum oriens, LTH cells (strong spike frequency adaptation, high Ih) are a putative new cell type distinct from OLM cells:

> "Strong and weak SFA cells were labeled in hippocampal slices from SST:cre Ai14 mice suggesting both cells express somatostatin" [10]

## Transcriptomic bridging and multimodal datasets (P2)

Several studies bridge classical morpho-physiological cell types to transcriptomic identities, though a complete one-to-one mapping remains elusive.

**Patch-seq of PV interneurons.** Que et al. (2021) applied patch-seq to morphologically identified PV+ cells in CA1, finding transcriptomic continuity across basket, axo-axonic, and bistratified morphologies [11]. The uniform CAM profile suggests that wiring specificity is not transcriptomically encoded in mature PV cells:

> "PV-INs show a uniform synaptic cell adhesion molecule (CAM) profile, suggesting that CAM expression in mature PV cells does not reflect wiring specificity after development" [11]

**Patch-seq of OLM cells.** Winterer et al. (2019) performed single-cell RNA-seq on anatomically identified OLM interneurons in Htr3a-Cre and Sst-Cre mouse lines, finding a highly homogeneous transcriptomic population:

> "OLMs constitute a highly homogenous transcriptomic population" [16]

**Patch-seq of CCK+ interneurons.** Fuzik et al. (2015) developed the patch-seq approach using CCK+ interneurons as a model system:

> "We focused on cholecystokinin (CCK)-containing(+) GABAergic interneurons because their morphological and molecular features are thought to form a quasi-continuum from axon- to dendrite-targeting interneurons" [23]

**Multi-institute scRNA-seq atlas.** Kim et al. (2025) integrated 86,852 GABAergic interneuron transcriptomes across multiple datasets, establishing canonical marker combinations for subtype annotation:

> "The Neurogliaform interneurons that are Lhx6 + /Lamp5 + /Id2 + are annotated as MGE-derived (NGFC.M); and those that are Lhx6 - /Lamp5 + /Id2 + /Ndnf + are annotated as CGE-derived (NGFC.C)" [1]

**Intersectional Cre/Flp genetics.** Chamberland et al. (2024) used combinatorial Cre/Flp mouse models to dissect SST-IN subtypes. The Sst;;Tac1 intersection isolates bistratified cells; the Ndnf;;Nkx2-1 intersection isolates OLM cells; the Sst;;Nos1 intersection isolates oriens-oriens cells [3, 7].

**Transcriptomic taxonomy gap.** Despite 100+ transcriptomic types described, functional mapping remains incomplete:

> "recent single-cell transcriptomic datasets have led to a more extensive taxonomy of hippocampal interneurons, with up to 100 types having been described, the functional significance of these transcriptomic types remains mostly uninvestigated" [5]

> "there is still much work to be done to determine how these transcriptomic cell types relate to the more traditional classifications such as morphological or molecular markers" [5]

No MERFISH bridging dataset was identified in this traversal. The multimodal bridging evidence is dominated by patch-seq (Que et al. for PV-INs, Winterer et al. for OLMs, Fuzik et al. for CCK+) and intersectional genetics (Chamberland et al. for SST subtypes).

## Subtype splitting and boundary cases (P3)

### IS-1/IS-2/IS-3 subtypes

Three IS interneuron subtypes were originally identified in rat hippocampus and confirmed in human:

> "a combination of immunohistochemistry and anatomical analysis identified three distinct subtypes of IS interneurons in the rat hippocampus" [32]

> "the hippocampus and the superficial cortical layers (layers 1-3) may be the only cortical regions that possess such a highly specialized population of GABAergic cells" [32]

**IS3 cells** are the best characterised: VIP+/CR+ co-expression, soma in PYR/RAD, axon to O/A, preferential innervation of OLM cells. They are functionally disinhibitory:

> "type 3 IS (IS3) cells that coexpress the vasoactive intestinal polypeptide (VIP) and calretinin contact several distinct types of interneurons within the hippocampal CA1 stratum oriens/alveus (O/A), with preferential innervation of oriens-lacunosum moleculare cells (OLMs) through dendritic synapses" [28]

> "IS3 cells in the mouse hippocampus were similar to those described originally in the rat hippocampus. These cells innervated heavily the O/A border" [28]

> "Their dendritic arbors were often unipolar (47% of cells), suggesting that these cells are preferentially recruited through the activation of the Schaffer collaterals" [28]

**IS1 cells** (CR+) are more heterogeneous. They have multipolar dendrites, axons in RAD/PYR, and form dendro-dendritically connected clusters:

> "One group of CR-positive cells had a cell body located within the O/A, PYR, or RAD; a multipolar dendritic tree; and a widely projecting axon that mostly occupied the CA1 RAD and PYR" [28]

> "In several cases (n = 5 slices/2 animals), the dendrites of 2-3 CR-positive cells of this subtype were found to form dendro-dendritically connected clusters (Fig. 6C1, top inset), which is a hallmark of the type I interneuron-specific (IS1) interneuron described previously in the rat CA1 hippocampus" [28]

> "This subtype of IS cells exhibited a remarkable anatomical diversity, with cell bodies that occupied different layers and an axon that projected mostly within the RAD and PYR. Similar to IS3 cells, IS1 cells exhibited a high input resistance but were more heterogeneous in terms of firing properties. Therefore, more than one subtype of putative IS1 cells is likely to be found within this group of CR-positive interneurons." [28]

**IS2 cells** received no direct characterisation in this traversal. The IS-2 subtype is the least documented of the three.

### Ivy cell vs neurogliaform cell boundary

This is one of the most informative findings of the traversal. Tricoire et al. (2010) provide definitive lineage evidence:

> "IvCs and nNOS+ NGCs have completely overlapping developmental, electrophysiological, morphological, and neurochemical properties, suggesting that these cells constitute a single unique interneuron subtype despite differences in laminar organization" [35]

> "classically defined NGCs can be subdivided into two groups based on nNOS expression and lineage with nNOS+ NGCs being derived from the MGE and nNOS- NGCs arising from CGE progenitors" [35]

The key boundary is therefore not IvC vs NGC (a laminar distinction), but rather nNOS+ (MGE-derived, Lamp5+/Lhx6+) vs nNOS- (CGE-derived, Lamp5+/Lhx6-/Ndnf+):

> "Amongst NGFCs Grin3a is expressed in both Lamp5+/Lhx6+ MGE-derived subsets, also known as Ivy cells (IvyCs), and Lamp5+/Lhx6- caudal ganglionic eminence (CGE)-derived subsets" [1]

In hippocampus specifically, the MGE-derived (nNOS+) subset is the majority, contrasting with neocortex:

> "we found that the nNOS+ subset, hence MGE derived, represents the majority of all hippocampal NGCs with a minor contribution from CGE-derived NGCs. This contrasts with findings in the neocortex in which fate-mapping evidence supports a dominant CGE origin for NGCs" [35]

The nNOS marker segregation from PV and SOM populations is also confirmed:

> "in the hippocampus, the neuronal isoform of nitric oxide synthase (nNOS) is expressed in an interneuron subpopulation that does not overlap with PV or SOM interneurons and also largely segregates from CR interneurons" [35]

> "nNOS strongly colocalizes with neuropeptide Y in both Ivy cells (IvCs) and a subset of neurogliaform cells (NGCs)" [35]

CGE-derived NPY+/GAD65+ cells in CA1 include both ivy and neurogliaform morphologies [asta_snippet, 33]:

> "The labeled cell types correspond well to previously described NPY-positive multipolar cells, often referred to as Ivy cells and neurogliaform cells" [33]

## Hippocampo-septal cell characterisation (P5)

Evidence for hippocampo-septal (HS) cells comes from a small number of sources. Takacs et al. (2024) provide the most detailed comparison with OLM cells:

> "Two main types of SOM-containing cells in area CA1 of the hippocampus are oriens-lacunosum-moleculare (OLM) cells and hippocampo-septal (HS) cells" [4]

> "These cell types show many similarities in their soma-dendritic architecture, but they have different axonal targets, display different activity patterns in vivo and are thought to have distinct network functions" [4]

> "we estimated that an OLM cell receives about 8400, whereas an HS cell about 15600 synaptic inputs, about 16% of which are GABAergic" [4]

HS cells are part of a diverse population of long-range SOM-expressing GABAergic neurons:

> "In the rat hippocampal CA1 area, at least five distinct types of SOM-expressing GABAergic neuron have been defined" [21]

> "In addition to these exclusively locally terminating SOM-expressing interneurons, a diverse population of long-range SOM-expressing GABAergic neurons send projections to the medial septum and/or retrohippocampal cortical areas" [21]

The septo-hippocampal reciprocal circuit is well established:

> "they form a reciprocal long-range GABAergic septo-hippocampal circuit. Many long-range GABAergic neurons simultaneously form local synapses in CA1 and en passant synapses in several remote areas" [20]

> "The long-range projecting axons of the GABAergic neurons are highly myelinated, which argues for a specific role in the immediate synchronization and functional binding of remote areas" [20]

However, HS cell characterisation remains thin: no patch-seq data, no specific Cre line, and molecular markers (Sst+/mGluR1a+/CB-/nNOS+) come from the original rat literature rather than from modern multimodal studies.

## Evidence gaps for hippocampal GABAergic interneurons

- **defining_markers:** partial -- well established for PV basket (Pvalb), CCK basket (Cck/Cnr1/Vglut3), OLM (Sst/Chrna2), neurogliaform (Ndnf/nNOS/NPY), ivy (nNOS/NPY/Lamp5/Lhx6); weaker for axo-axonic (Pvalb only, not distinguishable from basket transcriptomically), bistratified (Sst/Tac1 from one study), hippocampo-septal (Sst only, no specific marker), IS subtypes (VIP/CR co-expression, insufficient for IS1 vs IS2 vs IS3)
- **anatomical_location:** partial -- well documented for OLM, PV basket, CCK basket; hippocampo-septal confirmed in str. oriens but less detail; ivy cell soma in str. pyramidale needs more primary sources; IS-2 soma location absent
- **nt_type:** yes -- all nine types confirmed GABAergic; CCK basket cells additionally have VGLUT3 co-transmission capacity
- **electrophysiology_class:** partial -- fast-spiking for PV basket and axo-axonic; regular-spiking for bistratified (one source); late-spiking for ivy and NGC; IS subtypes poorly characterised electrophysiologically; HS cell electrophysiology not covered in this traversal
- **morphology_notes:** partial -- well described for OLM, PV basket, CCK basket, bistratified, IS3; ivy cell "extensive axonal cloud" is qualitative only; NGC "dense local axon" described; IS1 and IS2 morphology sparse; HS cell morphology described as "similar soma-dendritic architecture" to OLM but with different axonal targets

**Specific evidence gaps by type:**
- Axo-axonic cell: no transcriptomic distinguisher from PV basket; no specific Cre line
- Hippocampo-septal cell: no patch-seq, no specific Cre line, no modern multimodal data
- IS-2 interneuron: essentially absent from this traversal; no soma location, no electrophysiology, no molecular profile beyond the original rat description
- Bistratified cell: Tac1 marker from one study (Chamberland et al.); no independent replication yet
- No MERFISH or spatial transcriptomics datasets were identified bridging classical types to atlas clusters

## New classical types encountered

1. **Oriens-oriens (O-O) cell** -- Sst;;Nos1 intersection; axon confined to stratum oriens; distinct from OLM and bistratified. Key paper: Chamberland et al. (2024) [3]. Suggested action: **add stub** -- appears to be a genuine distinct type with specific molecular identity (Sst+/Nos1+).

2. **R-LM and P-LM cells** -- Novel SST+ interneuron subtypes identified in GIN mice with axons in radiatum-lacunosum moleculare and pyramidale-lacunosum moleculare respectively. Key paper: Oliva et al. (2000) [37]. Suggested action: **defer** -- described in one early study using transgenic labelling; unclear how they map to modern taxonomy.

3. **LTH cell** (stratum oriens) -- SST+ cell with strong spike frequency adaptation and high Ih, distinct from OLM cells based on physiological clustering. Key paper: Hewitt et al. (2021) [10]. Suggested action: **defer** -- single study, may overlap with oriens-oriens or other SST+ subtypes.

4. **Trilaminar cell** -- Long-range projecting GABAergic cell with unique high-frequency burst firing, distinguished from HS and other SOM+ projection neurons. Key paper: Katona et al. (2017) [21]. Suggested action: **add stub** -- well-documented in the Somogyi lab literature as a distinct projection cell type.

5. **VIP basket cell** -- VIP+ perisomatic-targeting cell distinct from IS interneurons; provides perisomatic inhibition to pyramidal neurons with asynchronous GABA release. Key paper: Tyan et al. (2014) [28]. Suggested action: **add stub** -- functionally distinct from IS cells despite shared VIP expression.

## References

[1] Kim JH et al. (2025). Discrete interneuron subsets participate in GluN1/GluN3A excitatory glycine receptor (eGlyR)-mediated regulation of hippocampal network activity throughout development and evolution. *bioRxiv*. CorpusId:282312227

[2] Bocchio M et al. (2024). Functional networks of inhibitory neurons orchestrate synchrony in the hippocampus. *bioRxiv*. CorpusId:262127573

[3] Chamberland S et al. (2024). Functional specialization of hippocampal somatostatin-expressing interneurons. *Proceedings of the National Academy of Sciences of the United States of America*. CorpusId:269246896

[4] Takacs VT et al. (2024). Synaptic and dendritic architecture of different types of hippocampal somatostatin interneurons. *bioRxiv*. CorpusId:258744074

[5] Tzilivaki A et al. (2023). Hippocampal GABAergic interneurons and memory. *Neuron*. CorpusId:259953057

[6] Hernandez-Frausto M et al. (2023). Local and long-range GABAergic circuits in hippocampal area CA1 and their link to Alzheimer's disease. *Frontiers in Neural Circuits*. CorpusId:263277661

[7] Chamberland S et al. (2023). Functional specialization of hippocampal somatostatin-expressing interneurons. *bioRxiv*. CorpusId:258397933

[8] Degro C et al. (2022). Interneuron diversity in the rat dentate gyrus: An unbiased in vitro classification. *Hippocampus*. CorpusId:246866323

[9] Perrenoud Q et al. (2022). Molecular and electrophysiological features of GABAergic neurons in the dentate gyrus reveal limited homology with cortical interneurons. *PLoS ONE*. CorpusId:250387238

[10] Hewitt L et al. (2021). High and low expression of the hyperpolarization activated current (Ih) in mouse CA1 stratum oriens interneurons. *Physiological Reports*. CorpusId:234597703

[11] Que L et al. (2021). Transcriptional and morphological profiling of parvalbumin interneuron subpopulations in the mouse hippocampus. *Nature Communications*. CorpusId:230508306

[12] Tecuatl C et al. (2020). Comprehensive Estimates of Potential Synaptic Connections in Local Circuits of the Rodent Hippocampal Formation by Axonal-Dendritic Overlap. *Journal of Neuroscience*. CorpusId:229694907

[13] Perez JD et al. (2020). Subcellular sequencing of single neurons reveals the dendritic transcriptome of GABAergic interneurons. *bioRxiv*. CorpusId:224817966

[14] Ekins TG et al. (2020). Emergence of non-canonical parvalbumin-containing interneurons in hippocampus of a murine model of type I lissencephaly. *bioRxiv*. CorpusId:221276443

[15] Contreras A et al. (2019). Molecular Specialization of GABAergic Synapses on the Soma and Axon in Cortical and Hippocampal Circuit Function and Dysfunction. *Frontiers in Molecular Neuroscience*. CorpusId:195584607

[16] Winterer J et al. (2019). Single-cell RNA-Seq characterization of anatomically identified OLM interneurons in different transgenic mouse lines. *European Journal of Neuroscience*. CorpusId:201041756

[17] Olah V et al. (2019). Functional specification of CCK+ interneurons by alternative isoforms of Kv4.3 auxiliary subunits. *bioRxiv*. CorpusId:198237048

[18] Nichol H et al. (2018). Electrophysiological and Morphological Characterization of Chrna2 Cells in the Subiculum and CA1 of the Hippocampus: An Optogenetic Investigation. *Frontiers in Cellular Neuroscience*. CorpusId:3591966

[19] Fasano C et al. (2017). Regulation of the Hippocampal Network by VGLUT3-Positive CCK-GABAergic Basket Cells. *Frontiers in Cellular Neuroscience*. CorpusId:13529065

[20] Muller C et al. (2017). Septo-hippocampal interaction. *Cell and Tissue Research*. CorpusId:21358766

[21] Katona L et al. (2017). Behavior-dependent activity patterns of GABAergic long-range projecting neurons in the rat hippocampus. *Hippocampus*. CorpusId:4934764

[22] Bezaire M et al. (2016). Interneuronal mechanisms of hippocampal theta oscillations in a full-scale model of the rodent CA1 circuit. *eLife*. CorpusId:4776309

[23] Fuzik J et al. (2015). Integration of electrophysiological recordings with single-cell RNA-seq data identifies novel neuronal subtypes. *Nature Biotechnology*. CorpusId:7738817

[24] Ferrante M et al. (2015). Distinct and synergistic feedforward inhibition of pyramidal cells by basket and bistratified interneurons. *Frontiers in Cellular Neuroscience*. CorpusId:15824759

[25] Whissell P et al. (2015). Comparative density of CCK- and PV-GABA cells within the cortex and hippocampus. *Frontiers in Neuroanatomy*. CorpusId:16859318

[26] Muller C et al. (2014). Dendritic inhibition mediated by O-LM and bistratified interneurons in the hippocampus. *Frontiers in Synaptic Neuroscience*. CorpusId:8248396

[27] Huang CC et al. (2014). Cell type-specific expression of Eps8 in the mouse hippocampus. *BMC Neuroscience*. CorpusId:10835885

[28] Tyan L et al. (2014). Dendritic Inhibition Provided by Interneuron-Specific Cells Controls the Firing Rate and Timing of the Hippocampal Feedback Inhibitory Circuitry. *Journal of Neuroscience*. CorpusId:23480858

[29] Molgaard S et al. (2014). Immunofluorescent visualization of mouse interneuron subtypes. *F1000Research*. CorpusId:10261984

[30] Hosp J et al. (2013). Morpho-physiological Criteria Divide Dentate Gyrus Interneurons into Classes. *Hippocampus*. CorpusId:14371295

[31] Leao R et al. (2012). OLM interneurons differentially modulate CA3 and entorhinal inputs to hippocampal CA1 neurons. *Nature Neuroscience*. CorpusId:7952877

[32] Chamberland S et al. (2012). Inhibitory control of hippocampal inhibitory neurons. *Frontiers in Neuroscience*. CorpusId:8530661

[33] Wierenga C et al. (2010). Molecular and Electrophysiological Characterization of GFP-Expressing CA1 Interneurons in GAD65-GFP Mice. *PLoS ONE*. CorpusId:8617990

[34] Weng J et al. (2010). Cell Type-Specific Expression of Acid-Sensing Ion Channels in Hippocampal Interneurons. *Journal of Neuroscience*. CorpusId:14052756

[35] Tricoire L et al. (2010). Common Origins of Hippocampal Ivy and Nitric Oxide Synthase Expressing Neurogliaform Cells. *Journal of Neuroscience*. CorpusId:2405079

[36] Oren I et al. (2009). Role of Ionotropic Glutamate Receptors in Long-Term Potentiation in Rat Hippocampal CA1 Oriens-Lacunosum Moleculare Interneurons. *Journal of Neuroscience*. CorpusId:1015389

[37] Oliva A et al. (2000). Novel Hippocampal Interneuronal Subtypes Identified Using Transgenic Mice That Express Green Fluorescent Protein in GABAergic Interneurons. *Journal of Neuroscience*. CorpusId:13398453

[38] van Hooft JA et al. (2000). Differential Expression of Group I Metabotropic Glutamate Receptors in Functionally Distinct Hippocampal Interneurons. *Journal of Neuroscience*. CorpusId:6652630

# CL new term request: hippocampal trilaminar cell

*Drafted from `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml` node `trilaminar_cell_hippocampus` on 2026-09-11.*
*No existing CL term covers this cell type; no `cl_mapping` is asserted on the source node. Proposed parents are given below.*

**Preferred term label**
hippocampal trilaminar cell

**Synonyms** (with reference where available)
- trilaminar cell (exact) — Sik et al., 1995, PMID:7472426
- CA1 trilaminar cell (exact)
- mGluR8a-innervated GABAergic trilaminar cell (related) — Katona et al., 2020, PMID:32016558

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A GABAergic interneuron with soma at the stratum oriens/alveus border of hippocampal CA1, whose dendrites remain largely confined to stratum oriens while its local axon distributes across strata oriens, pyramidale and radiatum — the arrangement for which the type is named — and which additionally projects to the subiculum (Sik et al., 1995, PMID:7472426; Ferraguti et al., 2005, PMID:16280590). It expresses a high level of somato-dendritic muscarinic M2 acetylcholine receptor and lacks somatostatin, parvalbumin, vasoactive intestinal peptide, neuropeptide Y and calbindin (Katona et al., 2020, PMID:32016558). Its presynaptic inputs are unusually densely decorated with mGluR8a-containing terminals (PMID:16280590; PMID:32016558). Output synapses are strongly biased toward other interneurons, including parvalbumin-expressing cells, while also contacting pyramidal cell somata (PMID:32016558). Firing falls during movement and rises in prolonged bursts above 200 Hz during slow-wave sleep (PMID:32016558).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
Two parents are proposed, since neither alone captures both the anatomical and the neurotransmitter classification:
- hippocampal interneuron (CL:1001569) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCL_1001569
- GABAergic interneuron (CL:0011005) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCL_0011005

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
CA1 stratum oriens (UBERON:0014552) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0014552

**Your ORCID**
0000-0002-5507-2103

**Additional notes or concerns**

*Nomenclature — please read before assigning a label.* The term "trilaminar cell" has been applied to at least three different things in the hippocampal literature, and this request concerns only one of them. Ferraguti et al. (2005, PMID:16280590), following Somogyi et al. (2005), explicitly proposed that the name be reserved for the cell type described by Sik et al. (1995, PMID:7472426) "and not to other different cells that have axons in three layers"; this request follows that stipulation. Two usages must not be conflated with it: (i) Slomianka et al. (2011, PMID:21597968) record that a deep CA1 *pyramidal* cell subpopulation expressing Ctip2, Sox5, muscarinic M1 receptor, somatostatin and neuropeptide Y has also been termed "trilaminar cells" — that population is glutamatergic and is not this cell type; (ii) "radial trilaminar cells," with dendrites perpendicular rather than horizontal to the pyramidal layer, may be a morphological variant of this type or a separate entity (Booker & Vida, 2018, PMID:30084021). Separately, "trilaminar complex" is used in the avian literature for a *brain region*, not a cell type (Meskenaite et al., 2016, PMID:27445724), and is unrelated.

*Distinguishing from the closest existing and candidate types.* The most similar characterised GABAergic type is the M2-positive VIP long-range projecting (VIP-LRP, Type I) cell of Francavilla et al. (2018, PMID:30487571). It shares soma position at the oriens/alveus border, horizontally oriented dendrites, somatostatin-negativity and mGluR8a-positive inputs. Katona et al. (2020, PMID:32016558) separate the two by this cell type's lack of VIP, neuropeptide Y and calbindin in the soma, by the much higher density of its mGluR8a-positive input decoration, and by the three-layer local axon distribution (VIP-LRP local collaterals concentrate in stratum oriens/alveus with only a small proportion entering strata pyramidale and radiatum). Against somatostatin-positive long-range projecting oriens cells — including the existing CL:4023121 `sst chodl GABAergic interneuron` — the decisive feature is somatostatin-negativity (Jinno et al., 2007, PMID:17699661; PMID:32016558), so CL:4023121 is not a suitable parent.

*A useful physiological discriminator.* Unlike several other CA1 stratum oriens interneurons, including OLM cells, this type reportedly does not show a sag and rebound response to hyperpolarisation (Hewitt et al., 2021, PMID:33991454, citing Gloveli et al., 2005).

*Regional extent.* The type is defined in CA1, which is where all the morphologically identified cells have been recovered. Katona et al. (2020, PMID:32016558) additionally report GABAergic neurons carrying the molecular features of this type in both CA1 and CA3, in rat and mouse. The proposed soma-location axiom is therefore restricted to CA1, and CA3 occurrence is noted here rather than asserted.

*Markers that cannot be axiomatised.* The negative markers (somatostatin, parvalbumin, VIP, neuropeptide Y, calbindin) are cytosolic or secreted rather than plasma-membrane proteins, so `lacks_plasma_membrane_part` is not appropriate and they are stated in the definition text only. The dense mGluR8a decoration is likewise a property of the *presynaptic terminals innervating* this cell, not of its own expression, and so is described but not axiomatised.

*Candidate transcriptomic correspondence.* Katona et al. (2020, PMID:32016558) note that single-cell RNA-seq of mouse CA1 reveals an isolated cluster of CGE-derived stratum oriens neurons lacking Sst and Pvalb and expressing Chrm2 and Ntng1 — the `Ntng1.Chrm2` class of Harris et al. (2017, PMID:29912866; see also Qian et al., 2018, DOI:10.1101/431957) — with a molecular profile similar to that of this cell type. In our own annotation transfer of the Harris et al. dataset (GEO:GSE99888) onto the Allen Whole Mouse Brain taxonomy CCN20230722, the `Ntng1.Chrm2` class corresponds to supertype `0198 RHP-COA Ndnf Gaba_6` at F1 = 0.96 (n = 66; group purity 0.96, target purity 0.97) and to cluster `0704 RHP-COA Ndnf Gaba_6` at F1 = 0.97, and is assigned at class level to `06 CTX-CGE GABA` with 0.99 purity — independently consistent with the CGE origin reported for the cluster. We flag two caveats: the identification of this transcriptomic cluster with the morphologically defined cell type is an inference by Katona et al. from shared marker profile, not a measurement on morphologically identified cells (no patch-seq or otherwise morphologically anchored transcriptome of this type has been published); and the Allen subclass label is retrohippocampal/cortical-amygdalar whereas the source cells are CA1 by dissection. We therefore do not propose a transcriptomic-taxonomy cross-reference as part of this term, and mention the correspondence only as supporting context and as a target for future validation.

*Requested editor input.* We could not resolve a PRO identifier for the muscarinic M2 acetylcholine receptor (CHRM2) protein to complete the `expresses` axiom below, and would welcome the correct ID.

Proposed logical axioms:
- subClassOf 'hippocampal interneuron' (CL:1001569)
- subClassOf 'GABAergic interneuron' (CL:0011005)
- subClassOf 'has soma location' (RO:0002100) some 'CA1 stratum oriens' (UBERON:0014552)
- subClassOf 'sends synaptic output to region' (RO:0013003) some 'CA1 stratum oriens' (UBERON:0014552)
- subClassOf 'sends synaptic output to region' (RO:0013003) some 'pyramidal layer of CA1' (UBERON:0014548)
- subClassOf 'sends synaptic output to region' (RO:0013003) some 'CA1 stratum radiatum' (UBERON:0014554)
- subClassOf 'sends synaptic output to region' (RO:0013003) some 'subiculum' (UBERON:0002191)
- subClassOf 'capable of' (RO:0002215) some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534)
- subClassOf 'expresses' some 'netrin-G1' (PR:000011467) — tentative; rests on the candidate transcriptomic correspondence discussed above, and may be better omitted until that link is confirmed
- subClassOf 'expresses' some muscarinic M2 acetylcholine receptor (CHRM2) — PRO ID required

Not asserted, deliberately:
- No parvalbumin `expresses` axiom. Parvalbumin appears in this literature as a marker of this cell type's postsynaptic *targets* (PMID:32016558), and the associated transcriptomic cluster is explicitly Pvalb-negative.
- No output axiom to the medial septum. The literature is inconsistent on direction: Ferraguti et al. (2005, PMID:16280590) refer to "their septal projection," and Slomianka et al. (2011, PMID:21597968) review reports of projections to septum, olfactory bulb and hypothalamus, whereas Katona et al. (2020, PMID:32016558) report that these cells *receive* mGluR8a-enriched GABAergic input *from* the medial septum. The CA1-to-subiculum projection is the well-established one and is the only long-range output asserted here.

Key references:
- Sik et al. 1995 — PMID:7472426 — supports: original definition; dendrites confined to stratum oriens with axon collaterals in strata radiatum, oriens and pyramidale; symmetric (inhibitory) synapses onto targets; early EPSP-IPSP-late depolarising response to commissural stimulation (in vivo intracellular labelling, rat CA1)
- Ferraguti et al. 2005 — PMID:16280590 — supports: soma at CA1 oriens/alveus border; strong somato-dendritic M2 receptor; dense mGluR8-positive input decoration; extensive projection to subiculum; preferential innervation of interneurons alongside pyramidal cell somata and dendrites; complex spike bursts during theta and strong discharge during sharp wave/ripple events; nomenclature stipulation (in vivo recording and labelling plus immunohistochemistry, rat)
- Katona et al. 2020 — PMID:32016558 — supports: high somato-dendritic M2; somatostatin-negativity; absence of VIP, neuropeptide Y and calbindin; mGluR8a-enriched inputs including from medial septum; electron-microscopic demonstration of output bias toward interneurons including parvalbumin-expressing cells; reduced firing during movement with prolonged burst firing above 200 Hz during slow-wave sleep; presence of the molecular phenotype in CA1 and CA3 in rat and mouse (electron microscopy plus recordings in freely moving rats)
- Jinno et al. 2007 — PMID:17699661 — supports: somatostatin-negativity; M2 expression; classification among GABAergic long-range projections from hippocampus to subiculum (retrograde tracing plus immunohistochemistry, rat)
- Booker & Vida 2018 — PMID:30084021 — supports: quantitative axon distribution across strata oriens, pyramidale and radiatum; horizontal versus radial dendritic variants; strong Schaffer collateral excitation together with strong inhibition (review of hippocampal interneuron morphology and connectivity)
- Francavilla et al. 2018 — PMID:30487571 — supports: characterisation of the closest confusable type (M2-positive VIP-LRP Type I cell) and its shared features (mouse hippocampus)
- Hewitt et al. 2021 — PMID:33991454 — supports: absence of sag and rebound response as a discriminator from other CA1 stratum oriens interneurons (whole-cell recording, mouse CA1)
- Slomianka et al. 2011 — PMID:21597968 — supports: documentation of the conflicting "trilaminar cell" usage for a deep CA1 pyramidal subpopulation (review)
- Harris et al. 2017 — PMID:29912866 — supports: the Sst-negative, Pvalb-negative, Chrm2- and Ntng1-expressing CA1 stratum oriens transcriptomic class (single-cell transcriptomics, 3663 mouse CA1 inhibitory neurons)
- Meskenaite et al. 2016 — PMID:27445724 — cited only to document the unrelated avian "trilaminar complex" regional usage

---
*Drafted by the evidencell cl-term-request workflow. Literature basis: ASTA deep research report `inputs/deepsearch/trilaminar_hippocampal_cells.pdf`, corpus IDs resolved to DOI/PMID via Semantic Scholar. KB ingest of this report is pending, so the source node does not yet carry quote-backed provenance for all statements above; every claim here is traceable to a quoted passage in that report.*

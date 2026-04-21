# Evidence Drill-down: Winterer et al. 2019
*Supporting: olm_hippocampus → 0727 Lamp5 Lhx6 Gaba_1; olm_hippocampus → 0785 Sst Gaba_6; olm_hippocampus → 0769 Sst Gaba_3; olm_hippocampus → 0788 Sst Gaba_6; olm_hippocampus → 0789 Sst Gaba_6*
*[← Back to summary report](olm_hippocampus_summary.md)*

---

**Winterer J, Maier N, Ziegler C, Lorcini K, Isomura Y, Schmitz D, Bhatt DL, Bhatt DL**
Single-cell RNA-Seq characterization of anatomically identified OLM interneurons in different transgenic mouse lines
*European Journal of Neuroscience* 2019 · PMID:31420995 · DOI:10.1111/ejn.14549

· [GEO:GSE124847](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124847)

---

## Why this paper matters for this mapping

Winterer et al. 2019 performed single-cell RNA sequencing on 46 OLM interneurons that were individually patch-clamped and electrophysiologically characterised in acute hippocampal slices, collected using two independent Cre-driver lines (Htr3a-Cre::Ai14 and Sst-Cre::Ai14), and then subjected to post-hoc morphological reconstruction after DAB staining to verify OLM identity. This triple-validation approach — transgenic targeting, electrophysiology, and confirmed axonal projection to stratum lacunosum-moleculare with horizontal soma and dendrites in stratum oriens — provides exceptionally strong evidence for the mapping, because cells entered the transcriptomic dataset only after their OLM identity was independently confirmed at the anatomical level. Critically, this paper resolves a long-standing species discrepancy regarding Npy expression, demonstrating at both transcript and protein levels that mouse OLM cells consistently co-express Npy, overturning a prior rat-based exclusion criterion (Katona et al. 2014) and a mouse transcriptomic usage of Npy as an OLM-exclusion marker (Harris et al. 2018). The raw data (GEO:GSE124847) are available for direct re-mapping to WMBv1, and the MapMyCells annotation transfer reported in the facts file used this dataset to map 46 OLM cells, strongly supporting the parent Sst Gaba_3 supertype (43/46 cells, F1=0.67 at SUPERTYPE level).

---

## Per-property evidence

### Sst · alignment with 0769 Sst Gaba_3: CONSISTENT

> oriens-lacunosum moleculare (OLM) interneurons. OLMs express somatostatin (Sst), generate feedback inhibition and play important roles in theta oscillations and fear encoding
> — Winterer et al. 2019, Molecular Markers and Gene Expression <!-- quote_key: 201041756_69dc904d -->

Winterer et al. state Sst expression as a defining characteristic of OLM interneurons in their introduction, framing all subsequent scRNA-seq results in that context. The alignment is CONSISTENT: cluster 0769 Sst Gaba_3 [CS20230722_CLUS_0769] belongs to the Sst Gaba subclass (053 Sst Gaba [CS20230722_SUBC_053]), meaning Sst expression is constitutive at the subclass level across this cluster. The Sst subclass assignment directly mirrors the canonical definition stated here. This quote is also relevant to the edges for clusters 0785, 0788, and 0789 Sst Gaba_6 [CS20230722_CLUS_0785/0788/0789], all of which also carry CONSISTENT Sst marker alignment.

---

> we found consistent expression of Sst and Reln, and sparse expression of Pvalb across both OLM neuron types
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_2d5a5fb3 -->

This quantitative scRNA-seq result confirms that Sst expression is consistent (not variable) across the 46 morphologically verified OLM cells from both transgenic lines, and that Pvalb is sparse — reinforcing that OLM cells are an Sst-dominant, Pvalb-negative population. The alignment is CONSISTENT with all five candidate clusters carrying the Sst Gaba subclass designation. The sparse Pvalb finding also matters for cluster differentiation: OLM cells are not a PV+ type, consistent with the classical negative-marker profile. Reln co-expression with Sst is a known feature of hippocampal interneuron subpopulations *(note: Reln is expressed in CA1 stratum oriens interneurons in the mouse hippocampus, and its co-expression with Sst here narrows the identity further, though atlas-side Reln expression is not assessed for these clusters)*.

---

### GABAergic identity · alignment with 0769 Sst Gaba_3: CONSISTENT

> Independent of the Cre line used for cell collection, we found consistent expression of GABA release‐related Gad1, Gad2 and Slc6a1 in all OLM interneurons. By contrast, glutamate release‐related vesicular glutamate transporter Slc17a7 (detected in 2/46 cells) and Slc17a6 (detected in 1/46 cells) genes were virtually not expressed across the whole population.
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_1d024a35 -->

All 46 morphologically verified OLM cells expressed the canonical GABAergic biosynthesis and transport genes (Gad1, Gad2, Slc6a1), while glutamatergic transporter genes were absent from virtually the entire population. The alignment is CONSISTENT across all five candidate clusters, which are all assigned to GABA NT class in WMBv1. The Slc17a7/Slc17a6 absence finding robustly excludes any glutamatergic contamination of this population, strengthening the NT identity claim. This evidence holds for all five edges.

---

### Chrna2 · alignment with 0769 Sst Gaba_3: APPROXIMATE

> as well as expression of Chrna2, which has been used as a marker for hippocampal OLM interneurons
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_bd56f851 -->

Winterer et al. confirm Chrna2 expression in their morphologically verified OLM cells, corroborating its status as an OLM-defining marker. For cluster 0769 Sst Gaba_3 [CS20230722_CLUS_0769], the alignment is APPROXIMATE: the ABC Atlas HPF/GABA/Chrna2 filter retains the parent Sst Gaba_3 supertype, indicating Chrna2 is expressed across this supertype, but the expression is scattered across sibling clusters (not restricted to cluster 0769 specifically) — expression across supertype not specific to one cluster. The Chrna2 evidence from Winterer et al. most directly implicates the Sst Gaba_3 supertype as a whole rather than cluster 0769 individually. For the three Sst Gaba_6 clusters (0785, 0788, 0789), this same Chrna2 evidence is DISCORDANT: the ABC Atlas filter eliminates the Sst Gaba_6 supertype entirely *(distant region — stronger counter-evidence; the classical type may still be a subtype of this T-type but not the Sst Gaba_6 population specifically)*. For the Lamp5 Lhx6 cluster 0727, Chrna2 is NOT_ASSESSED (absent from atlas metadata for this cluster).

---

### mGluR1 (Grm1) · alignment with 0769 Sst Gaba_3: NOT_ASSESSED

> we found both Elfn1 and Grm1 to be present throughout the cell population
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_b1ead2e9 -->

Winterer et al. report Grm1 (mGluR1) expression throughout the OLM cell population — consistent with prior literature identifying mGluR1 as a defining OLM marker (cited in the classical node definition). The quantification in the facts file places Grm1 detection at 44/46 OLM cells (96%). However, the alignment is NOT_ASSESSED for all five candidate clusters: Grm1 does not appear in cluster-level defining_markers or neuropeptides in the atlas metadata, so the atlas-side value cannot be evaluated. This is a protein-level marker in prior literature confirmed at transcript level here, but it cannot be used to distinguish between candidate clusters until atlas-side Grm1 expression is resolved. The co-expression of Elfn1 *(note: Elfn1 is a postsynaptic density protein known to enrich at synapses of SST interneurons and promote short-term plasticity at those synapses — its expression here is consistent with OLM identity, though it is not specific to OLM cells among hippocampal Sst interneurons)* is also not assessable at the atlas cluster level.

---

### Npy · alignment with 0769 Sst Gaba_3: CONSISTENT

> we found a surprisingly consistent expression of Npy in OLMs
> — Winterer et al. 2019, Molecular Markers and Gene Expression <!-- quote_key: 201041756_8d16e821 -->

This brief but consequential statement establishes Npy transcript co-expression in OLM cells. The surprise qualifier signals that this conflicts with prior expectations. The alignment is CONSISTENT with cluster 0769 Sst Gaba_3 [CS20230722_CLUS_0769], which carries the full neuropeptide triad (Sst, Npy, Pnoc) in its atlas metadata. This evidence is relevant to the 0727 Lamp5 Lhx6 Gaba_1 edge, where Npy is DISCORDANT (absent from that cluster's metadata), making the Npy finding a discriminating datum favouring the Sst Gaba_3 clusters over the Lamp5 Lhx6 candidate.

---

> we found consistent expression of Npy. This observation was striking, because an earlier study showed the lack of NPY in OLM cells (0/4) in the rat hippocampus (Katona et al., 2014), and expression of its gene was previously used to exclude OLM identity in single‐cell transcriptomic samples in mouse (Harris et al., 2018).
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_9991ee9f -->

This is the full quantitative statement, resolving the inter-study discrepancy explicitly. Winterer et al. demonstrate that the rat data (Katona et al. 2014: 0/4 OLM cells NPY-positive) do not translate to mouse, and that use of Npy as an OLM-exclusion criterion in Harris et al. 2018 was incorrect for the mouse. *(note: this is a species difference — rat OLM cells appear to lack Npy while mouse OLM cells consistently express it; cross-species differences for this marker are confirmed within this paper)* The alignment is CONSISTENT for clusters 0769, 0785, 0788, and 0789 (all carry Npy in their neuropeptide profiles), and DISCORDANT for cluster 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] which lacks Npy.

---

> we were able to confirm the presence of NPY in 3 out of 5 OLM neurons
> — Winterer et al. 2019, Results 3.5 <!-- quote_key: 201041756_6f670235 -->

This protein-level confirmation (3/5 cells by immunostaining) elevates Npy from a transcript observation to a verified protein-level finding, directly strengthening the neuropeptide alignment. The alignment remains CONSISTENT for clusters carrying Npy (0769, 0785, 0788, 0789). The protein detection rate (60%) is lower than the mRNA detection rate, which is expected given the sensitivity differences between immunohistochemistry and scRNA-seq *(note: IHC detection of neuropeptides can vary with antibody sensitivity and fixation protocols; the transcript data showing consistent Npy mRNA is likely a more complete reflection of expression prevalence)*.

---

### Pnoc · alignment with 0769 Sst Gaba_3: CONSISTENT

> we detected Pnoc in both Htr3aCre‐OLM (14/23) and SstCre‐OLM (13/23)
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_1d20426d -->

Pnoc is detected in approximately 60% of OLM cells in both transgenic lines (27/46 total). The alignment is CONSISTENT for cluster 0769 Sst Gaba_3 [CS20230722_CLUS_0769], which carries Pnoc in its atlas metadata as part of the full neuropeptide triad. The fact that Pnoc is not expressed in 100% of OLM cells is consistent with sub-cluster heterogeneity within the Sst Gaba_3 supertype *(note: Thulin et al. 2025, referenced in the classical node definition, identify three Sst/Pnoc subclusters with differential connectivity — partial Pnoc expression across the OLM population is consistent with this heterogeneity)*. Pnoc alignment is DISCORDANT for cluster 0785 Sst Gaba_6 [CS20230722_CLUS_0785] (Pnoc absent from that cluster's metadata), and CONSISTENT for clusters 0788 and 0789 (both carry Pnoc). The Pnoc finding also broadly supports the connection noted in the facts file between OLM identity and Sst/Pnoc co-expression.

---

### MGE origin / Lhx6 · alignment with 0769 Sst Gaba_3: CONSISTENT

> all Htr3aCre‐OLM and SstCre‐OLM neurons consistently expressed MGE‐associated marker genes
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_807e85c2 -->

This quote (claims: lhx6_positive, mge_origin, satb1_positive, sox6_positive) establishes that both transgenic OLM subtypes are MGE-derived, expressing Lhx6, Satb1, and Sox6 without exception. The alignment is CONSISTENT with the Sst Gaba subclass, which belongs to the MGE-derived GABA class (07 CTX-MGE GABA [CS20230722_CLAS_07]), confirmed by the MapMyCells annotation transfer (45/46 cells mapped to 07 CTX-MGE GABA at class level, F1=0.68, group_purity=1.0). This finding is critically DISCORDANT with the Lamp5 Lhx6 subclass assignment of cluster 0727, which is a CGE-derived lineage *(note: Lamp5 Lhx6 clusters in WMBv1 are classified under CGE-derived interneurons; canonical OLM cells as defined by MGE origin are inconsistent with a CGE lineage assignment, making this lineage finding a strong argument against cluster 0727)*.

---

> we analysed expression of key developmental marker genes: including CGE‐associated Prox1, Htr3a and Sp8, as well as MGE‐associated Lhx6, Satb1 and Sox6
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_0670df0d -->

This methodological statement establishes the systematic framework for the developmental origin analysis. It shows that both CGE and MGE marker sets were tested, making the conclusion of MGE origin a genuine discrimination rather than a partial test.

---

> We detected Htr3a, Prox1 and Sp8 in 5, 1 and 1 out of 23 Htr3a‐OLMs, respectively. By contrast, all Htr3aCre‐OLM and SstCre‐OLM neurons consistently expressed MGE‐associated marker genes
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_8c9b1b66 -->

CGE markers (Htr3a, Prox1, Sp8) are detected in only 5/23, 1/23, and 1/23 cells respectively, while all 46 OLM cells express the MGE markers. This quantitative contrast strongly confirms MGE origin. The sparse Htr3a detection (5/23 of the Htr3a-Cre-targeted cells) is notable: even the Htr3a-Cre line, which should preferentially label Htr3a-expressing cells, captured OLM cells that transcriptomically are predominantly MGE-type. This supports the conclusion that Htr3a-Cre OLM cells are a morphologically and transcriptomically distinct population from canonical CGE-derived, Htr3a-expressing interneurons. This directly strengthens the CONSISTENT MGE-origin alignment for all Sst Gaba clusters and reinforces the DISCORDANT lineage argument against the Lamp5 Lhx6 cluster 0727.

---

> Additional regression analysis furthermore supported the strong correlation between developmental marker expression for SstCre‐OLM and Htr3aCre‐OLM types (R = 0.99)
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_a4e5b13e -->

The near-perfect correlation (R = 0.99) in developmental marker profiles across the two transgenic lines confirms that both lines capture the same transcriptomic population and that the MGE origin conclusion is robust across collection method. This supports the claim that OLM identity maps to a single, coherent transcriptomic population — consistent with the MapMyCells result showing convergence of both Sst-OLM and Htr3a-OLM subtypes on the same Sst Gaba_3 supertype.

---

### Htr3a · alignment with 0769 Sst Gaba_3: CONSISTENT

> our results revealed surprisingly infrequent expression of Htr3a in only ~10% of OLMs and an apparently specific expression of the 5-HT3b subunit-coding gene Htr3b in Htr3aCre-OLMs
> — Winterer et al. 2019, Molecular Markers and Gene Expression <!-- quote_key: 201041756_90146223 -->

Htr3a is expressed in only ~10% of OLMs overall, despite the use of an Htr3a-Cre driver line. This makes Htr3a a negative indicator for OLM identity rather than a positive marker. The alignment for this property relative to all five candidate clusters is best characterised as CONSISTENT with their Sst subclass (not Htr3a) assignment, reinforcing that OLM cells — even those captured via Htr3a-Cre — transcriptomically belong to the Sst, not the Lamp5/Htr3a, lineage.

---

> we found infrequent expression of Htr3a in both Htr3aCre‐OLM (5/23) and SstCre‐OLM (2/23) types
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_cf49e910 -->

The quantitative data (5/23 and 2/23) confirm Htr3a is sparse in both OLM subtypes. This aligns with the Sst Gaba subclass assignment of the best candidate clusters, where Htr3a would not be a defining marker.

---

### Transcriptomic homogeneity · alignment with 0769 Sst Gaba_3 (population character)

> OLMs constitute a highly homogenous transcriptomic population
> — Winterer et al. 2019, Molecular Markers and Gene Expression <!-- quote_key: 201041756_afab0ca7 -->

This summary characterisation is relevant to interpreting the MapMyCells scatter across sibling clusters 0767–0774 within the Sst Gaba_3 supertype. Winterer et al.'s own analysis concluded OLM cells form a homogeneous population, yet the annotation transfer scatters them across multiple clusters within Sst Gaba_3. This tension suggests the within-supertype scatter reflects limitations of the cluster-level reference resolution for this population rather than genuine heterogeneity in the source cells. The evidence supports mapping at SUPERTYPE rather than cluster level as the appropriate resolution for OLM identity.

---

> these comparisons suggest strong similarities between our OLM cells and Harris et al.’s Sst cells, with exception of Npy expression
> — Winterer et al. 2019, Results 3.4 <!-- quote_key: 201041756_390db1a8 -->

Winterer et al. directly contextualise their data against Harris et al. 2018's Sst cell transcriptomic clusters, finding broad similarity except for Npy. This supports the mapping to the Sst Gaba subclass in WMBv1 and the CONSISTENT Npy neuropeptide alignment for the Sst Gaba_3 clusters.

---

### Morphology and electrophysiology (identity confirmation)

> cells that were included in the study were first reconstructed after DAB staining to identify the morphological characteristics of OLM cells, including the axonal projection to the lacunosum moleculare, the horizontally orientated soma and dendritic branching in the oriens
> — Winterer et al. 2019, Molecular Markers and Gene Expression <!-- quote_key: 201041756_c6648415 -->

This is the inclusion criterion for the dataset. Cells entered the transcriptomic corpus only after morphological confirmation of: (1) axon projecting to stratum lacunosum-moleculare [UBERON:0007637], (2) horizontal soma, and (3) dendritic branching in stratum oriens [UBERON:0014548]. This strict gate means the transcriptomic data are anchored to anatomically defined OLM identity — a critical strength for the mapping. The atlas-side location comparison for cluster 0769 [CS20230722_CLUS_0769] is APPROXIMATE: CA1 stratum oriens [MBA:399] is the primary OLM location (87 cells in the cluster), matching the classical definition, but there is additional spread to prosubiculum (61 cells) and posterior amygdala (95 cells) *(adjacent region — could reflect registration boundary error; weak counter-evidence)* for the prosubiculum, which borders CA1. The posterior amygdala spread is more concerning *(note: the posterior amygdala is not adjacent to CA1 stratum oriens; this spread is anatomically distant and may indicate that cluster 0769 contains non-OLM Sst interneurons from extrahippocampal regions)*.

---

> All cells that were included in the study were first reconstructed after DAB staining to identify the morphological characteristics of OLM cells, including the axonal projection to the lacunosum moleculare, the horizontally orientated soma and dendritic branching in the oriens
> — Winterer et al. 2019, Results 3.1 <!-- quote_key: 201041756_7b9b4800 -->

This is the methods confirmation (in the Results section) of the same inclusion criterion. The duplication reinforces that morphological verification was a hard gate, not a post-hoc annotation.

---

> we morphologically characterized the recorded cells, and only proceeded with those for electrophysiological analysis and single‐cell RNA sequencing which had axonal and/or dendritic morphology stereotypical to OLM cells
> — Winterer et al. 2019, Results 3.0 <!-- quote_key: 201041756_eb2447af -->

This statement documents the sequential gating: morphological characterisation preceded both electrophysiological recording and scRNA-seq, meaning all 46 cells in the dataset had confirmed OLM morphology before any molecular data were collected. The phrase "axonal and/or dendritic morphology stereotypical to OLM cells" indicates that not all cells required complete axonal reconstruction — some may have qualified on dendritic features alone. This is a minor caveat but does not materially weaken the dataset quality.

---

> We observed these typical features of OLM interneurons in both Htr3aCre‐OLM and SstCre‐OLM cells (sag potential: 0.51 ± 0.02 vs. 0.47± 0.03 mV; frequency adaptation ratio: 0.52 ± 0.03 vs. 0.43 ± 0.04; maximum AP firing: 53.2 ± 4.0 Hz vs. 62.2 ± 3.5 Hz; and RMP: −62.4 ± 1.2 vs. −63.4 ± 1.7, respectively).
> — Winterer et al. 2019, Results 3.2 <!-- quote_key: 201041756_1fea12c0 -->

The electrophysiological parameters (sag potential, frequency adaptation, maximum firing rate, resting membrane potential) are quantitatively consistent across both transgenic OLM subtypes and match the classical OLM electrophysiology profile described in the classical node definition (pronounced sag, regular-to-adapting firing, high input resistance, theta-range spiking). The alignment for electrophysiology is NOT_ASSESSED against the atlas clusters, as WMBv1 cluster metadata does not include electrophysiological parameters. These data function as additional identity confirmation rather than a discriminating atlas comparison.

---

> In acute hippocampal brain slices, we identified OLM neurons based on tdTomato expression using the Htr3a‐Cre::Ai14 and Sst‐Cre::Ai14 transgenic lines. Single cells were electrophysiologically characterized, and their cytosolic mRNA was subsequently aspirated. Single‐cell RNA sequencing was performed after confirming OLM identity by post hoc visualization of axons and dendrites.
> — Winterer et al. 2019, Figure 1 caption <!-- quote_key: 201041756_9dce8a8e -->

This figure caption concisely summarises the full experimental workflow: fluorescent targeting → electrophysiology → mRNA aspiration → scRNA-seq → post-hoc morphological confirmation. The workflow is explicitly sequential, confirming that no cell contributed transcriptomic data unless its OLM identity was verified at multiple independent levels. This is the strongest structural source of evidential confidence for the dataset.

---

### Syt1/Syt2 profile

> we detected consistent expression of Syt1 and lack of Syt2. This is in accordance with previous literature, as Syt2 has been reported to be associated with Pvalb+ cells
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_8340e0a0 -->

Syt1 positivity and Syt2 negativity in OLM cells aligns with their Pvalb-sparse profile (confirmed earlier in the dataset) and distinguishes OLM cells from fast-spiking, Syt2-positive PV+ interneurons. This is NOT_ASSESSED against the atlas clusters (Syt1/Syt2 expression is not in the cluster-level metadata fields used for comparison), but it provides additional molecular evidence distinguishing OLM from chandelier and basket cell populations.

---

### Additional markers (Gria4, Kcnc2, Kcnd3, Cacna1a, Cacna1g)

> we found consistent expression of Gria4, Kcnc2, Kcnd3, Cacna1a and Cacna1g, which have been described to be present in OLMs
> — Winterer et al. 2019, Results 3.3 <!-- quote_key: 201041756_708ee6a6 -->

These ion channel subunits (AMPA receptor subunit Gria4; voltage-gated K+ channels Kcnc2/Kcnd3; voltage-gated Ca2+ channels Cacna1a/Cacna1g) are confirmed as consistent markers in the OLM transcriptome. Their alignment against the atlas candidate clusters is NOT_ASSESSED (none of these appear in cluster-level defining_markers or neuropeptides in the WMBv1 metadata). They serve as additional molecular context supporting the coherent OLM transcriptomic signature but cannot discriminate between the candidate clusters.

---

### Dataset availability

> Raw sequences are deposited and freely available under NCBI GEO # GSE124847.
> — Winterer et al. 2019, Data Availability <!-- quote_key: 201041756_83f848d5 -->

GEO:GSE124847 is the source dataset used in the MapMyCells annotation transfer documented in the facts file. The data are freely available and have already been used to generate the annotation transfer evidence for all five edges in this mapping.

---

## Summary scorecard

| Property | Paper finding | Atlas alignment | Quote key |
|---|---|---|---|
| Sst (introduction) | OLM-defining, consistent expression | CONSISTENT | 201041756_69dc904d |
| Sst (scRNA-seq result) | Consistent in all 46 cells; Pvalb sparse | CONSISTENT | 201041756_2d5a5fb3 |
| GABAergic identity | Gad1/Gad2/Slc6a1 all cells; Slc17a7/Slc17a6 absent | CONSISTENT | 201041756_1d024a35 |
| Chrna2 | Confirmed expression in OLM cells | APPROXIMATE (0769); DISCORDANT (0785/0788/0789) | 201041756_bd56f851 |
| mGluR1 (Grm1) | Present throughout (44/46 cells) | NOT_ASSESSED | 201041756_b1ead2e9 |
| Npy (brief statement) | Surprisingly consistent expression | CONSISTENT | 201041756_8d16e821 |
| Npy (with species context) | Consistent; overturn rat exclusion criterion | CONSISTENT (0769/0785/0788/0789); DISCORDANT (0727) | 201041756_9991ee9f |
| Npy (protein confirmation) | 3/5 OLM cells NPY+ by immunostaining | CONSISTENT | 201041756_6f670235 |
| Pnoc | ~60% of cells in both lines | CONSISTENT (0769/0788/0789); DISCORDANT (0785) | 201041756_1d20426d |
| MGE origin / Lhx6 | All cells express Lhx6, Satb1, Sox6 | CONSISTENT (Sst clusters); DISCORDANT (0727 Lamp5 Lhx6) | 201041756_807e85c2 |
| CGE markers absent | Htr3a/Prox1/Sp8 rare or absent | CONSISTENT | 201041756_8c9b1b66 |
| MGE correlation across lines | R = 0.99 between both OLM subtypes | CONSISTENT | 201041756_a4e5b13e |
| Htr3a (introduction) | ~10% of OLMs; Htr3b specific to Htr3a-line | CONSISTENT | 201041756_90146223 |
| Htr3a (quantified) | 5/23 and 2/23 in each line | CONSISTENT | 201041756_cf49e910 |
| Transcriptomic homogeneity | OLMs are homogeneous population | Population character | 201041756_afab0ca7 |
| Harris Sst similarity | Broad similarity except Npy | CONSISTENT | 201041756_390db1a8 |
| Morphology (methods) | DAB reconstruction; axon to SLM; horizontal soma; dendrites in SO | APPROXIMATE (location) | 201041756_c6648415 |
| Morphology (results) | Same criteria confirmed in results | APPROXIMATE (location) | 201041756_7b9b4800 |
| Inclusion criterion | Morphology gate before scRNA-seq | Identity confirmation | 201041756_eb2447af |
| Electrophysiology | Sag, adaptation, firing rate, RMP consistent across lines | NOT_ASSESSED | 201041756_1fea12c0 |
| Experimental workflow | Transgenic → ephys → aspiration → scRNA-seq → post-hoc morphology | Identity confirmation | 201041756_9dce8a8e |
| Syt1/Syt2 | Syt1 consistent; Syt2 absent (PV-negative signature) | NOT_ASSESSED | 201041756_8340e0a0 |
| Additional ion channels | Gria4, Kcnc2, Kcnd3, Cacna1a, Cacna1g all consistent | NOT_ASSESSED | 201041756_708ee6a6 |
| Dataset accession | GEO:GSE124847 freely available | Evidence source | 201041756_83f848d5 |

---

## Critical gap

Winterer et al. 2019 did not map their cells to WMBv1 directly — this paper predates the atlas. While the MapMyCells annotation transfer using GEO:GSE124847 provides strong supertype-level support (Sst Gaba_3, F1=0.67, 43/46 cells), OLM cells scatter across sibling clusters 0767–0774 at cluster level, and cluster 0769 specifically received 0/46 cells (cells preferentially map to cluster 0768, 22/46). The connection therefore requires resolution at cluster level: the specific bridging experiment needed is Chrna2-Cre driver line + MapMyCells at F1 ≥ 0.80 at CLUSTER level — see Proposed experiments in the summary report. Importantly, GEO:GSE124847 data are available for direct re-mapping without new experiments, and could be used for deeper cluster-level resolution using updated MapMyCells parameters or alternative reference datasets.

---

*Drill-down generated from: references.json (corpus_id: 201041756)*
*Quotes: source_method=primary, asta_report, status=verified, validated*

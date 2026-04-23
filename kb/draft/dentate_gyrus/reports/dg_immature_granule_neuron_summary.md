# Dentate Gyrus Immature Granule Neuron — Allen Brain Cell Atlas CCN202307220 Mapping Report
*draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

**⚠ DRAFT WARNING:** Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.

---

## Classical Type

The dentate gyrus immature granule neuron (CL:9900002) is a postmitotic, DCX-positive excitatory neuron occupying the inner granule cell layer immediately following migration from the subgranular zone. It constitutes stage 5 of the adult hippocampal neurogenesis sequence and is distinguished from the immediately preceding neuroblast by the co-acquisition of NeuN and from the succeeding mature granule neuron by the absence of Calbindin. CL:9900002 was proposed on the basis of this mapping work, anchored by the Tbr1+/Prox1+/Igfbpl1+ atlas marker profile and the classical DCX+/NeuN+ description.

The classical definition is protein-IHC–based; all transcriptomic comparisons in this report involve a methodological gap between protein abundance and mRNA expression level (see Concerns, below).

---

## 3. Classical Type Table

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus granule cell layer [UBERON:0005381] — inner (SGZ-proximal) zone | [1], [2] |
| Neurotransmitter | Glutamatergic | [3], [4] |
| Defining markers | DCX (protein, positive) | [5], [6] |
| | NeuN / RBFOX3 (protein, positive; postmitotic) | [5], [6] |
| | PSA-NCAM (protein, positive; migrating neurons) | [6] |
| | Tis21 / BTG2 (protein, positive; postmitotic re-expression) | [7] |
| Negative markers | Calbindin (protein, absent; distinguishes from mature granule neuron) | — |
| Neuropeptides | None reported | — |
| CL term | immature dentate gyrus granule neuron (CL:9900002) — EXACT | — |

---

## 4. Mapping Candidates Table

| Rank | WMBv1 Cluster | Supertype | Cells | Confidence | Key Property Alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514] | DG-PIR Ex IMN_2 | N/A | 🔴 LOW | NT consistent; location consistent (DGdo,me HIP:0.98); EXACT CL:9900002; Tbr1+/Prox1+/Emx2+/Igfbpl1+ TF core; Calbindin absent; DCX/NeuN/Tis21 APPROXIMATE | Speculative — part of TYPE_A_SPLITS pair |
| 2 | 0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515] | DG-PIR Ex IMN_2 | N/A | 🔴 LOW | NT consistent (parent-class Glut); location consistent (DGdo,me HIP:1.0); EXACT CL:9900002; identical core TF profile; Rarb/Bcl11b/Cd24a distinctive markers | Speculative — TYPE_A_SPLITS companion to 0514 |

Both clusters carry the same discovery composite score (0.82) and the same EXACT CL annotation. Neither alone fully represents the classical type; together they span the immature granule neuron stage.

---

## 5. Candidate Paragraphs

### Cluster 0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514]

**Supporting evidence**

- EXACT CL:9900002 (immature dentate gyrus granule neuron) assigned by atlas curators, with the annotation "late neuroblast/immature granule cell", directly matching the classical stage 5 designation. [ATLAS_METADATA]
- Transcription factor profile Tbr1+/Prox1+/Emx2+/Igfbpl1+/Ccbe1 is consistent with a postmitotic granule neuron precursor identity. Tbr1 onset is established as the molecular marker for the neuroblast-to-immature-granule-neuron transition, because Tbr1 is expressed exclusively in postmitotic granule cells and never co-localises with the progenitor marker nestin-GFP [8].
- Stage 5 of the adult neurogenesis sequence (DCX+/NeuN+ co-expression, Calbindin−) is the accepted definition of the immature granule neuron. The absence of Calbindin (Calb1) from the cluster's defining markers is consistent with pre-terminal immature identity and distinguishes it from the mature granule neuron stage [5].
- Tis21 (Btg2) re-expression in postmitotic adult DG neurons confirms that Tis21 marks a stage later than type-2/3 progenitors and is proposed to relate to functional integration. This is compatible with Tbr1+ postmitotic status [7].
- Glutamatergic neurotransmitter type is consistent across classical literature [3], [4] and the ATLAS annotation (Glut). Spatial localisation to dentate gyrus dorsal/medial blade (DGdo,me; HIP allocation 0.98) is consistent with the classical inner GCL soma location [UBERON:0005381] [1], [2].

**Concerns**

- DCX, NeuN, PSA-NCAM, and Tis21 are all APPROXIMATE alignments, reflecting the protein-IHC / scRNA-seq methodological gap. DCX mRNA is broadly expressed across the DG-PIR Ex IMN subclass and may be present in cluster 0514 below the atlas marker-ranking threshold. PSA-NCAM is a post-translational glycan epitope and is intrinsically undetectable by transcriptomics. APPROXIMATE alignments do not indicate biological discordance; they indicate incomplete evidence.
- Cluster 0514 carries a Gad1 nt_marker signal (score 5.56). *(note: this may reflect the transient depolarising GABAergic input known to occur in immature granule neurons during the 8–18 dpi window when EGABA is −26.9 to −44.5 mV, or it may indicate a doublet artefact or low-level contamination from adjacent GABAergic interneurons — not yet resolved)*
- The classical type is split across two atlas clusters (TYPE_A_SPLITS): cluster 0514 (this edge) and cluster 0515 are both assigned CL:9900002 and share the same core TF profile. Neither cluster alone fully captures the classical type. The biological basis for this two-cluster split is unresolved.
- Twelve proposed literature evidence items (proposed_evidence_dg_immature_granule_neuron.yaml) are pending review and attachment to this edge and its companion to cluster 0515; the evidence presented here covers the most load-bearing items only.

**What would upgrade confidence**

- Anti-DCX / anti-Tbr1 co-immunostaining on adult mouse DG tissue to confirm that Tbr1+ inner-GCL cells are also DCX+/NeuN+ at the protein level, directly bridging the atlas TF profile and the classical IHC-based definition.
- Query of the full Allen Brain Cell Atlas CCN202307220 feature matrix for *Dcx*, *Rbfox3*, and *Btg2* expression in clusters 0514/0515 below the marker-ranking threshold, to determine whether their absence from defining markers reflects genuine non-expression or a rank-filtering artefact.
- Resolution of the Gad1 signal (doublet testing, comparison with adjacent interneuron clusters).

---

### Cluster 0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515]

**Supporting evidence**

- EXACT CL:9900002 assigned by atlas curators with annotation "late neuroblast". Core TF profile is identical to cluster 0514 (Tbr1+/Prox1+/Emx2+/Igfbpl1+), strongly supporting postmitotic granule neuron identity at the same developmental stage [ATLAS_METADATA].
- Spatial localisation DGdo,me with HIP allocation 1.0 (perfect hippocampal assignment) is consistent with the inner GCL soma location [UBERON:0005381] [1], [2].
- Same literature support as cluster 0514: stage 5 definition (DCX+/NeuN+/Calbindin−) [5], Tbr1 as postmitotic transition marker [8], and Tis21 re-expression in maturing adult DG neurons [7].
- Additional cluster-distinctive MERFISH markers Rarb, Bcl11b, Cd24a, and Fam163a localise within the same dorsal/medial DG spatial context; while their biological interpretation is unresolved, they do not contradict the immature granule neuron assignment.

**Concerns**

- All DCX, NeuN, PSA-NCAM, and Tis21 marker comparisons are APPROXIMATE or NOT_ASSESSED, for the same protein-IHC / transcriptomics methodological reasons as cluster 0514.
- NT type is not directly assigned at cluster level (nt_type_combo_label: null); glutamatergic identity is inherited from the parent class. Direct cluster-level NT assignment would strengthen the evidence.
- Gad1 nt_marker signal (score 3.67) is lower than in cluster 0514 (5.56). If the two clusters represent a maturational continuum, the lower Gad1 signal in 0515 may indicate a more advanced stage (with less transient GABAergic input) — or alternatively 0515 is earlier, making cluster ordering currently uncertain *(note: interpretation of Gad1 signal ordering relative to maturational stage requires pseudotime or RNA velocity analysis)*.
- TYPE_A_SPLITS companion to cluster 0514; same caveats regarding completeness apply.

**What would upgrade confidence**

- RNA velocity or pseudotime analysis on the DG-PIR Ex IMN_2 supertype (clusters 0512–0515) to establish the ordering of clusters along the neuroblast-to-immature-GN axis, and to place clusters 0514 and 0515 relative to each other.
- Targeted single-molecule FISH (smFISH) for Tbr1, Rarb, Bcl11b, and Dcx in adult DG sections to determine whether Rarb+/Bcl11b+ cells form a spatially distinct subpopulation within the inner GCL, and whether they are DCX+ at the mRNA level.
- Direct cluster-level NT assignment from the atlas feature matrix.

---

## Eliminated Candidates

No UNCERTAIN-confidence edges are present in this mapping. Both candidate clusters are LOW confidence, assessed as Speculative.

---

## 6. Proposed Experiments

### Immunohistochemistry / Immunofluorescence

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Anti-DCX + anti-Tbr1 co-stain on adult mouse DG | Protein co-expression in inner GCL | Confirm Tbr1+ inner-GCL cells are DCX+/NeuN+ at protein level | Bridges atlas TF evidence (Tbr1) to classical IHC-based stage-5 definition; upgrades DCX and NeuN comparisons from APPROXIMATE to CONSISTENT |
| Anti-Rarb + anti-Bcl11b + anti-DCX triple-label smFISH | Rarb, Bcl11b, Dcx mRNA in adult DG | Determine whether Rarb+/Bcl11b+ cells are spatially distinct within inner GCL and are Dcx+ | Resolves biological basis for 0514 vs 0515 split; confirms 0515 identity as immature GN sub-stage |

### Transcriptomic / Computational

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Feature-matrix query: Dcx, Rbfox3, Btg2 expression in clusters 0514/0515 | Full Allen Brain Cell Atlas CCN202307220 feature matrix | Expression levels below marker-ranking threshold, if present | Resolves APPROXIMATE marker alignments for DCX, NeuN, Tis21 |
| RNA velocity or pseudotime on DG-PIR Ex IMN_2 supertype (clusters 0512–0515) | Transcriptional dynamics across the neuroblast–immature-GN axis | Ordered trajectory; cluster positions along the axis | Determines ordering of 0514 vs 0515; clarifies maturational sub-stage interpretation |

---

## 7. Open Questions

1. What is the biological basis for the two-cluster split of the immature granule neuron stage into clusters 0514 and 0515? Candidate explanations include: maturational sub-stages within stage 5, sex-biased transcriptional states, or circadian/activity-dependent gene expression.
2. Does *Dcx* mRNA appear in clusters 0514/0515 below the atlas marker-ranking threshold? A targeted query of the full atlas feature matrix would resolve the DCX protein–mRNA alignment gap.
3. Why does cluster 0514 show a Gad1 nt_marker signal (score 5.56) and cluster 0515 a Gad1 signal (score 3.67)? Does this reflect the known transient depolarising GABAergic phase (8–18 dpi), a doublet artefact, or low-level contamination from neighbouring interneurons?
4. Does the Gad1 signal gradient (0514 > 0515) indicate a maturational ordering (0515 more advanced) or the reverse? This is currently unresolved without pseudotime data.
5. What distinguishes cluster 0515 from 0514 biologically? Rarb (retinoic acid receptor beta, cluster-scoped in 0515) and Bcl11b/Cd24a/Fam163a MERFISH markers are distinctive but their functional significance in this context is unknown.
6. Do the 12 pending proposed literature evidence items (proposed_evidence_dg_immature_granule_neuron.yaml) change confidence assessment for either edge once reviewed and attached?

---

## 8. Evidence Base Table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514 | ATLAS_METADATA, LITERATURE (review [5]), LITERATURE (experimental [8]), LITERATURE (experimental [7]) | SUPPORT (all items) |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0515 | ATLAS_METADATA, LITERATURE (review [5]), LITERATURE (experimental [8]), LITERATURE (experimental [7]) | SUPPORT (all items) |

---

## 9. References

[1] Velusamy 2017 · [PMID:28168008](https://pubmed.ncbi.nlm.nih.gov/28168008/) · DOI:10.1155/2017/3279061 · *Used for: soma location*

[2] Regalado-Santiago 2016 · [PMID:26880934](https://pubmed.ncbi.nlm.nih.gov/26880934/) · DOI:10.1155/2016/1513285 · *Used for: soma location*

[3] Stoll 2014 · [PMID:26056581](https://pubmed.ncbi.nlm.nih.gov/26056581/) · DOI:10.1186/2052-8426-2-12 · *Used for: neurotransmitter type*

[4] Vangeneugden 2015 · [PMID:25954142](https://pubmed.ncbi.nlm.nih.gov/25954142/) · DOI:10.3389/fnins.2015.00110 · *Used for: neurotransmitter type*

[5] Micheli 2025 · [PMID:40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) · DOI:10.3389/fcell.2025.1605116 · *Used for: DCX marker; stage-5 (DCX+/NeuN+/Calbindin−) definition*

[6] Stepień 2021 · [PMID:37082558](https://pubmed.ncbi.nlm.nih.gov/37082558/) · DOI:10.5114/ppn.2021.111950 · *Used for: DCX marker; PSA-NCAM*

[7] Attardo 2009 · [PMID:19482889](https://pubmed.ncbi.nlm.nih.gov/19482889/) · DOI:10.1093/cercor/bhp100 · *Used for: Tis21 marker (postmitotic re-expression in adult DG)*

[8] Hodge 2008 · [PMID:18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) · DOI:10.1523/JNEUROSCI.4280-07.2008 · *Used for: Tbr1 onset marks postmitotic transition from neuroblast to immature granule neuron*

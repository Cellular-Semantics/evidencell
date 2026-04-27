# Sexually dimorphic nucleus of the preoptic area (SDN-POA) calbindin neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:515] *(specifically the SDN-POA subnucleus, not separately parcellated in WMBv1)* | [1], [2] |
| Defining marker | Calb1 (calbindin-D28K; protein, IHC) | [2] |
| Negative marker | Th (no TH-positive cell bodies in SDN-POA) | [2] |

No CL term exists for this cell type; it is a candidate for a new CL entry.

**Background.** The SDN-POA is a histologically defined cluster of neurons in the medial preoptic area of the hypothalamus. It is the most thoroughly characterised sexually dimorphic brain structure in rodents — larger in males than in females — and is functionally linked to male sex behaviour [1]. It is considered the rodent homolog of the third interstitial nucleus of the anterior hypothalamus (INAH3) in humans; homologous structures have been described in sheep (ovine SDN), rhesus macaque, and quail [2].

**Anatomy note.** The classical node is located in Medial preoptic nucleus [MBA:515]. An earlier version of the KB erroneously recorded the location as MBA:464 (Paraventricular hypothalamic nucleus, descending division — PVN); this has been corrected to MBA:515 (MPN) in the current graph. The SDN-POA is a cytoarchitectonically defined subnucleus within MPN and is not resolved as a distinct spatial domain in WMBv1 MERFISH data.

The nucleus is delineated either by conventional Nissl staining or by calbindin-D28K immunoreactivity:

> "One of the well-defined sexually dimorphic structures in the brain is the sexually dimorphic nucleus, a cluster of cells located in the preoptic area of the hypothalamus. The rodent sexually dimorphic nucleus of the preoptic area can be delineated histologically using conventional Nissl staining or immunohistochemically using calbindin D28K immunoreactivity"
> — Z et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_d6c3a647 -->

> "The sexually dimorphic nucleus of the preoptic area is highlighted by calbindin-D28K immunoreactivity: no TH-positive cells were found, but fine axon-like projections/synaptic structures were seen"
> — Z et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_17d4bd9d -->

---

## 2. Mapping candidates

### 4a. Candidate overview

| Rank | WMBv1 candidate | Level | Cells (MPN) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] | SUPERTYPE | n=47 at MBA:515 | 🔴 LOW | Calb1 CONSISTENT; Th DISCORDANT | Speculative |
| 2 | 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] | CLUSTER | n=22 at MBA:515 | 🔴 LOW | Calb1 CONSISTENT; Th DISCORDANT; MFR CONSISTENT | Speculative |

Both edges are PARTIAL_OVERLAP / Speculative. 2 edges total; no MODERATE or HIGH edges.

### 4b. Property alignment — SUPT_0423 (primary) and CLUS_1550 (best cluster)

| Property | Classical | SUPT_0423 | CLUS_1550 | Alignment |
|---|---|---|---|---|
| Soma location | MBA:515 (MPN; SDN-POA is histological subnucleus) | MBA:515 n=47; also BNST n=18, AHN n=46, PVN n=31 | MBA:515 n=22 (primary soma); also PVH n=9, PVHap n=4 | APPROXIMATE |
| Calb1 expression | POSITIVE (protein, primary defining marker) | mean_expression=6.42 (DEFINING_SCOPED atlas marker) | mean_expression=6.66 | CONSISTENT |
| Th expression | ABSENT (negative marker; no TH cell bodies in SDN-POA) | mean_expression=0.99 | mean_expression=2.75 | DISCORDANT |
| Sex ratio | Male-biased (SDN-POA larger in males) | not available | MFR=3.35 [CS20230722_CLUS_1550] (male-biased) | CONSISTENT |
| Annotation transfer | — | NOT_ASSESSED | NOT_ASSESSED | — |

---

## 5. Candidate paragraphs

## 0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] · 🔴 LOW

**Supporting evidence**

- SUPT_0423 is the only anatomically plausible rank-1 candidate for sdn_poa_calbindin_neuron identified by taxonomy DB search (DB score = 1). The search filtered on MBA:515 (MPN) at supertype level; SUPT_0423 was the sole survivor.
- Calb1 mean_expression = 6.42 in SUPT_0423 is consistent with Calb1 as the primary defining marker of the SDN-POA. Calb1 is annotated as a DEFINING_SCOPED atlas marker for this supertype.
- MBA:515 (MPN) is represented with 47 cells in SUPT_0423, confirming at least a partial spatial overlap with the classical anatomical location. The SDN-POA occupies the dorsomedial MPN and is contained within this region, so the supertype plausibly includes SDN-POA cells.

**Marker evidence provenance**

- **Calb1:** Evidence is protein-level (immunohistochemistry with anti-calbindin-D28K antibody) [2]. The study identified the SDN-POA as a Calb1+ cluster within the MPN; cell identity was confirmed by cytoarchitectural position (dorsomedial MPN) and male-biased cell number, both hallmarks of the SDN-POA. The atlas marker (mean_expression=6.42, DEFINING_SCOPED) is transcript-level from scRNA-seq; the protein–transcript alignment is expected but not formally cross-validated here.
- **Th (negative marker):** Evidence is protein-level (IHC; "no TH-positive cells were found" [2]). The quote is from the same study that defined the Calb1 marker. At supertype level, SUPT_0423 shows Th mean_expression = 0.99, which is DISCORDANT. However, SUPT_0423 spans BST, AHN, and PVN in addition to MPN; Th-expressing cells in these non-MPN compartments plausibly drive the non-zero mean. Without single-cell spatial decomposition, the Th signal cannot be attributed specifically to MPN-localised cells. *(note: TH neurons are well-documented in the periventricular hypothalamus and BNST but are not expected in the MPN proper — the discordance is therefore more likely due to multi-region cluster composition than to genuine SDN-POA Th expression.)*

**Concerns**

- **Th DISCORDANT at supertype level.** SUPT_0423 shows Th mean_expression = 0.99 against the classical Th NEGATIVE assertion. Th discordance persists — and worsens — at cluster level: child cluster CLUS_1550 shows Th = 2.75. The most parsimonious explanation is contamination from Th-positive cells in the BST/AHN/PVN components of this multi-region supertype rather than from MPN-proper cells, but this cannot be confirmed without spatial inspection of the Th channel in MERFISH data.
- **Location APPROXIMATE.** SUPT_0423 is distributed across MBA:515 (MPN, n=47), BNST (n=18), AHN (n=46), and PVN (n=31). The MPN cells are anatomically the most plausible SDN-POA candidates, but the supertype as a whole spans well beyond MPN. *(note: BNST and AHN are adjacent preoptic/hypothalamic regions; PVN is more caudal and ventral but still within the hypothalamic continuum — this is weak rather than strong counter-evidence for MPN identity.)*
- **MERFISH registration.** The SDN-POA is a cytoarchitectonically defined subnucleus within MPN. WMBv1 MERFISH parcellation does not resolve it as a distinct spatial domain; any match is necessarily at MPN level.
- **Calb1 not specific.** Calb1 is expressed broadly across the brain and is classified as DEFINING_SCOPED (not DEFINING) for SUPT_0423. It cannot distinguish SDN-POA neurons from other Calb1+ MPN neurons.
- **Sex ratio not assessable at supertype level.** MFR is a rank-0 (cluster-level) metric; no per-sex cell count is available for SUPT_0423.

**What would upgrade confidence**

- A child cluster of SUPT_0423 with MBA:515 as primary soma, high Calb1, low/absent Th, and male-biased MFR would substantially improve the mapping (see CLUS_1550 below, which meets the Calb1 and MFR criteria but retains Th discordance).
- Spatial inspection of SUPT_0423 MERFISH cells in MBA:515 for sub-regional clustering at the dorsomedial MPN position (MERFISH spatial analysis — see Proposed experiments).
- MapMyCells annotation transfer of a Calb1-Cre or SDN-POA-targeted scRNA-seq dataset to assess F1 >= 0.80 against SUPT_0423, which would add `AnnotationTransferEvidence` to this edge.
- A primary literature search for transcriptomic markers co-expressed with Calb1 specifically in SDN-POA neurons — the current evidence base has only two general citations [1], [2] and lacks a primary single-cell or spatial transcriptomics study of SDN-POA.

---

## 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] · 🔴 LOW

**Supporting evidence**

- CLUS_1550 is the only child cluster of SUPT_0423 with MBA:515 (MPN) as its primary soma (n=22 cells), making it the best available atlas resolution for the SDN-POA within the WMBv1 taxonomy.
- Calb1 mean_expression = 6.66 is consistent with the Calb1 defining marker; this is the highest Calb1 value among SUPT_0423 child clusters and matches the primary classical assertion.
- Male:female ratio = 3.35 for CLUS_1550 — a clear male bias consistent with the MALE_BIASED sex_bias assertion of sdn_poa_calbindin_neuron. This is the only quantitative sex-ratio evidence in the mapping and is a meaningful convergent signal given that the SDN-POA is defined precisely by male-biased cell number dimorphism.

**Marker evidence provenance**

- **Calb1 (CLUS_1550):** Transcript-level mean_expression = 6.66 from WMBv1 precomputed stats. The classical assertion is protein-level (IHC [2]). Protein–transcript cross-validation not performed; alignment is expected but not formally confirmed.
- **Th (CLUS_1550):** Th mean_expression = 2.75 — higher than at supertype level (0.99) — is DISCORDANT with the classical Th NEGATIVE assertion. The cluster spans MPN (n=22), PVH (n=9), and PVHap (n=4) in addition to unspecified hypothalamic cells (n=9). PVH/PVHap are known Th-expressing compartments *(note: Th neurons in the periventricular zone, including PVH/PVHap, are well-established; Th expression in MPN-proper is unexpected but cannot be excluded from the current atlas metadata alone)*. Whether the Th signal originates from MPN cells or from PVH/PVHap components of CLUS_1550 cannot be determined without single-cell spatial channel inspection.

**Concerns**

- **Th DISCORDANT (primary concern).** Th = 2.75 in CLUS_1550 is the principal barrier to higher confidence. This is a stronger Th signal than at supertype level (0.99) and represents the most concrete disqualifying evidence for the mapping. Until MERFISH spatial analysis confirms that Th expression in CLUS_1550 is restricted to non-MPN cells (PVH/PVHap), the Th discordance cannot be explained away.
- **Cluster not MPN-restricted.** CLUS_1550 cells distribute across MPN (n=22), PVH (n=9), PVHap (n=4), and unspecified hypothalamic regions (n=9). The cluster contains non-SDN-POA cells, and atlas marker averages are influenced by those populations.
- **SDN-POA not spatially resolvable in WMBv1.** Even within the 22 MPN-localised cells of CLUS_1550, the dorsomedial SDN-POA cytoarchitectonic zone cannot be confirmed from MERFISH registration alone.
- **Small MPN cell count.** n=22 MPN-primary cells in CLUS_1550 is a small sample; expression averages and MFR may not be stable estimates.
- **Annotation transfer NOT_ASSESSED.** No MapMyCells run has been performed for this node; the F1 score at cluster level is unknown.

**What would upgrade confidence**

- MERFISH spatial channel inspection of Th in CLUS_1550 cells assigned to MBA:515: if Th signal is confined to PVH/PVHap cells and absent from MPN cells, the Th discordance would be resolved and confidence could be upgraded toward MODERATE.
- MapMyCells annotation transfer of MPN Calb1+ or SDN-POA-targeted scRNA-seq data, targeting F1 >= 0.80 at CLUSTER level against CLUS_1550, which would add `AnnotationTransferEvidence` to this edge (see Proposed experiments).
- Identification of additional molecular markers co-expressed with Calb1 in the SDN-POA from primary literature (cite-traverse recommended: "calbindin SDN-POA preoptic transcriptome").

---

## 6. Proposed experiments

### MERFISH spatial channel inspection (Th)

| | |
|---|---|
| **What** | Inspect the Th fluorescence channel in WMBv1 MERFISH data for CLUS_1550 cells assigned to MBA:515 (MPN, n=22), testing whether Th expression co-localises with MPN cells or is restricted to PVH/PVHap cells within the cluster |
| **Target** | Th signal absent or near-zero in MBA:515-assigned CLUS_1550 cells |
| **Expected output** | Spatial decomposition of Th expression by assigned region within CLUS_1550; would distinguish SDN-POA-plausible cells from non-MPN contaminating cells |
| **Resolves** | Th DISCORDANT concern on both edges; if resolved, would be the single most important upgrade for CLUS_1550 edge confidence |

### MapMyCells annotation transfer

| | |
|---|---|
| **What** | MapMyCells annotation transfer of a Calb1-Cre, SDN-POA-targeted, or MPN scRNA-seq dataset to WMBv1 CCN20230722 taxonomy |
| **Target** | F1 >= 0.80 at CLUSTER level against CS20230722_CLUS_1550 |
| **Expected output** | `AnnotationTransferEvidence` entry on edge_sdn_poa_calbindin_neuron_to_cs20230722_clus_1550 and edge_sdn_poa_calbindin_neuron_to_cs20230722_supt_0423 |
| **Resolves** | Annotation transfer NOT_ASSESSED on both edges; would provide direct transcriptomic bridging evidence |

### MERFISH sub-regional clustering

| | |
|---|---|
| **What** | Spatial inspection of all SUPT_0423 cells in MBA:515 (n=47) for a sub-regional cluster at the dorsomedial MPN position corresponding to the known SDN-POA cytoarchitecture |
| **Target** | A spatially coherent cluster at dorsomedial MPN, male-biased, Calb1-high, Th-low |
| **Expected output** | Confirmation that CLUS_1550 (or a subset thereof) occupies SDN-POA cytoarchitectonic territory; would upgrade location alignment from APPROXIMATE to CONSISTENT |
| **Resolves** | MERFISH registration uncertainty caveat on both edges; open question 3 |

---

## 7. Open questions

1. Do CLUS_1550 cells assigned to MBA:515 (MPN) express Th, or does the Th=2.75 signal originate exclusively from the PVH/PVHap components of this multi-region cluster? *(edges: both)*
2. Can sub-regional MERFISH spatial data distinguish SDN-POA dorsomedial cells from other MPN Calb1+ neurons within CLUS_1550? *(edges: both)*
3. Do any clusters within SUPT_0423 show peak Calb1 co-located with MBA:515 and a male-biased sex ratio consistent with SDN-POA identity — and if so, is CLUS_1550 the best or only such cluster? *(edge: SUPT_0423)*

---

## 8. Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_sdn_poa_calbindin_neuron_to_cs20230722_supt_0423 | ATLAS_METADATA | WEAK |
| edge_sdn_poa_calbindin_neuron_to_cs20230722_clus_1550 | ATLAS_METADATA | WEAK |

Both edges are supported by atlas metadata only. No literature evidence items are attached to either edge; literature citations appear on the classical node only.

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | P et al. 2015 | [26672480](https://pubmed.ncbi.nlm.nih.gov/26672480/) | Soma location; SDN-POA sexual dimorphism |
| [2] | Z et al. 2013 | [25206587](https://pubmed.ncbi.nlm.nih.gov/25206587/) | Soma location; Calb1 defining marker; Th negative marker; cross-species homology |

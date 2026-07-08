# Oriens-oriens (O-O) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | stratum oriens of hippocampus [UBERON:0014548] (CA1) | — |
| NT | GABAergic | — |
| Markers | Sst+, Nos1+ | [1] |

**Node notes:** Stub from cite-traverse (2026-04-10). The O-O cell is a GABAergic interneuron defined by soma and axon confinement to stratum oriens, characterised by Chamberland et al. 2024 [1] using intersectional Sst;;Nos1 Cre/Flp genetics; 12 of 15 cells matching this label were consistent with O-O morphological description. The O-O cell is distinguished from OLM cells by axon confinement to stratum oriens rather than projection to stratum lacunosum-moleculare. Evidence for this as a discrete classical type is thin — a single study with n=12–15 cells.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — | ⚪ UNCERTAIN | Sst CONSISTENT · Nos1 APPROXIMATE · location APPROXIMATE | Eliminated — plausible but unconfirmed |

1 edge total · relationship type: UNCERTAIN. No MODERATE or LOW candidates were established.

---

## Eliminated candidates

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] — ⚪ UNCERTAIN

The primary shared disqualifying signal is the absence of Nos1 confirmation at atlas level combined with a CA3 versus CA1 subregional mismatch.

**Supporting evidence**

- Sst expression strongly consistent: precomputed stats mean=10.17 for SUPT_0219 [CS20230722_SUPT_0219], matching the Sst-positive identity of O-O cells [1].
- SUPT_0219 belongs to the Sst Gaba subclass, consistent with the GABAergic/Sst interneuron classification of O-O cells. NT type: CONSISTENT.
- Annotation transfer (MapMyCells; Yao 2021 Sst SSv4, GEO:GSE185862, n=273 HIP cells): Sst subclass maps to WMBv1 with high fidelity at subclass level (F1=0.983, 265 cells to 053 Sst Gaba). At supertype level, SUPT_0219 is the dominant annotation transfer target within this subclass (F1=0.759, 161/273 cells, purity=0.964), indicating it captures the largest fraction of hippocampal Sst interneurons in the Yao 2021 dataset.

**Marker evidence provenance**

- **Sst:** Defined via intersectional Sst-Cre genetics by Chamberland et al. 2024 [1]. Precomputed stats (mean=10.17) confirm strong atlas-side Sst expression. Strongest molecular anchor for this proposed correspondence.
- **Nos1:** The second arm of the Sst;;Nos1 intersectional label used to isolate O-O cells [1], and the key feature distinguishing them from OLM and other Sst+ CA1 interneuron types. SUPT_0219 [CS20230722_SUPT_0219] does not list Nos1 among its defining markers; precomputed stats show a low mean=1.81 (alignment: APPROXIMATE). Whether this reflects genuine absence, heterogeneous expression within the supertype, or sub-threshold detection at supertype resolution is unknown.
- **Id3, Sp9 (atlas-defined markers of SUPT_0219):** No correspondence established in O-O classical literature — both are NOT_ASSESSED.
- **Annotation transfer caveat:** The annotation transfer source (Yao 2021 SSv4 Sst subclass) pools OLM, bistratified, hippocampo-septal, oriens-oriens, and other Sst interneuron types. Supertype-level resolution cannot discriminate O-O cells from co-resident Sst+ types.

**Concerns**

- **Subregional mismatch (APPROXIMATE):** O-O cells were characterised in CA1 stratum oriens [UBERON:0014548] [1]. SUPT_0219 [CS20230722_SUPT_0219] is CA3-enriched: top location is Field CA3, stratum oriens (305 cells), with no prominent CA1 SO entry. *(note: CA3 and CA1 are adjacent hippocampal subfields, but the CA3 versus CA1 distinction is a real anatomical difference — this is a meaningful subregional discrepancy, not a registration boundary error.)*
- **Nos1 not confirmed at atlas level:** The low Nos1 mean (1.81) is concerning given that Sst+/Nos1+ co-expression is the defining intersectional signature used to isolate O-O cells [1]. A different supertype or cluster with higher Nos1 may be a better candidate.
- **Single-study evidence base (OTHER caveat):** O-O cell as a classically distinct type is supported by one study [1] with a small cell sample. Robustness of the Sst+/Nos1+ definition and its distinctness from other CA1 Sst+ interneurons awaits independent replication.
- **Supertype resolution insufficient (MARKER_NOT_SPECIFIC caveat):** Without Nos1 verification at atlas level, which supertype within the Sst Gaba subclass — if any — specifically captures the O-O cell population remains unclear.

**What would upgrade confidence**

- Demonstration of Nos1 expression in SUPT_0219 [CS20230722_SUPT_0219] at cluster level (cluster-level precomputed stats or scRNA-seq re-analysis of a Sst;;Nos1 intersectional dataset mapped to WMBv1) would be required to move to LOW confidence.
- Identification of a CA1 stratum oriens-enriched Sst+/Nos1+ supertype or cluster within the Sst Gaba subclass could shift the primary mapping candidate and raise confidence to LOW or MODERATE.
- Independent replication of the O-O cell morphological and molecular phenotype — ideally from a publicly available single-cell dataset with morphologically identified neurons — would strengthen the classical-side evidence sufficiently to attempt a more definitive mapping.

---

## Proposed experiments

### Intersectional genetics + transcriptomics
- **What:** scRNA-seq or snRNA-seq from Sst-Cre;;Nos1-Flp intersectional mouse hippocampus (CA1 enriched); map to WMBv1 using MapMyCells
- **Target:** Identify the supertype(s) capturing the O-O population directly
- **Expected output:** AnnotationTransferEvidence on this edge; or identification of a better-fitting supertype
- **Resolves:** Q1 (Nos1 penetrance in SUPT_0219), Q3 (whether a CA1 SO Sst+/Nos1+ supertype exists)

### Atlas cluster re-analysis
- **What:** Inspect cluster-level (not supertype-level) Nos1 expression within the Sst Gaba subclass; identify any cluster with high Nos1 mean and hippocampal CA1 SO enrichment
- **Target:** Cluster with Nos1 mean substantially above the 1.81 supertype mean and CA1 SO cells
- **Expected output:** Candidate replacement cluster for SUPT_0219 [CS20230722_SUPT_0219] as primary O-O cell mapping target
- **Resolves:** Q1, Q3

### Multiplex FISH
- **What:** HiPlex RNAscope co-staining of CA1 and CA3 stratum oriens for Sst + Nos1 + Id3 + Sp9
- **Target:** Confirm whether Nos1-co-expressing Sst cells occur within Id3/Sp9-expressing clusters
- **Expected output:** Spatial validation that SUPT_0219 [CS20230722_SUPT_0219] contains a Nos1+ subpopulation in CA1 SO; or identification of a different supertype cluster
- **Resolves:** Q1, Q2

---

## Open questions

1. Does SUPT_0219 [CS20230722_SUPT_0219] express Nos1 at meaningful penetrance? If so, is this confined to a specific cluster within the supertype?
2. Are the CA3 stratum oriens cells in SUPT_0219 [CS20230722_SUPT_0219] analogous to the CA1 O-O cells described by Chamberland et al. 2024 [1], or does the CA3 enrichment reflect a functionally distinct population?
3. Is there a CA1 stratum oriens-enriched Sst+/Nos1+ supertype in WMBv1 that better matches O-O cell identity than SUPT_0219 [CS20230722_SUPT_0219]?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA — supertype marker and anatomy comparison | PARTIAL |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA — precomputed stats cross-check (Sst=10.17, Nos1=1.81) | PARTIAL |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | ANNOTATION_TRANSFER — MapMyCells · GEO:GSE185862 · Sst subclass n=273 HIP cells | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker; intersectional Sst;;Nos1 O-O cell identification |

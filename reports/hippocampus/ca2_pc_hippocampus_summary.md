# CA2 pyramidal cell

**⚠ Draft mappings — confidence labels reflect current evidence only and will be revised.**

---

## Classical type summary

| Field | Value | Source |
|---|---|---|
| Definition basis | CLASSICAL_MULTIMODAL | — |
| Neurotransmitter | Glutamatergic | [4] |
| Soma location | Stratum pyramidale of CA2 (UBERON:0014549) | [1][2][3] |
| Defining markers | Pcp4, Rgs14, Amigo2 | [5][6] |
| Negative markers | None recorded | — |
| Neuropeptides | None recorded | — |
| Electrophysiology class | Not specified | — |

CA2 pyramidal cells are glutamatergic principal neurons whose somata reside in the pyramidal layer of hippocampal subfield CA2, a compact region interposed between CA1 and CA3.

> "CA2 area is a small region located between CA1 and CA3 neurons that receives input from the dentate gyrus and from the entorhinal cortex and projects to CA1 pyramidal neurons."
> <!-- quote_key: 18555666_d095397d -->
> *— Colciago et al. 2016 · CorpusId:18555666*

Like all pyramidal neurons of Ammon's horn, CA2 cells are glutamatergic:

> "There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG."
> <!-- quote_key: 2281033_5b9805ff -->
> *— Dale et al. 2015 · PMID:26346726*

CA2 pyramidal cells are set apart from CA1 and CA3 neighbours by a distinctive molecular signature centred on Pcp4, Rgs14, and Amigo2:

> "Here we report identification of the CA2 region in the mouse by immunostaining with a Purkinje cell protein 4 (PCP4) antibody, which effectively delineates CA3/CA2 and CA2/CA1 borders and agrees well with previous cytoarchitectural definitions of CA2."
> <!-- quote_key: 18746823_614030d2 -->
> *— Antonio et al. 2014 · PMID:24166578*

> "These markers include Purkinje cell protein 4 (PCP4), neurotrophin 3, fibroblast growth factor, a-actinin 2, adenosine A1 receptor, vasopressin 1b receptor, RGS14 (regulator of G-protein signaling 14), and amigo2. These markers are specifically or more prominently expressed in the distal portion of regio inferior corresponding roughly to Lorente de Nó's CA2."
> <!-- quote_key: 18746823_8ba0bf29 -->
> *— Antonio et al. 2014 · PMID:24166578*

> "a number of genes, including the regulator of G-protein signaling 14 (RGS14), Amigo2, PCP4, TARP5, FGF5, and several adenylyl cyclases (e.g., adcy1, adcy5, and adcy6), are highly expressed in CA2."
> <!-- quote_key: 20853920_44ab38bb -->
> *— Caruana et al. 2012 · PMID:22904370*

---

## Mapping candidates

### CS20230722_SUPT_0100 (0100 CA2-FC-IG Glut_1) — MODERATE

**Relationship:** PARTIAL_OVERLAP | **Verdict:** Best candidate

**Atlas metadata.** SUPT_0100 belongs to subclass CS20230722_SUBC_025 (025 CA2-FC-IG Glut), which groups CA2 together with fasciola cinerea (FC) and indusium griseum (IG) glutamatergic populations in WMBv1 (CCN20230722). This supertype received the highest discovery score (4) among all queried WMBv1 supertypes.

**Supporting evidence.**

*Neurotransmitter type (CONSISTENT).* Both the classical type and SUPT_0100 are glutamatergic, consistent with the CA2-FC-IG Glut subclass designation [4].

*Anatomical location (APPROXIMATE).* SUPT_0100 has 446 cells in Field CA2, pyramidal layer (MBA:446), directly consistent with the CA2 stratum pyramidale soma location of classical CA2 pyramidal cells [1][2][3]. However, the supertype also registers substantial off-target counts: 292 cells in Field CA1, stratum oriens (MBA:399); 215 cells in Field CA3, stratum oriens (MBA:486); 165 cells in Field CA3, pyramidal layer (MBA:495). CA2 pyramidal layer is the largest single compartment but does not dominate the total.

> "For CA2, we identified some pyramidal cells at the CA3c region while others distributed along the intermediate (CA3b) and distal (CA3a) subregions."
> <!-- quote_key: 233984943_56acd5f8 -->
> *— Sanchez-Aguilera et al. 2021 · PMID:33956790*

*Marker expression (CONSISTENT for all three CA2 markers, confirmed by precomputed expression).* The WMBv1 defining markers for SUPT_0100 are Lefty1, Il16, and Etv1; the canonical CA2 markers do not appear in that list. However, precomputed expression statistics queried from `precomputed_stats.h5` at the supertype level confirm high mean expression of all three CA2-selective markers in SUPT_0100:

| Marker | Mean expression in SUPT_0100 | Classical role |
|---|---|---|
| Pcp4 | 11.26 | CA2 region delineator [5] |
| Rgs14 | 8.84 | CA2-selective marker [5] |
| Amigo2 | 7.39 | CA2-enriched transcript [6] |

These values were confirmed by `add-expression` (precomputed_stats.h5, supertype level) and constitute the primary basis for upgrading confidence from LOW to MODERATE.

> "we profiled transcriptomes at both dorsal and ventral poles, producing a cell-class- and region-specific transcriptional description for these populations."
> <!-- quote_key: 4875295_8cb069d9 -->
> *— Cembrowski et al. 2016 · PMID:27113915*

*Annotation transfer.* Annotation transfer of the Yao 2021 (GSE185862) CA2-IG-FC subclass label (n=19 cells) mapped 94.7% of cells to SUPT_0101 (0101 CA2-FC-IG Glut_2, F1=0.947), not to SUPT_0100 (F1=0.1). This result requires careful interpretation: SUPT_0101 MERFISH anatomy shows 0 cells in CA2 pyramidal layer (MBA:446) and is dominated by Fasciola cinerea (175 cells) and Indusium griseum (61 cells), whereas SUPT_0100 has 106 CA2 pyramidal layer cells and 0 FC/IG cells. The AT result therefore reflects the FC/IG component of the mixed Yao CA2-IG-FC label mapping to the FC/IG-enriched atlas supertype SUPT_0101, not a failure of SUPT_0100 as the CA2 pyramidal cell target. A CA2-specific dataset is required for a definitive test.

**Concerns.**

1. **FC/IG conflation (DISCORDANT_ANATOMY).** The SUPT_0100 name explicitly includes FC (fasciola cinerea) and IG (indusium griseum). These are small CA2-adjacent archicortical structures distinct from classical CA2 pyramidal cells. The PARTIAL_OVERLAP relationship reflects uncertainty about whether SUPT_0100 cleanly captures CA2 PCs or conflates them with FC/IG populations.

2. **Off-target MERFISH cells.** The large numbers of SUPT_0100 cells in CA1 and CA3 strata (combined >670 versus 446 in CA2 pyramidal layer) could reflect: genuine deep CA3c neurons near the CA2 border, MERFISH registration noise at subfield boundaries, or contamination by FC/IG cells whose MERFISH coordinates fall outside CA2. Orthogonal spatial validation is needed to distinguish these scenarios.

3. **Indirect annotation transfer.** No clean CA2-only AT result exists yet for SUPT_0100. The available GSE185862 result uses a mixed CA2-IG-FC label and is therefore not informative about the CA2 pyramidal cell component specifically.

**Upgrade criteria.**

- Annotation transfer from a CA2-specific dataset (e.g. Caramello 2024 CA2 scRNA-seq, or Yao CA2 cells isolated from the mixed label) showing F1 ≥ 0.70 for SUPT_0100 would upgrade confidence to HIGH.
- FISH or smFISH validation of Rgs14 or Amigo2 co-expression in MERFISH-assigned SUPT_0100 cells in the CA2 pyramidal layer would further consolidate the MODERATE confidence.
- Resolution of the FC/IG supertype composition (determining whether FC/IG cells segregate cleanly to SUPT_0101 and away from SUPT_0100) would clarify the PARTIAL_OVERLAP scope.

---

## Proposed experiments

1. **CA2-specific annotation transfer.** Run MapMyCells (WMBv1 CCN20230722) on a dataset with a clean CA2-only label — e.g. Caramello 2024 CA2 scRNA-seq, or Yao 2021 CA2 cells isolated by spatial filtering from the CA2-IG-FC label. Target: F1 ≥ 0.70 at supertype level for SUPT_0100. This is the highest-priority step to confirm or upgrade the MODERATE confidence and to definitively distinguish SUPT_0100 from SUPT_0101 as the CA2 pyramidal cell target.

2. **FISH validation of CA2 markers in SUPT_0100-assigned cells.** Perform smFISH or RNAscope for Rgs14 and Pcp4 in the CA2 pyramidal layer. Confirm that MERFISH-assigned SUPT_0100 cells co-express these markers. This provides orthogonal spatial confirmation of the precomputed expression evidence and would address the FC/IG conflation concern directly.

3. **Resolve FC/IG composition within SUBC_025.** Examine cluster-level MERFISH anatomy within subclass CS20230722_SUBC_025 to determine whether FC and IG populations segregate cleanly to specific supertypes (e.g. SUPT_0101) or are also present within SUPT_0100. This would clarify the boundary of the PARTIAL_OVERLAP relationship.

---

## Open questions

- Do SUPT_0100 cells in CA1 and CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near the CA2 border) or MERFISH registration errors? The high Pcp4 and Rgs14 mean expression in SUPT_0100 suggests these are real CA2-identity cells, but FISH confirmation is needed.
- What is the functional and transcriptomic relationship between CA2 pyramidal cells and the FC/IG populations grouped in SUBC_025? Are they sufficiently similar to justify a shared subclass, or does the atlas grouping reflect a limitation of clustering resolution?
- Can the Sanchez-Aguilera et al. 2021 [3] observation of CA2-like pyramidal cells at the CA3c region be explained by CA2-border sampling, and do those border cells express canonical CA2 markers such as Rgs14 and Amigo2?

---

## Evidence base

| Evidence type | Source | Summary |
|---|---|---|
| ATLAS_METADATA | WMBv1 SUPT_0100 (discovery score 4) | NT CONSISTENT; 446 CA2 pyramidal layer cells (APPROXIMATE location due to off-target counts) |
| PRECOMPUTED_EXPRESSION | precomputed_stats.h5, supertype level | Pcp4 11.26, Rgs14 8.84, Amigo2 7.39 in SUPT_0100 — all three CA2 markers CONSISTENT |
| ANNOTATION_TRANSFER | GSE185862 CA2-IG-FC mixed label | SUPT_0101 F1=0.947; SUPT_0100 F1=0.1; result reflects FC/IG component, not CA2 PC specificity |
| LITERATURE | [4] Dale et al. 2015 | Glutamatergic neurotransmitter type |
| LITERATURE | [5] Antonio et al. 2014 | Pcp4 and Rgs14 as CA2-selective markers |
| LITERATURE | [6] Caruana et al. 2012 | Amigo2 as CA2-enriched transcript |

---

## References

1. Cembrowski et al. 2016. Hipposeq: a comprehensive RNA-seq database of gene expression in hippocampal principal neurons. *eLife* 5:e14997. PMID:27113915. DOI:10.7554/eLife.14997
2. Colciago et al. 2016. Neurosteroids Involvement in the Epigenetic Control of Memory Formation and Storage. CorpusId:18555666
3. Sanchez-Aguilera et al. 2021. An update to Hippocampome.org by integrating single-cell phenotypes with circuit function in vivo. PMID:33956790
4. Dale et al. 2015. Effects of serotonin in the hippocampus: how SSRIs and multimodal antidepressants might regulate pyramidal cell function. PMID:26346726. DOI:10.1017/S1092852915000425
5. Antonio et al. 2014. Distinct physiological and developmental properties of hippocampal CA2 subfield revealed by using anti-Purkinje cell protein 4 (PCP4) immunostaining. *J Comp Neurol* 522:1333–1354. PMID:24166578. DOI:10.1002/cne.23486
6. Caruana et al. 2012. New insights into the regulation of synaptic plasticity from an unexpected place: hippocampal area CA2. *Learn Mem* 19:391–400. PMID:22904370. DOI:10.1101/lm.025304.111

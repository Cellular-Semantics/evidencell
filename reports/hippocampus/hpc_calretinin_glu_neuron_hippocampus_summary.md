# hippocampal calretinin-positive glutamatergic neuron — WMBv1 (CCN20230722) Mapping Report

## Introduction

Calretinin-positive (Calb2+) glutamatergic neurons of the hippocampal formation occupy the stratum lacunosum-moleculare (SLM) and outer molecular layer (OML), where they constitute an excitatory pathway that flows against the classical trisynaptic circuit direction. Unlike the larger population of calretinin-positive GABAergic interneurons, these cells are glutamatergic and include both local-projecting and long-range subpopulations spanning the SLM, OML, and subicular complex.

### Classical type table

| Property | Value | References |
|---|---|---|
| Neurotransmitter | Glutamatergic | — |
| Defining marker | Calb2 (calretinin) | — |
| Soma location | Hippocampal formation [UBERON:0002421]; stratum lacunosum-moleculare / outer molecular layer | [1], [2] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

> Notably, CR cells provide the first evidence of intrinsic glutamatergic hippocampal connections that flow against the classical trisynaptic circuit direction (Anstotz et al., 2015)(Ceranik et al., 1997).
> — Ceranik et al. 1997, Specialized Glutamatergic Populations · [2] <!-- quote_key: 393787_0325d3d4 -->

</details>

### Cell Ontology mapping

| Field | Value |
|---|---|
| CL term | glutamatergic neuron (CL:0000679) |
| Mapping type | BROAD |
| Mapping notes | No calretinin-positive glutamatergic-specific CL term exists; CL:0000679 is the broadest accurate assignment. |

---

## Results

A single WMBv1 candidate was identified: supertype 0135 HPF CR Glut_1 [CS20230722_SUPT_0135]. Atlas metadata and MapMyCells annotation transfer both converge on this target, though confidence remains LOW given the small reference cell count, absent VGluT3 expression, and the ambiguous Cajal-Retzius designation of the WMBv1 subclass.

![Annotation transfer F1 heatmap (GEO:GSE95315 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_tree.png)

### Candidate overview table

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 0135 HPF CR Glut_1 | CS20230722_SUPT_0135 | 🔴 LOW | PARTIAL_OVERLAP | Speculative |

### Property alignment — 0135 HPF CR Glut_1 [CS20230722_SUPT_0135]

**Table 1: Property comparison**

| Property | Classical type | WMBv1 SUPT_0135 | Alignment |
|---|---|---|---|
| Neurotransmitter | Glutamatergic | Glutamatergic (HPF CR Glut subclass) | CONSISTENT |
| Soma location | SLM / outer molecular layer (UBERON:0002421) | Only WMBv1 Glut supertype outside DG/CA/SUB subclasses; MERFISH not assessed | APPROXIMATE |
| Marker — Calb2 | Defining | Mean 4.5–8.2 UMIs/cell across 5 clusters; highest Calb2 among all HPF Glut supertypes (30–100× above DG Glut) | CONSISTENT |

**Table 2: Evidence support**

| Evidence type | Supports | Summary |
|---|---|---|
| ATLAS_METADATA | SUPPORT | SUPT_0135 only HPF Glut supertype outside DG/CA1/CA2/CA3/SUB subclasses; high Calb2 + Reln/Trp73 consistent with SLM/OML identity |
| ANNOTATION_TRANSFER | SUPPORT | Hochgerner 2018 "Cajal-Retzius" cluster (n=33, GEO:GSE95315) maps exclusively to HPF CR Glut lineage: F1=0.985 at subclass, F1=1.0 at cluster rank |

**MapMyCells F1 by level — Cajal-Retzius source cluster (n=33 cells, GEO:GSE95315)**

| Level | Best target | F1 | Group purity | Target purity | n cells mapped |
|---|---|---|---|---|---|
| CLASS | 03 OB-CR Glut | 1.000 | 1.00 | 1.00 | 15 |
| SUBCLASS | 036 HPF CR Glut | 0.985 | 1.00 | 0.97 | 33 |
| SUPERTYPE | 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] | 0.985 | 1.00 | 0.97 | 33 |
| CLUSTER | 0497 HPF CR Glut_1 | 1.000 | 1.00 | 1.00 | 13 |

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Hippocampal calretinin-positive glutamatergic neurons defined as CLASSICAL_MULTIMODAL. Key references: Wheeler et al. 2015 (PMID:26402459); Ceranik et al. 1997 (PMID:9204922). Note: Calb2 marker and NT-type entries carry no primary citations in the current KB node — a targeted cite-traverse for "calretinin glutamatergic stratum lacunosum-moleculare" is recommended.

**Atlas mapping query.** Candidate search in WMBv1 (CCN20230722) at supertype rank, querying HPF-located glutamatergic supertypes. SUPT_0135 identified as the only HPF Glut supertype outside the DG, CA1-ProS, CA2-FC-IG, CA3, and SUB-ProS subclasses.

**Property alignment.** Calb2, Reln, and Trp73 mean expression retrieved from precomputed_stats.h5 (CCN20230722) at supertype level.

**Annotation transfer.**

| Run | Dataset | Source label | n cells | Method | Tool |
|---|---|---|---|---|---|
| at_run_20260427_hochgerner2018_dg_mmc_wmbv1 | GEO:GSE95315 (Hochgerner 2018, mouse DG) | Cajal-Retzius | 33 | MapMyCells local, raw normalization, 100 bootstrap iterations | cell_type_mapper v1.7.1 |

Atlas pseudobulk SHA: b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b. Code: https://github.com/AllenInstitute/cell_type_mapper

**Anti-hallucination.** All accessions, quote keys, and PMIDs validated against the KB reference store at write time.

*Report generated 2026-05-19. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`.*

**Evidence base**

| Evidence type | Count |
|---|---|
| ATLAS_METADATA | 1 |
| ANNOTATION_TRANSFER | 1 |

</details>

---

## Discussion

**The speculative best candidate is 0135 HPF CR Glut_1 [CS20230722_SUPT_0135]**, supported by high Calb2 expression (the primary defining marker) and near-perfect annotation transfer from Cajal-Retzius cells in the Hochgerner 2018 dataset. However, several factors keep confidence at LOW: (1) SUPT_0135 reference cells strongly co-express Reln and Trp73, canonical Cajal-Retzius markers associated with developmentally transient cells largely absent in adult rodent hippocampus; (2) Slc17a8 (VGluT3), reported in some descriptions of SLM glutamatergic neurons, is essentially absent from SUPT_0135 (0–0.3 UMIs in only 2/5 clusters); and (3) the reference population is extremely small (n=5 cells total, one per cluster), limiting all statistical inference. The central unresolved question is whether SUPT_0135 captures Cajal-Retzius remnants sampled during adult brain profiling, or represents the Calb2+ glutamatergic population described in adult SLM/OML.

### Proposed experiments

1. Run MapMyCells annotation transfer from a source dataset containing validated Calb2+/Slc17a8+ adult SLM glutamatergic cells onto WMBv1, to determine whether these cells segregate to SUPT_0135 or disperse to other supertypes.
2. Inspect WMBv1 MERFISH soma location data for SUPT_0135 cells via the ABC Atlas browser to confirm SLM/OML placement and assess whether an exclusively developmental origin is consistent.
3. Perform ISH co-localisation of Trp73 and Calb2 in adult mouse SLM/OML to determine whether Trp73-expressing cells survive into adulthood and whether they overlap with a Slc17a8+ glutamatergic population.

### Open questions

1. Is SUPT_0135 a Cajal-Retzius remnant population (Calb2+/Reln+/Trp73+, developmentally transient) or does it represent adult SLM/OML Calb2+ glutamatergic neurons? ISH validation of Trp73 and Calb2 co-expression in adult SLM/OML would help resolve this.
2. Why is Slc17a8 (VGluT3) absent from SUPT_0135 given descriptions of SLM glutamatergic neurons as VGluT3+? Is VGluT3 expression restricted to a subset of Calb2+ SLM cells, or is the classical node definition too broad?
3. Does the classical node need to be split into a Cajal-Retzius subtype and a separate adult SLM glutamatergic neuron type?

---

## References

[1] Wheeler et al. 2015 · PMID:26402459 · DOI:10.7554/eLife.09960

[2] Ceranik et al. 1997 · PMID:9204922 · DOI:10.1523/JNEUROSCI.17-14-05380.1997

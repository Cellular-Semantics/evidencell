# GPi shell neuron (Mus musculus) — WMBv1 Mapping Report
*2026-02-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/BG/GPi_shell_neuron_Mmus.yaml`*

---

> **Location note.** WMBv1 location data derives from MERFISH spatial
> registration and records **soma position** only. Axonal and dendritic
> projection targets are not reflected in atlas cluster location fields and
> are not used in mapping assessments.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | internal globus pallidus shell projection neuron (CL:4310096) | |
| Soma location | Internal segment of globus pallidus, shell region [MBA:1031] |  |
| NT | GABA-Glut (dual) | [1] |
| Markers | Tbr1+, Cngb3+, Sst+ |  |
| Negative | Pvalb− | |
| Neuropeptides | Sst |  |

---

## Cell Ontology mapping

GPi shell neuron (Mus musculus) is mapped to **internal globus pallidus shell projection neuron (CL:4310096)** as an **exact match** in the Cell Ontology (skos:exactMatch); the existing CL term covers this type.

*Mapping notes:* CL:4310096 is defined at species-neutral level (Primates scope in the current approved definition). This node represents the Mus musculus instance of that type, supported by cross-species conservation (Wallace et al. 2017) and MapMyCells transfer from the primate HMBA group.

**Proposed CL term:** *internal globus pallidus shell projection neuron* (DRAFT)

> A internal globus pallidus shell projection neuron of the Mus musculus brain. These cells are located in the internal segment of globus pallidus (entopeduncular nucleus in rodents). Reference transcriptomic data for this type can be found in the dataset/taxonomy - Yao et al. (2023), Whole Mouse Brain in cell set Supertype:0504 GPi Tbr1 Cngb3 Gaba-Glut_1.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | Supertype:0504 GPi Tbr1 Cngb3 Gaba-Glut_1 (WMBv1) [CS20230722_SUPT_0504] |  | 460 |  |  |

All edges: `skos:exactMatch`

---

## Supertype:0504 GPi Tbr1 Cngb3 Gaba-Glut_1 (WMBv1) · 

*`CS20230722_SUPT_0504` · 460 cells (10x)*

**Supporting evidence:**

- WMBv1 atlas metadata (Yao et al. 2023) provides: (1) anatomical annotation "GPi" (manually curated); (2) NT type Glut-GABA (dual, confirmed by nt.markers: Gad2, Slc17a6, Gad1, Slc32a1); (3) cluster marker Cngb3 (all 3 clusters); (4) TF markers Pax6 and Tbr1 (all 3 clusters); (5) neuropeptide Sst in 2/3 clusters (Sst:8.5, 9.1), confirming somatostatin expression seen in the classical shell description. All features are consistent with the GPi shell neuron profile. [Atlas metadata]
- MapMyCells hierarchical annotation transfer from the primate HMBA BG Consensus Taxonomy (GPi Shell group, CS20250428_GROUP_0016) to WMBv1 identifies Supertype:0504 as the best mouse equivalent. Cross-species convergence on the same anatomical location (GPi border, surrounding core), molecular profile (dual GABA-Glut, Tbr1+, Sst+, Pvalb-) and atlas label ("GPi shell") provides independent support for the GPi shell neuron identity in mouse. [Annotation transfer]

**Concerns:**

- Anatomical location (GPi) is inferred from MERFISH CCF registration in WMBv1. CCF distribution data shows significant registration scatter, particularly for cluster 1995 where only 17% of cells register to GPi (with 25% to LHA, 11% GPe). Clusters 1996 (GPi:44%) and 1997 (GPi:24%) show better GPi assignment but still substantial spread to PAL/int. Cells in LHA, GPe, and pallidal subregions may represent registration errors rather than true anatomical localisation.
- Cross-species annotation transfer (primate HMBA BG → mouse WMBv1) is used as supporting evidence. The mouse EP/GPi is the functional homologue of the primate GPi but shows evolutionary differences in cytoarchitecture and projection targets. The shell/core organisation is conserved at the molecular level (Tbr1+/Sst+ shell; Pvalb+ core) but the degree of correspondence at the single-cluster level is not fully characterised.

**What would upgrade confidence:**

- *Unresolved:* Verify NCBIGene ID for Cngb3 (Mus musculus) — ID not populated; confirm from NCBI Gene before publishing.

- *Unresolved:* Cluster 1995 shows only 17% GPi registration with 25% in LHA. Is this a registration artefact, or does this cluster genuinely include neurons with soma outside GPi proper (e.g. peri-GPi cells)? Compare spatial plots for clusters 1995 vs 1996/1997.

- *Proposed:* MERFISH with probes for Tbr1, Cngb3, Sst, and Pvalb in mouse GPi/EP to validate location and marker profile with higher spatial precision.

- *Proposed:* Explore WMBv1 cluster-level data within Supertype:0504 to characterise fine-grained heterogeneity; compare with the primate GPi Shell group at equivalent resolution.


---

## Proposed experiments

### 1 — MERFISH / spatial transcriptomics

- MERFISH with probes for Tbr1, Cngb3, Sst, and Pvalb in mouse GPi/EP to validate location and marker profile with higher spatial precision.
*Resolves: edge_gpi_shell_mmus_to_wmb_0504*

### 2 — Other

- Explore WMBv1 cluster-level data within Supertype:0504 to characterise fine-grained heterogeneity; compare with the primate GPi Shell group at equivalent resolution.
*Resolves: edge_gpi_shell_mmus_to_wmb_0504*

---

## Open questions

1. Verify NCBIGene ID for Cngb3 (Mus musculus) — ID not populated; confirm from NCBI Gene before publishing.
2. Cluster 1995 shows only 17% GPi registration with 25% in LHA. Is this a registration artefact, or does this cluster genuinely include neurons with soma outside GPi proper (e.g. peri-GPi cells)? Compare spatial plots for clusters 1995 vs 1996/1997.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_gpi_shell_mmus_to_wmb_0504 | Atlas metadata | SUPPORT |
| edge_gpi_shell_mmus_to_wmb_0504 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.1016/j.neuron.2017.03.017 | — | neurotransmitter type |

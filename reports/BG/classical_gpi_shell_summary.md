# GPi shell neuron (internal globus pallidus shell projection neuron) — HMBA_BG_Consensus Mapping Report
*2026-02-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/BG/GPi_shell_neuron.yaml`*

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
| Soma location | Internal segment of globus pallidus, shell region [HBA:12898] |  |
| NT | GABA-Glut (dual) | [1] |
| Markers | SST+, TBR1+, SLC17A6+ |  |
| Negative | PVALB− | |
| Neuropeptides | SST |  |

---

## Cell Ontology mapping

GPi shell neuron (internal globus pallidus shell projection neuron) is mapped to **internal globus pallidus shell projection neuron (CL:4310096)** as an **exact match** in the Cell Ontology (skos:exactMatch); the existing CL term covers this type.

*Mapping notes:* CL:4310096 was created specifically for this type; this node IS that term.

**Proposed CL term:** *internal globus pallidus shell projection neuron* (ACCEPTED)

> A internal globus pallidus shell projection neuron of the Primates brain. These cells are located in the striatum, external segment of globus pallidus, internal segment of globus pallidus. Reference transcriptomic data for this type can be found in the dataset/taxonomy - HMBA Basal Ganglia Consensus Taxonomy in cell set Group:GPi Shell.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | Group:GPi Shell (HMBA Basal Ganglia Consensus Taxonomy) [CS20250428_GROUP_0016] |  | — |  |  |

All edges: `skos:exactMatch`

---

## Group:GPi Shell (HMBA Basal Ganglia Consensus Taxonomy) · 

*`CS20250428_GROUP_0016`*

**Supporting evidence:**

- HMBA atlas metadata provides MERFISH-derived soma location (GPi and surrounding GPi core region), neurotransmitter type (dual GABA-Glut), and defining marker expression (Sst+, Tbr1+, Slc17a6+, Pvalb-). All features are consistent with the classical GPi shell neuron description. [Atlas metadata]
- Establishes three molecularly distinct neuron classes in human GPi by triple FISH: SST+/SLC17A6+/SLC32A1+ dual-transmitter neurons at the GPi border (shell), and PVALB+ pure GABAergic neurons in the center (core). Directly supports dual GABA-Glut, SST+/Pvalb- marker profile and shell vs core anatomical organisation in primates. [Literature] [1]
- Establishes shell/core anatomical subregion structure of the mouse EPN (= rodent GPi equivalent) using SP and CB1R immunoreactivity: SOM (somatostatin) neurons concentrate in the shell, PV neurons in the core. Directly supports the anatomical shell/core distinction and differential SOM vs Pvalb distribution. Note: mouse data; Tbr1 and Slc17a6 are not described in this study — those markers come from the HMBA atlas (ATLAS_METADATA evidence above). [Literature] [2]

**Concerns:**

- Anatomical location (GPi shell) is inferred from MERFISH CCF registration. Registration may be inaccurate, potentially misassigning cells to adjacent regions (GPe, striatum). This is explicitly noted in CL:4310096.
- The target cell set is at "Group" level in the HMBA BG taxonomy (hierarchy: Class > Group). Group is a substructure within Class and sits above Subclass/Supertype/Cluster, so this is a moderately coarse mapping. The Group may encompass multiple more finely-resolved clusters that have not yet been individually characterised.

**What would upgrade confidence:**

- *Unresolved:* Are there finer-grained HMBA clusters within the GPi Shell group (CS20250428_GROUP_0016) that correspond to distinct sub-populations (e.g. by projection target or co-transmission ratio)?

- *Proposed:* Re-examine HMBA data at cluster level within Group:GPi Shell to determine if additional transcriptomic heterogeneity is present within this group.

- *Proposed:* MERFISH with probes for Sst, Tbr1, Slc17a6 and Pvalb in GPi to validate location and marker profile with higher spatial precision.


---

## Proposed experiments

### 1 — Other

- Re-examine HMBA data at cluster level within Group:GPi Shell to determine if additional transcriptomic heterogeneity is present within this group.
*Resolves: edge_gpi_shell_to_hmba*

### 2 — MERFISH / spatial transcriptomics

- MERFISH with probes for Sst, Tbr1, Slc17a6 and Pvalb in GPi to validate location and marker profile with higher spatial precision.
*Resolves: edge_gpi_shell_to_hmba*

---

## Open questions

1. Are there finer-grained HMBA clusters within the GPi Shell group (CS20250428_GROUP_0016) that correspond to distinct sub-populations (e.g. by projection target or co-transmission ratio)?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_gpi_shell_to_hmba | Atlas metadata | SUPPORT |
| edge_gpi_shell_to_hmba | Literature [1] | SUPPORT |
| edge_gpi_shell_to_hmba | Literature [2] | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.1016/j.neuron.2017.03.017 | — | neurotransmitter type |
| [2] | https://doi.org/10.1523/ENEURO.0208-22.2022 | — | Establishes shell/core anatomical subregion structure of the mouse EPN (= rodent |

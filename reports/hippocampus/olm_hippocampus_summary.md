# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*Draft · 2026-03-25 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_OLM.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum oriens [UBERON:0005371]; stratum lacunosum-moleculare [UBERON:0007637] | [1] [2] [1] [3] |
| NT | GABAergic | [4] [5] |
| Markers | Sst+, Chrna2+, mGluR1+ | [6] [7] [2] [8] |
| Negative | PV−, CB−, CR−, NOS−, VIP− | |
| Neuropeptides | Sst, Npy, Pnoc | [7] [9] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0769 Sst Gaba_3 [CS20230722_CLUS_0769] |  | — | 🟡 MODERATE | Best candidate |
| 2 | 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] |  | — | 🔴 LOW | Speculative |
| — | 0785 Sst Gaba_6 [CS20230722_CLUS_0785] |  | — | ⚪ UNCERTAIN | Eliminated (Chrna2) |
| — | 0788 Sst Gaba_6 [CS20230722_CLUS_0788] |  | — | ⚪ UNCERTAIN | Eliminated (Chrna2) |
| — | 0789 Sst Gaba_6 [CS20230722_CLUS_0789] |  | — | ⚪ UNCERTAIN | Eliminated (Chrna2) |

All edges: `TYPE_A_SPLITS`

---

## 0769 Sst Gaba_3 · 🟡 MODERATE

**Supporting evidence:**

- Best CA1 signal. Sst subclass consistent. CA1 SO (87 cells) — primary OLM location. Full neuropeptide triad: Sst, Npy, Pnoc. No SLM. Significant prosubiculum (61) and posterior amygdala (95) distribution. [Atlas metadata]
- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) strongly supports the parent Sst Gaba_3 supertype (43/46 cells, F1=0.67) but OLM cells scatter across sibling clusters 0767–0774 within it. Cluster 0769 specifically received 0/46 cells — OLM cells preferentially map to cluster 0768 (22/46, best cluster-level F1=0.53). This suggests OLM identity maps to the supertype level rather than to cluster 0769 specifically. Both Sst-OLM and Htr3a-OLM subtypes converge on the same Sst Gaba_3 supertype. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=stratum oriens (UBERON:0005371); SLM (UBERON:0007637) / B=CA1 SO (MBA:399, 87 cells); prosubiculum; posterior amygdala. CA1 SO matches — strongest CA1 signal. SLM absent. Extra-hippocampal spread.
- **marker_Chrna2** (APPROXIMATE): A=Chrna2 — defining marker / B=Chrna2 expressed (scattered) in Sst Gaba_3 supertype per ABC Atlas. ABC Atlas filter (HPF/GABA/Chrna2) retains Sst Gaba_3 but eliminates Sst Gaba_6. Expression scattered across clusters of this supertype — not a defining marker at cluster level, but present. https://tinyurl.com/a4f3kd4v

- mGluR1 (Grm1) not resolvable from atlas metadata.
- Prosubiculum (61 cells) and posterior amygdala (95 cells) — cluster may include non-OLM Sst interneurons from adjacent regions.
- Annotation transfer maps OLM cells to Sst Gaba_3 supertype but to sibling clusters (primarily 0768), not 0769. May indicate the mapping is more appropriate at supertype than cluster level.

**What would upgrade confidence:**

- *Unresolved:* Are the CA1 SO cells OLM-morphology? What are the amygdala cells?
- *Unresolved:* Why do OLM cells map to cluster 0768 rather than 0769? Do these clusters differ in hippocampal enrichment?
- *Proposed:* Chrna2-Cre + MapMyCells for CA1 stratum oriens neurons.
- *Proposed:* Targeted scRNA-seq or MERFISH of Chrna2+ stratum oriens neurons.

---

## 0727 Lamp5 Lhx6 Gaba_1 · 🔴 LOW

**Supporting evidence:**

- Partial property overlap. GABA consistent. CA3 SO + SLM match OLM anatomy. Sst and Pnoc neuropeptides present but Npy absent. Subclass is Lamp5 Lhx6, NOT Sst — discordant with canonical OLM identity. Chrna2/Grm1 not assessable. [Atlas metadata]

**Concerns:**

- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Lamp5 Lhx6 subclass. All 45 successfully classified cells mapped to Sst Gaba subclass (Sst Gaba_3 supertype). Zero support for this Lamp5 Lhx6 cluster as an OLM target. [Annotation transfer]
- **location** (APPROXIMATE): A=stratum oriens (UBERON:0005371); SLM (UBERON:0007637) / B=CA3 SO (MBA:486); CA3 SLM (MBA:471). SO and SLM present. CA3-enriched, not CA1.
- **marker_Sst** (APPROXIMATE): A=Sst — defining marker / B=Sst in neuropeptides, NOT defining_markers; Lamp5 Lhx6 subclass. Sst expressed but not defining. Subclass is Lamp5 Lhx6, not Sst.
- **neuropeptide_Npy** (DISCORDANT): A=Npy / B=absent. OLM expresses Npy; this cluster does not.
- Lamp5 Lhx6 subclass (CGE-derived), not Sst (MGE-derived). Biologically surprising for canonical Sst+ MGE-derived OLM. Requires independent validation.
- Chrna2 and mGluR1 not resolvable from atlas metadata.

**What would upgrade confidence:**

- *Unresolved:* Is Sst expression in this Lamp5 Lhx6 cluster biologically meaningful? OLM morphology/ephys present?
- *Proposed:* Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens.
- *Proposed:* Chrna2-Cre + MapMyCells to test Chrna2+ neuron mapping.

---

## Eliminated candidates

**Primary reason:** Shared disqualifying signal: Chrna2 is DISCORDANT across all UNCERTAIN edges.

**0785 Sst Gaba_6** (? cells)
- Filtering the ABC Atlas on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the Sst Gaba_6 supertype entirely. Chrna2 is a defining marker of OLM interneurons; its absence from this supertype argues against any cluster within it being OLM. [A]
- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Sst Gaba_6 supertype. All 45 successfully classified cells mapped to Sst Gaba_3 supertype instead. Zero support for this Sst Gaba_6 cluster as an OLM target.
- marker_Chrna2: ABC Atlas filter (HPF/GABA/Chrna2) eliminates Sst Gaba_6. https://tinyurl.com/a4f3kd4v

- neuropeptide_Pnoc: OLM expresses Pnoc; absent from this cluster.

**0788 Sst Gaba_6** (? cells)
- Filtering the ABC Atlas on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the Sst Gaba_6 supertype entirely. Chrna2 is a defining marker of OLM interneurons; its absence from this supertype argues against any cluster within it being OLM. [A]
- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Sst Gaba_6 supertype. All 45 successfully classified cells mapped to Sst Gaba_3 supertype instead. Zero support for this Sst Gaba_6 cluster as an OLM target.
- marker_Chrna2: ABC Atlas filtering on Chrna2 expression eliminates Sst Gaba_6 entirely. https://tinyurl.com/a4f3kd4v


**0789 Sst Gaba_6** (? cells)
- Filtering the ABC Atlas on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the Sst Gaba_6 supertype entirely. Chrna2 is a defining marker of OLM interneurons; its absence from this supertype argues against any cluster within it being OLM. [A]
- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Sst Gaba_6 supertype. All 45 successfully classified cells mapped to Sst Gaba_3 supertype instead. Zero support for this Sst Gaba_6 cluster as an OLM target.
- marker_Chrna2: ABC Atlas filtering on Chrna2 expression eliminates Sst Gaba_6 entirely. https://tinyurl.com/a4f3kd4v


---

## Proposed experiments

### 1 — Patch-seq

- Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens.
- Patch-seq of Sst+ CA1/CA3 stratum oriens neurons.
*Resolves: edge_olm_to_wmb_clus_0727, edge_olm_to_wmb_clus_0788*

### 2 — MapMyCells / annotation transfer

- Chrna2-Cre + MapMyCells to test Chrna2+ neuron mapping.
- Chrna2-Cre + MapMyCells for CA1 stratum oriens neurons.
- Chrna2-Cre + MapMyCells.
*Resolves: edge_olm_to_wmb_clus_0727, edge_olm_to_wmb_clus_0769, edge_olm_to_wmb_clus_0788, edge_olm_to_wmb_clus_0789*

### 3 — MERFISH / spatial transcriptomics

- Targeted scRNA-seq or MERFISH of Chrna2+ stratum oriens neurons.
*Resolves: edge_olm_to_wmb_clus_0769*

### 4 — Other

- Region-specific dissection of CA3 SO vs amygdala cells in this cluster.
*Resolves: edge_olm_to_wmb_clus_0789*

---

## Open questions

1. Are the CA1 SO cells OLM-morphology? What are the amygdala cells?
2. Why do OLM cells map to cluster 0768 rather than 0769? Do these clusters differ in hippocampal enrichment?
3. Is Sst expression in this Lamp5 Lhx6 cluster biologically meaningful? OLM morphology/ephys present?
4. Given Chrna2 absence, is this cluster a non-OLM Sst stratum oriens type?
5. Are SO cells OLM-morphology? What are corpus callosum cells?
6. Are CA3 SO cells OLM? What is the amygdala population?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_olm_to_wmb_clus_0769 | Atlas metadata | SUPPORT |
| edge_olm_to_wmb_clus_0769 | Annotation transfer | PARTIAL |
| edge_olm_to_wmb_clus_0727 | Atlas metadata | PARTIAL |
| edge_olm_to_wmb_clus_0727 | Annotation transfer | REFUTE |
| edge_olm_to_wmb_clus_0785 | Atlas metadata | PARTIAL |
| edge_olm_to_wmb_clus_0785 | Atlas query [A] | REFUTE |
| edge_olm_to_wmb_clus_0785 | Annotation transfer | REFUTE |
| edge_olm_to_wmb_clus_0788 | Atlas metadata | PARTIAL |
| edge_olm_to_wmb_clus_0788 | Atlas query [A] | REFUTE |
| edge_olm_to_wmb_clus_0788 | Annotation transfer | REFUTE |
| edge_olm_to_wmb_clus_0789 | Atlas metadata | PARTIAL |
| edge_olm_to_wmb_clus_0789 | Atlas query [A] | REFUTE |
| edge_olm_to_wmb_clus_0789 | Annotation transfer | REFUTE |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 · PMID:20421280 | [20421280](https://pubmed.ncbi.nlm.nih.gov/20421280/) | soma location |
| [2] | Nichol et al. 2018 · PMID:29487503 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/) | soma location |
| [3] | Tecuatl et al. 2020 · PMID:33361464 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/) | soma location |
| [4] | Böhm et al. 2015 · PMID:26021702 | [26021702](https://pubmed.ncbi.nlm.nih.gov/26021702/) | neurotransmitter type |
| [5] | Oliva et al. 2000 · PMID:10777798 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | neurotransmitter type |
| [6] | Hooft et al. 2000 · PMID:10804195 | [10804195](https://pubmed.ncbi.nlm.nih.gov/10804195/) | Sst marker |
| [7] | Winterer et al. 2019 · PMID:31420995 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) | Sst marker |
| [8] | Leão et al. 2012 · PMID:23042082 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/) | Chrna2 marker |
| [9] | Thulin et al. 2025 · PMID:40757734 | [40757734](https://pubmed.ncbi.nlm.nih.gov/40757734/) | Pnoc neuropeptide |
| [A] | ABC Atlas | — | anatomy=HPF; NT=GABA; expression=Chrna2 · [view](https://tinyurl.com/a4f3kd4v) |

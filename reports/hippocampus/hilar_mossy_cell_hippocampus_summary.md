# Hilar mossy cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | dentate gyrus neuron (CL:4023062) | |
| Soma location | dentate gyrus polymorph layer [UBERON:0002928] | [1] [2] [3] |
| NT | glutamatergic | [4] [3] [5] |
| Markers | Gria4+, Dkk3+ |  |

---

## Cell Ontology mapping

Hilar mossy cell is a **broad match** to **dentate gyrus neuron (CL:4023062)** in the Cell Ontology — i.e. **dentate gyrus neuron (CL:4023062)** is the closest existing CL term (an ancestor) but does not fully cover this type. A new child term is a candidate for submission to CL.

*Mapping notes:* Hilar mossy cells are glutamatergic neurons with soma restricted to the dentate gyrus polymorphic layer; CL:4023062 covers all dentate gyrus neurons and is therefore a BROAD match. No mossy cell-specific CL term currently exists.

**Proposed CL term:** *hilar mossy cell* (SUBMITTED)

> A dentate gyrus neuron with soma in the polymorphic layer (UBERON:0002928) (Scharfman & Myers, 2012), capable of glutamate secretion as a neurotransmitter (Scharfman & Bernstein, 2015). Distinguished by a large multipolar soma, thorny excrescences on proximal dendrites, and commissural/associational axon projections terminating in the inner molecular layer of the dentate gyrus (Scharfman & Myers, 2012). Electrophysiologically characterised by a depolarised resting membrane potential, prominent hyperpolarisation-activated cation current (Ih), and firing accommodation (Scharfman & Myers, 2012). In rodents, serves as a major excitatory neuron of the dentate hilus providing feedback excitation to granule cells (Sun et al., 2017).

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0078 CA3 Glut_4 [CS20230722_SUPT_0078] |  | 5,709 |  |  |
| — | 0079 CA3 Glut_5 [CS20230722_SUPT_0079] |  | 1,308 |  |  |

All edges: `skos:closeMatch`

---

## 0078 CA3 Glut_4 · 

*`CS20230722_SUPT_0078` · 5,709 cells (10x)*

**Supporting evidence:**

- MapMyCells local annotation transfer of Hochgerner 2018 (GSE95315) Mossy-Cyp26b1 label onto WMBv1 (CCN20230722). 33 of 34 Mossy-Cyp26b1 cells map to SUPT_0078 (0078 CA3 Glut_4) at the supertype level (F1=0.943; coverage=0.971, purity=0.917). At cluster level, the best cluster is 0315 CA3 Glut_4 (n=20, F1=0.833) followed by 0314 CA3 Glut_4 (n=7). The high F1 indicates that Mossy-Cyp26b1 cells are a near-complete subset of SUPT_0078. The PARTIAL_OVERLAP relationship is used because SUPT_0078 MERFISH cells are distributed across CA3 strata rather than the dentate hilus, suggesting this supertype captures mossy cells resident at the CA3c/hilus border or includes CA3 pyramidal cells sharing the Cyp26b1 transcriptomic profile. [Annotation transfer]

**Concerns:**

- **location** (DISCORDANT): A=dentate gyrus polymorph layer / hilus (UBERON:0001885, compartment: SOMA) / B=Field CA3, pyramidal layer (MBA:495): 1467 cells; Field CA3, stratum oriens (MBA:486): 1381 cells; Field CA3, stratum radiatum (MBA:504): 945 cells; Field CA3, stratum lucidum (MBA:479): 868 cells; Field CA3, stratum lacunosum-moleculare (MBA:471): 437 cells. SUPT_0078 MERFISH soma assignments are entirely within CA3 strata; no cells are listed in the dentate gyrus polymorph layer (MBA:10704) or granule cell layer (MBA:632). Classical hilar mossy cells have soma in the hilus/polymorph layer. The high AT F1 (0.943) suggests Mossy-Cyp26b1 cells are transcriptomically equivalent to SUPT_0078 despite this anatomical discordance. Hilar mossy cells at the CA3c border may fall within MERFISH CA3 registration, or the Cyp26b1+ mossy cell subtype may have a distinct anatomical distribution compared to the broader mossy cell population.

- The anatomical discordance between SUPT_0078 (CA3 strata) and classical hilar mossy cells (hilus/polymorph layer) is a key unresolved issue. Hilar mossy cells at the CA3c/hilus boundary may register as CA3 cells in MERFISH data, or the Cyp26b1+ subpopulation may have soma positions that overlap with proximal CA3c. This mapping remains a hypothesis pending independent anatomy validation.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: DISCORDANT comparison(s), existing caveats → closeMatch. Curator review recommended.

**What would upgrade confidence:**

- *Unresolved:* Are SUPT_0078 cells that map to CA3 pyramidal layer actually at the CA3c/hilar boundary? High-resolution FISH of Homer3 or Cldn22 (SUPT_0078 defining markers) in hilus/CA3c would resolve this.

- *Proposed:* smFISH or MERFISH spot validation of SUPT_0078 defining markers (Homer3, Cldn22) in dentate hilus to test whether soma positions span the CA3c/hilus boundary.


---

## 0079 CA3 Glut_5 · 

*`CS20230722_SUPT_0079` · 1,308 cells (10x)*

**Supporting evidence:**

- MapMyCells local annotation transfer of Hochgerner 2018 (GSE95315) Mossy-Adcyap1 label onto WMBv1 (CCN20230722). 20 of 27 Mossy-Adcyap1 cells map to SUPT_0079 (0079 CA3 Glut_5) at the supertype level (F1=0.833; coverage=0.741, purity=0.952). The high purity (0.952) indicates Mossy-Adcyap1 cells account for the majority of SUPT_0079 cells captured by AT — suggesting this supertype may be specific to the Adcyap1+ mossy cell subtype. SUPT_0079 uniquely has 181 cells in Dentate gyrus, polymorph layer (MBA:10704, the hilus), consistent with the hilar soma location of classical mossy cells. The PARTIAL_OVERLAP relationship is used because SUPT_0079 also has substantial cells in CA3 strata, indicating a broader supertype than the hilar-restricted classical mossy cell. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=dentate gyrus polymorph layer / hilus (UBERON:0001885, compartment: SOMA) / B=Dentate gyrus, polymorph layer (MBA:10704): 181 cells; Dentate gyrus, granule cell layer (MBA:632): 147 cells; Field CA3, pyramidal layer (MBA:495): 294 cells; Field CA3, stratum oriens (MBA:486): 121 cells; Field CA3, stratum lucidum (MBA:479): 175 cells; Field CA3, stratum radiatum (MBA:504): 261 cells. SUPT_0079 is the only WMBv1 CA3 Glut supertype with cells assigned to the dentate gyrus polymorph layer (181 cells, MBA:10704), which is the hilus — the classical mossy cell soma location. This is a positive anatomical correspondence. The majority of cells are however in CA3 strata, which may reflect CA3c pyramidal cells that share the Adcyap1+ transcriptomic signature, or MERFISH registration of hilus cells into adjacent CA3c.

- Hochgerner 2018 identifies three molecular subtypes of hilar mossy cells: Mossy-Cyp26b1, Mossy-Adcyap1, and Mossy-Klk8. These map to SUPT_0078 (Cyp26b1, F1=0.943) and SUPT_0079 (Adcyap1, F1=0.833) respectively. Mossy-Klk8 (n=6 cells) maps ambiguously across multiple CA3 supertypes (best: SUPT_0077, F1=0.308) — insufficient evidence to build a separate edge. Together, SUPT_0078 and SUPT_0079 represent the molecular subdivision of the classical hilar mossy cell into two WMBv1 transcriptomic types.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: existing caveats → closeMatch. Curator review recommended.

**What would upgrade confidence:**

- *Unresolved:* What is the functional and anatomical distinction between the SUPT_0078 (Cyp26b1+) and SUPT_0079 (Adcyap1+) mossy cell subtypes? Do they correspond to dorsal vs. ventral mossy cells, or to distinct projection patterns (IML-only vs. IML+MML in dorsal mossy cells)?

- *Proposed:* ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus to confirm non-overlapping expression and validate the two-supertype mossy cell split.

- *Proposed:* Run AT from a full Hochgerner 2018 mouse replication to confirm species-generality of the SUPT_0078/0079 mossy cell split.


---

## Proposed experiments

### 1 — MERFISH / spatial transcriptomics

- smFISH or MERFISH spot validation of SUPT_0078 defining markers (Homer3, Cldn22) in dentate hilus to test whether soma positions span the CA3c/hilus boundary.
*Resolves: edge_hilar_mossy_cell_hippocampus_to_supt_0078*

### 2 — Other

- ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus to confirm non-overlapping expression and validate the two-supertype mossy cell split.
- Run AT from a full Hochgerner 2018 mouse replication to confirm species-generality of the SUPT_0078/0079 mossy cell split.
*Resolves: edge_hilar_mossy_cell_hippocampus_to_supt_0079*

---

## Open questions

1. Are SUPT_0078 cells that map to CA3 pyramidal layer actually at the CA3c/hilar boundary? High-resolution FISH of Homer3 or Cldn22 (SUPT_0078 defining markers) in hilus/CA3c would resolve this.
2. What is the functional and anatomical distinction between the SUPT_0078 (Cyp26b1+) and SUPT_0079 (Adcyap1+) mossy cell subtypes? Do they correspond to dorsal vs. ventral mossy cells, or to distinct projection patterns (IML-only vs. IML+MML in dorsal mossy cells)?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_hilar_mossy_cell_hippocampus_to_supt_0078 | Annotation transfer | SUPPORT |
| edge_hilar_mossy_cell_hippocampus_to_supt_0079 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Botterill et al. 2021 · PMID:33600026 | [33600026](https://pubmed.ncbi.nlm.nih.gov/33600026/) | soma location |
| [2] | Fredes & Shigemoto 2021 · PMID:34214666 | [34214666](https://pubmed.ncbi.nlm.nih.gov/34214666/) | soma location |
| [3] | Scharfman & Myers 2013 · PMID:23420672 | [23420672](https://pubmed.ncbi.nlm.nih.gov/23420672/) | soma location |
| [4] | Sun et al. 2017 · PMID:28451637 | [28451637](https://pubmed.ncbi.nlm.nih.gov/28451637/) | neurotransmitter type |
| [5] | Scharfman & Bernstein 2015 · PMID:26347618 | [26347618](https://pubmed.ncbi.nlm.nih.gov/26347618/) | neurotransmitter type |

# Oriens-oriens (O-O) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum oriens [UBERON:0014552]; stratum oriens [UBERON:0014552] |  |
| NT | GABAergic |  |
| Markers | Sst+, Nos1+ | [1] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] |  | 1,495 |  |  |

All edges: `evidencell:UncertainRelationship`

---

## 0219 Sst Gaba_6 · 

*`CS20230722_SUPT_0219` · 1,495 cells (10x)*

**Supporting evidence:**

- Sst Gaba_6 supertype is Sst+ GABAergic interneuron enriched in CA3 (SO 305, SR 167, SP 261, lucidum 99). O-O cell is Sst+/Nos1+ with axon confined to stratum oriens. Id3, Adamtsl1, Sp9 are defining markers with no correspondence established in O-O classical literature. Critically, O-O cells were identified by Sst;;Nos1 intersectional genetics (Chamberland 2024) and SUPT_0219 lacks Nos1 in its marker list, which is a potential concern. However, Nos1 may be expressed without being a defining marker at supertype resolution. The CA3 enrichment of SUPT_0219 vs the CA1 description for O-O cells is a further point of uncertainty. Evidence for O-O cell as a distinct classical type is thin (single study), making this a PLAUSIBLE but unconfirmed assignment. [Atlas metadata]
- Precomputed stats cross-check: Sst=10.17 strongly confirmed, but Nos1=1.81 is low. O-O cells are defined by Sst+Nos1 co-expression; weak Nos1 in SUPT_0219 suggests this may not be the primary O-O supertype. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Sst subclass (n=273 HIP cells) onto WMBv1. SUPT_0219 (Sst Gaba_6) is the dominant supertype target for Sst cells (F1=0.759, 161/273 cells, purity=0.964), consistent with the oriens-oriens cell correspondence to SUPT_0219. PARTIAL because the Sst SSv4 label is mixed; SUPT_0219 being the dominant target is supportive but not cell-type-specific. Yao 2021 SSv4 'Sst' subclass (n=273 HIP cells) encompasses multiple Sst interneuron types (OLM, bistratified, hippocampo-septal, oriens-oriens, and others); subtype resolution requires a dataset with morphologically identified Sst-IN labels. [Annotation transfer]

**Concerns:**

- **location_stratum_oriens** (APPROXIMATE): A=CA1 stratum oriens (UBERON:0014552) — SOMA / B=Field CA3, stratum oriens (MBA:486, 305 cells) — CA3-enriched, not CA1. O-O cell defined in CA1 (Chamberland 2024). SUPT_0219 is CA3-enriched with no explicit CA1 SO entry in top locations. This is a subregional mismatch.

- **marker_Nos1** (APPROXIMATE): A=Nos1 — defining marker (intersectional genetics, Sst;;Nos1 strategy) / B=not listed in SUPT_0219 markers; precomputed stats mean: 1.81. Nos1 is critical for the Sst;;Nos1 intersectional identification of O-O cells. Its absence from atlas defining markers does not confirm absence of expression — may reflect different marker selection criteria.

- O-O cell evidence is thin: identified in a single study (Chamberland et al. 2024, PMID:38640347) using Sst;;Nos1 intersectional Cre/Flp. The assignment to SUPT_0219 is based on Sst co-expression alone; the Nos1 component is not confirmed in the atlas supertype. CA3 vs CA1 enrichment mismatch further weakens this assignment.
- Sst Gaba_6 subclass contains multiple supertypes. Without Nos1 verification at the atlas level, it is unclear which (if any) Sst Gaba_6 supertype captures the O-O cell population. SUPT_0219 is a plausible candidate based on hippocampal enrichment but remains unconfirmed.

**What would upgrade confidence:**

- *Unresolved:* Does SUPT_0219 express Nos1? If so, at what penetrance?
- *Unresolved:* Are the CA3 SO cells in SUPT_0219 analogous to the CA1 O-O cells described by Chamberland 2024?
- *Unresolved:* Is there a CA1 SO Sst+/Nos1+ supertype better matching O-O cell identity?

---

## Open questions

1. Does SUPT_0219 express Nos1? If so, at what penetrance?
2. Are the CA3 SO cells in SUPT_0219 analogous to the CA1 O-O cells described by Chamberland 2024?
3. Is there a CA1 SO Sst+/Nos1+ supertype better matching O-O cell identity?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | Atlas metadata | PARTIAL |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | Atlas metadata | PARTIAL |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 · PMID:38640347 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker |

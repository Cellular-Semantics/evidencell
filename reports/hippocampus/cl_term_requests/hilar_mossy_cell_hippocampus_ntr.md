# CL new term request: Hilar mossy cell

*Drafted from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml` node `hilar_mossy_cell_hippocampus` on 2026-05-21.*
*Parent (current cl_mapping): dentate gyrus neuron (CL:4023062) — BROAD*

**Preferred term label**
Hilar mossy cell

**Synonyms** (with reference where available)
- mossy cell (exact) — Scharfman & Myers 2012, PMID:23420672
- dentate hilar mossy cell (exact) — Fredes & Shigemoto 2021, PMID:34214666

**Definition** (with inline references; Author et al., YEAR format)
A dentate gyrus neuron with soma in the polymorphic layer (UBERON:0002928) (Scharfman & Myers, 2012), capable of glutamate secretion as a neurotransmitter (Scharfman & Bernstein, 2015). Distinguished by a large multipolar soma, thorny excrescences on proximal dendrites, and commissural/associational axon projections terminating in the inner molecular layer of the dentate gyrus (Scharfman & Myers, 2012). Electrophysiologically characterised by a depolarised resting membrane potential, prominent hyperpolarisation-activated cation current (Ih), and firing accommodation (Scharfman & Myers, 2012). In rodents, serves as a major excitatory neuron of the dentate hilus providing feedback excitation to granule cells (Sun et al., 2017).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
dentate gyrus neuron (CL:4023062) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCL_4023062

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
dentate gyrus polymorphic layer (UBERON:0002928) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0002928

**Your ORCID**
0000-0002-5507-2103

**Additional notes or concerns**
No mossy cell-specific CL term currently exists. The parent term CL:4023062 (dentate gyrus neuron) covers all neurons of the dentate gyrus without resolution to the distinct excitatory hilar population. Hilar mossy cells are a well-established, morphologically and functionally distinct glutamatergic cell class in the dentate hilus, separable from granule cells and dentate interneurons by soma location in the polymorphic layer, thorny excrescence morphology, and commissural/associational projections to the inner molecular layer (Scharfman & Myers 2012, PMID:23420672). A specific CL term would enable precise annotation of single-cell transcriptomic datasets in which mossy cells form a reproducible cluster (Hochgerner et al. 2018) and map with high fidelity to WMBv1 atlas supertypes in annotation transfer (Botterill et al. 2021, PMID:33600026; Fredes & Shigemoto 2021, PMID:34214666). Note: defining markers Gria4 and Dkk3 (NCBIGene:14802, NCBIGene:50781) are present in the KB but lack a primary ISH/scRNA-seq citation specifically naming them as mossy cell markers; `expresses` axioms are withheld pending confirmation of the appropriate PRO identifiers and primary sources.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'dentate gyrus polymorphic layer' (UBERON:0002928)
- subClassOf 'capable of' (RO:0002215) some 'glutamate secretion, neurotransmission' (GO:0061535)

Key references:
- Scharfman & Myers 2012 — PMID:23420672 — supports: soma in dentate gyrus polymorphic layer (hilus); glutamatergic identity; defining morphological and projection criteria (review with defining criteria, guinea pig and rodent)
- Scharfman & Bernstein 2015 — PMID:26347618 — supports: glutamatergic neurotransmitter identity; hilar location (review, rodent dentate gyrus)
- Sun et al. 2017 — PMID:28451637 — supports: feedback excitation of granule cells; hilar location; glutamatergic projection (viral genetic circuit mapping, adult mouse dentate gyrus)
- Fredes & Shigemoto 2021 — PMID:34214666 — supports: hilar mossy cell as a distinct glutamatergic cell class; dorsal/ventral distinction (review, rodent dentate gyrus)
- Botterill et al. 2021 — PMID:33600026 — supports: soma in dentate gyrus polymorphic layer; Cre-line-confirmed identity (Drd2-Cre, Crlr-Cre); mossy cell projections (adult mouse dentate gyrus)

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml#hilar_mossy_cell_hippocampus`.*
*Source facts: `reports/hippocampus/hilar_mossy_cell_hippocampus_facts.json`.*

# CL new term request: CA1 pyramidal cell

*Drafted from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml` node `ca1_pc_hippocampus` on 2026-05-21.*
*Parent (current cl_mapping): hippocampal pyramidal neuron (CL:1001571) — BROAD*

**Preferred term label**
CA1 pyramidal cell

**Synonyms** (with reference where available)
- CA1 pyramidal neuron (exact) — Cembrowski et al., 2016, PMID:27113915
- pyramidal cell of CA1 (exact) — Cembrowski et al., 2016, PMID:27113915

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A hippocampal pyramidal neuron with soma located in the pyramidal layer of hippocampal area CA1 (UBERON:0014548) (Cembrowski et al., 2016; Müller & Remy, 2017), forming the dominant excitatory projection population of the CA1 subfield. As the primary output cell of Ammon's horn, it projects via the subiculum to entorhinal cortex and is capable of glutamate secretion as a neurotransmitter (Dale et al., 2015). In mouse, it is distinguished from CA2 and CA3 pyramidal neurons by soma position within the CA1 stratum pyramidale and by expression of wolframin (Wfs1), an endoplasmic reticulum-resident membrane protein enriched in deep-sublayer CA1 cells (Cembrowski et al., 2016).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
hippocampal pyramidal neuron (CL:1001571) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCL_1001571

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
pyramidal layer of CA1 (UBERON:0014548) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0014548

**Your ORCID**
0000-0002-5507-2103

**Additional notes or concerns**
No CA1-specific CL term currently exists. The parent term CL:1001571 (hippocampal pyramidal neuron) covers all pyramidal neurons of the hippocampus — CA1, CA2, CA3, and subiculum — without anatomical resolution to individual subfields. This gap prevents precise annotation of single-cell transcriptomic datasets in which CA1, CA2, and CA3 pyramidal cells are robustly distinguishable by both soma location and gene expression (Cembrowski et al. 2016, PMID:27113915). In the Allen Brain Atlas WMBv1, CA1 pyramidal cells form an exclusive glutamatergic subclass (016 CA1-ProS Glut) with near-perfect fidelity in annotation transfer from the Yao 2021 hippocampal formation dataset (subclass F1=0.995). A CA1-specific term would also enable subtype terms for the known deep- vs. superficial-sublayer populations distinguished by Wfs1 expression, once their atlas correspondence is resolved. Note: the Wfs1 `expresses` axiom is withheld pending confirmation of the appropriate PRO identifier; a primary ISH citation supporting Wfs1 enrichment in CA1 deep-sublayer cells should be added before posting.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'pyramidal layer of CA1' (UBERON:0014548)
- subClassOf 'capable of' (RO:0002215) some 'glutamate secretion, neurotransmission' (GO:0061535)

Key references:
- Cembrowski et al. 2016 — PMID:27113915 — supports: soma location in CA1 stratum pyramidale; Wfs1 as a transcriptomic marker enriched in CA1 pyramidal cells (RNA-seq, adult mouse dorsal and ventral hippocampus)
- Müller & Remy 2017 — PMID:29250747 — supports: CA1 as a major output structure of the hippocampal formation; soma in CA1 subfield (review, rodent)
- Dale et al. 2015 — PMID:26346726 — supports: glutamatergic neurotransmitter type; CA1 pyramidal cells as principal cells of Ammon's horn (review, mouse/rat)
- Mancini et al. 2022 — PMID:37011759 — supports: pyramidal layer of CA1 as soma location; glutamatergic identity (review, rodent hippocampus)

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml#ca1_pc_hippocampus`.*
*Source facts: `reports/hippocampus/ca1_pc_hippocampus_facts.json`.*

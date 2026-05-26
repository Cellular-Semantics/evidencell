# CL new term request: CA3 pyramidal cell

*Drafted from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml` node `ca3_pc_hippocampus` on 2026-05-26.*
*Parent (current cl_mapping): hippocampal pyramidal neuron (CL:1001571) — BROAD*

**Preferred term label**
CA3 pyramidal cell

**Synonyms** (with reference where available)
- CA3 pyramidal neuron (exact) — Cembrowski et al., 2016, PMID:27113915
- pyramidal cell of CA3 (exact) — Cembrowski et al., 2016, PMID:27113915

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A hippocampal pyramidal neuron with soma located in the pyramidal layer of hippocampal area CA3 (UBERON:0014550) (Cembrowski et al., 2016; Wheeler et al., 2015). Capable of glutamate secretion as a neurotransmitter (Dale et al., 2015) and distinguished from CA1 and CA2 pyramidal neurons by thorny excrescences on the proximal apical dendrites — postsynaptic specializations that receive excitatory mossy fiber input from dentate gyrus granule cells (Munster-Wandowski et al., 2013). Harbours a dense recurrent Schaffer collateral network; individual neurons can act as hub neurons capable of triggering hippocampal network bursts (Marissal et al., 2012).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
hippocampal pyramidal neuron (CL:1001571) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCL_1001571

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
pyramidal layer of CA3 (UBERON:0014550) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0014550

**Your ORCID**
0000-0002-5507-2103

**Additional notes or concerns**
No CA3-specific CL term currently exists. The parent term CL:1001571 (hippocampal pyramidal neuron) covers all pyramidal neurons of the hippocampus — CA1, CA2, CA3, and subiculum — without anatomical resolution to individual subfields. This gap prevents precise annotation of single-cell transcriptomic datasets in which CA3, CA2, and CA1 pyramidal cells are robustly distinguishable by soma location, gene expression, and connectivity (Cembrowski et al. 2016, PMID:27113915). CA3 pyramidal cells are uniquely defined among Ammon's horn pyramidal neurons by their thorny excrescences — postsynaptic specializations receiving mossy fiber input from dentate gyrus granule cells — which are absent from CA1 and CA2 pyramidal neurons (Munster-Wandowski et al. 2013, PMID:24319410). In the Allen Brain Atlas WMBv1, CA3 pyramidal cells form an exclusive glutamatergic subclass (017 CA3 Glut) with near-perfect annotation transfer fidelity at the subclass level (F1=0.994), confirming that essentially all CA3 pyramidal cells resolve unambiguously to a single atlas subclass. Note: no molecular marker exclusively specific to CA3 pyramidal cells relative to all other hippocampal pyramidal cell types has been identified in the classical literature; `expresses` axioms are therefore withheld. The thorny excrescence morphology and mossy fiber innervation remain the primary defining criteria. A CA3-specific term would complement the existing (proposed) CA1 and CA2 terms to achieve full Ammon's horn subfield resolution.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'pyramidal layer of CA3' (UBERON:0014550)
- subClassOf 'capable of' (RO:0002215) some 'glutamate secretion, neurotransmission' (GO:0061535)

Key references:
- Cembrowski et al. 2016 — PMID:27113915 — supports: soma location in CA3 stratum pyramidale; RNA-seq profiling of hippocampal principal cell types including CA3 (adult mouse, dorsal and ventral hippocampus)
- Wheeler et al. 2015 — PMID:26402459 — supports: soma location in CA3 stratum pyramidale; Hippocampome.org knowledge base of neuron types in the rodent hippocampal formation (literature mining + curation)
- Dale et al. 2015 — PMID:26346726 — supports: glutamatergic neurotransmitter type; CA3 pyramidal cells as principal cells of Ammon's horn (review, mouse/rat)
- Munster-Wandowski et al. 2013 — PMID:24319410 — supports: thorny excrescences on CA3 proximal apical dendrites as postsynaptic targets of mossy fiber terminals from dentate gyrus granule cells; mixed glutamatergic/gap junction synaptic connectivity (electron microscopy + immunohistochemistry, adult rat)
- Marissal et al. 2012 — PMID:23271650 — supports: hub neuron capacity; recurrent excitatory connectivity enabling single CA3 pyramidal neurons to trigger hippocampal network bursts (patch-clamp + multineuron Ca2+ imaging, juvenile and adult mouse CA3)

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml#ca3_pc_hippocampus`.*
*Source facts: `reports/hippocampus/ca3_pc_hippocampus_facts.json`.*

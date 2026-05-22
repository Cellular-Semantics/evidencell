# CL new term request: CA2 pyramidal cell

*Drafted from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml` node `ca2_pc_hippocampus` on 2026-05-22.*
*Parent (current cl_mapping): hippocampal pyramidal neuron (CL:1001571) — BROAD*

**Preferred term label**
CA2 pyramidal cell

**Synonyms** (with reference where available)
- CA2 pyramidal neuron (exact) — Cembrowski et al., 2016, PMID:27113915
- pyramidal cell of CA2 (exact) — Cembrowski et al., 2016, PMID:27113915

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A hippocampal pyramidal neuron with soma located in the pyramidal layer of hippocampal area CA2 (Cembrowski et al., 2016; Sanchez-Aguilera et al., 2021). Distinguished from CA1 and CA3 pyramidal neurons by expression of Pcp4, Rgs14, and Amigo2 in rodents (San Antonio et al., 2014; Caruana et al., 2012), and by absence of the CA1 marker wolframin (Wfs1) (Evans et al., 2018). Receives strong LTP-competent input from entorhinal cortex at distal dendrites, while Schaffer collateral inputs to proximal dendrites are resistant to canonical LTP in wild-type animals (Chevaleyre & Siegelbaum, 2010). Required for social memory in mice (Hitti & Siegelbaum, 2014).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
hippocampal pyramidal neuron (CL:1001571) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCL_1001571

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
pyramidal layer of CA2 (UBERON:0014549) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0014549

**Your ORCID**
0000-0002-5507-2103

**Additional notes or concerns**
No CA2-specific CL term currently exists. The parent term CL:1001571 (hippocampal pyramidal neuron) covers all pyramidal neurons of the hippocampus — CA1, CA2, CA3, and subiculum — without anatomical resolution to individual subfields. This gap prevents precise annotation of single-cell transcriptomic datasets in which CA1, CA2, and CA3 pyramidal cells are robustly distinguishable by both soma location and gene expression (Cembrowski et al. 2016, PMID:27113915). CA2 pyramidal cells are further distinguished by a unique circuit function: they are essential for social memory in mice, as demonstrated by selective genetic inactivation of Amigo2-Cre-expressing CA2 neurons (Hitti & Siegelbaum 2014, PMID:24572357). In the Allen Brain Atlas WMBv1, CA2 pyramidal cells correspond to the CA2-FC-IG Glut subclass (SUBC_025), with SUPT_0100 (0100 CA2-FC-IG Glut_1) as the primary supertype candidate based on MERFISH anatomy (446 cells in CA2 pyramidal layer). A CA2-specific term would also clarify the relationship between CA2 pyramidal cells and the fasciola cinerea and indusium griseum neurons that share the same WMBv1 subclass. Note: `expresses` axioms for Pcp4, Rgs14, and Amigo2 are withheld pending confirmation of the appropriate PRO identifiers; primary ISH citations supporting these markers are available (PMID:24166578; PMID:22904370) and should be added before posting.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'pyramidal layer of CA2' (UBERON:0014549)
- subClassOf 'capable of' (RO:0002215) some 'glutamate secretion, neurotransmission' (GO:0061535)

Key references:
- Cembrowski et al. 2016 — PMID:27113915 — supports: soma location in CA2 stratum pyramidale; transcriptomic distinction of CA2 from CA1/CA3 (RNA-seq, adult mouse dorsal and ventral hippocampus)
- Sanchez-Aguilera et al. 2021 — PMID:33956790 — supports: soma location in CA2 pyramidal layer; dorsoventral CA2 distribution (review, rat hippocampus)
- Dale et al. 2015 — PMID:26346726 — supports: glutamatergic neurotransmitter type; CA2 as a principal cell subfield (review, mouse/rat)
- San Antonio et al. 2014 — PMID:24166578 — supports: Pcp4 and Rgs14 as defining markers of CA2; delineation of CA3/CA2 and CA2/CA1 borders by PCP4 immunostaining (adult mouse hippocampus)
- Caruana et al. 2012 — PMID:22904370 — supports: Amigo2 as a CA2-enriched marker; Schaffer collateral LTP resistance (adult mouse hippocampus)
- Evans et al. 2018 — PMID:29911178 — supports: Wfs1 as a CA1 marker absent from CA2; Amigo2-EGFP labels CA2 selectively relative to WFS1-positive CA1 cells (adult mouse, IHC)
- Chevaleyre & Siegelbaum 2010 — PMID:20510860 — supports: entorhinal cortex LTP at distal CA2 dendrites; Schaffer collateral LTP resistance in wild-type CA2 (mouse slice electrophysiology)
- Hitti & Siegelbaum 2014 — PMID:24572357 — supports: CA2 as essential for social memory; Amigo2-Cre genetic targeting of CA2 pyramidal neurons (adult mouse behaviour)

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml#ca2_pc_hippocampus`.*
*Source facts: `reports/hippocampus/ca2_pc_hippocampus_facts.json`.*

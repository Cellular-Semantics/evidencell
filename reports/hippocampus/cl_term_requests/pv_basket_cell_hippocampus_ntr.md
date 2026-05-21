# CL new term request: parvalbumin-positive basket cell

*Drafted from `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml` node `pv_basket_cell_hippocampus` on 2026-05-19.*
*Parent: basket cell (CL:0000118) — user-specified (override of BROAD cl_mapping)*

**Preferred term label**
parvalbumin-positive basket cell

**Synonyms** (with reference where available)
- PV basket cell (exact) — —
- PV+ basket cell (exact) — —
- parvalbumin basket cell (exact) — —

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A basket cell of the hippocampal formation that expresses the calcium-binding protein parvalbumin (Pvalb) in rodents (Rivera et al., 2014; Que et al., 2021; Contreras et al., 2019). Somata is located in the pyramidal layers of CA1 and CA3 and the granule cell layer of the dentate gyrus. Axon collaterals are confined to the pyramidal layer, forming dense perisomatic inhibitory synapses on the somata of principal neurons; a single cell contacts more than 1500 pyramidal neurons (Sik et al., 1995). This cell is a fast-spiking GABAergic interneuron with sustained firing rates exceeding 200 Hz, and is distinguished from CCK basket cells by absence of cannabinoid receptor 1 (Cnr1) expression (Whissell et al., 2015).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
basket cell (CL:0000118) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCL_0000118

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
hippocampal formation (UBERON:0002421) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0002421

**Your ORCID**
0000-0002-5507-2103

**Additional notes or concerns**
No hippocampus-specific PV basket cell term currently exists in CL. The existing term basket cell (CL:0000118) covers perisomatic-targeting GABAergic interneurons broadly but does not capture PV-specific identity. This gap prevents precise annotation of single-cell transcriptomic datasets in which PV basket cells, CCK basket cells, and axo-axonic cells are distinguishable by marker expression. The proposed term fills that gap and enables downstream reasoning: an `expresses some Pvalb` axiom distinguishes this population from CCK basket cells (which express Cnr1 and lack Pvalb), while `has soma location some hippocampal formation` scopes the term anatomically. Note that transcriptomic data (Que et al. 2021, PMID:33398060) demonstrate that hippocampal PV basket cells, bistratified cells, and axo-axonic cells are highly similar transcriptomically and can only be separated at the single-cluster level with morphologically confirmed data; this term should therefore be understood as defined primarily by morphology + marker expression rather than transcriptomic cluster identity alone.

Proposed logical axioms:
- subClassOf 'GABAergic neuron' (CL:0000617)
- subClassOf 'expresses' (RO:0002292) some 'parvalbumin alpha' (PR:000013502)
- subClassOf 'has soma location' (RO:0002100) some 'hippocampal formation' (UBERON:0002421)
- subClassOf 'capable of' (RO:0002215) some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534)

Key references:
- Sik et al. 1995 — PMID:7472426 — supports: morphology (axon collaterals confined to pyramidal layer; perisomatic innervation of >1500 pyramidal neurons; fast-spiking electrophysiology; immunoreactivity for parvalbumin confirmed by biocytin fill in rat CA1)
- Rivera et al. 2014 — PMID:25018703 — supports: Pvalb defining marker; soma location in CA1/CA3 stratum pyramidale and dentate gyrus granule cell layer (rat hippocampus, immunohistochemistry)
- Que et al. 2021 — PMID:33398060 — supports: Pvalb marker (transcript); high transcriptomic similarity among PV-IN morphological subtypes; patch-seq with confirmed basket morphology
- Whissell et al. 2015 — PMID:26441554 — supports: GABAergic neurotransmitter type; PV/CCK basket cell distinction (Cnr1-negative PV population)
- Contreras et al. 2019 — PMID:31297048 — supports: Pvalb as defining marker of perisomatic interneuron population; PV vs CCK framing

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml#pv_basket_cell_hippocampus`.*
*Source facts: `reports/hippocampus/pv_basket_cell_hippocampus_facts.json`.*

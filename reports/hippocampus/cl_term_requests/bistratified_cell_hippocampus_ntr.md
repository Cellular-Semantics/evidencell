# CL new term request: hippocampal bistratified interneuron

*Drafted from `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml` node `bistratified_cell_hippocampus` on 2026-05-13.*
*Source-KB current cl_mapping: bistratified cell (CL:0004247) — BROAD. Proposed parent in this NTR: interneuron (CL:0000099) with `bistratified cell` (CL:0004247) as a secondary parent — see "Action requested of CL editors" below.*

**Preferred term label**
hippocampal bistratified interneuron

**Synonyms** (with reference where available)
- bistratified cell of hippocampus (exact) — —
- CA1 bistratified cell (related) — —

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A hippocampal interneuron with its soma in or near the pyramidal layer of CA1 whose axon ramifies in a bilaminar pattern in CA1 stratum oriens and CA1 stratum radiatum, providing GABAergic dendritic inhibition to CA1 pyramidal cells (PMID:23162426, PMID:39401246, PMID:33404500, PMID:29321728). In mouse it co-expresses parvalbumin with somatostatin and Tac1, distinguishing it from PV basket cells, which target the perisomatic compartment, and from somatostatin-only oriens-lacunosum moleculare cells (PMID:33150866, PMID:37162922, PMID:37467748, PMID:33398060). Intersectional Sst;;Tac1 genetics labels this population, which preferentially synapses onto fast-spiking interneurons (PMID:38640347).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
interneuron (CL:0000099) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0000099

Plus secondary parent: bistratified cell (CL:0004247) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0004247 (see note below — definition needs CL-side adjustment to cover axonal as well as dendritic bistratification).

The hippocampal location is captured by the `has soma location` and `overlaps` axioms below and should be inferable from those plus the `interneuron` parent; we do not assert `hippocampal interneuron` (CL:1001569) as a direct parent.

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
pyramidal layer of CA1 (UBERON:0014548) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0014548

**Your ORCID**
0000-0002-7073-9172

**Additional notes or concerns**

**Action requested of CL editors — please address one of the following before merging this term, so the dual subClassOf is internally consistent:**

The existing CL term `bistratified cell` (CL:0004247) is defined as *"A neuron that stratifies dendrites at two and only two locations."* The hippocampal bistratified interneuron requested here is named for its **axonal** field — its axon arborises in CA1 stratum oriens and CA1 stratum radiatum, while its dendrites are not stratified (they are typically vertical/radial in stratum oriens). Under the current CL definition, asserting `subClassOf bistratified cell` for the hippocampal type is therefore not literally correct.

We have kept `subClassOf bistratified cell` in the proposed axioms because the community uses "bistratified" for both dendritic and axonal bilaminar morphologies, and because retaining the link makes the term findable by anyone searching the existing CL hierarchy. But CL needs to resolve this. Suggested options:

1. **Broaden** CL:0004247's definition to "A neuron that stratifies dendrites *or* axon at two and only two locations" (or split into a parent term covering both, with `retinal bistratified cell` and `hippocampal bistratified interneuron` as siblings).
2. **Sibling**: rename CL:0004247 to make its dendritic scope explicit (e.g. `dendritically bistratified neuron`) and place this new hippocampal term as a sibling rather than a subclass.

Whichever option is chosen, please also add an editor note to the resulting CL:0004247 (or its successor) flagging the dendrite-vs-axon homonymy, so future curators classifying axonally bistratified hippocampal interneurons do not place them under a dendrite-stratification term by mistake. The hippocampal usage is well-established in the literature (PMID:23162426, PMID:33404500, PMID:39401246) and the misclassification risk is real.

**Definitional summary for this term:**

The defining feature combination is (i) bilaminar CA1 SO + CA1 SR axonal field with soma in/near CA1 stratum pyramidale and (ii) Pvalb+/Sst+/Tac1+ co-expression. PV interneuron transcriptomic landscapes in hippocampus are continuous rather than discrete (PMID:33398060), so morphology + intersectional markers remain the most robust definitional handle.

**Mapping context to WMBv1** (CCN20230722; included as informational, not as part of the CL request): morphologically confirmed PV bistratified patch-seq cells from Que 2021 (GEO:GSE142546) reach F1 = 0.800 at cluster 0737 Pvalb Gaba_2 (CS20230722_CLUS_0737) within supertype 0206 Pvalb Gaba_2 (CS20230722_SUPT_0206), with bilaminar CA1 SO/SR anatomy and Sst:4.4, Tac1:7.3 NP profile on that cluster.

Proposed logical axioms:
- subClassOf 'interneuron' (CL:0000099)
- subClassOf 'bistratified cell' (CL:0004247) — see action-requested note above
- subClassOf 'has soma location' (RO:0002100) some 'pyramidal layer of CA1' (UBERON:0014548)
- subClassOf 'overlaps' (RO:0002131) some 'CA1 stratum oriens' (UBERON:0014552)
- subClassOf 'overlaps' (RO:0002131) some 'CA1 stratum radiatum' (UBERON:0014554)
- subClassOf 'capable of' (RO:0002215) some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534)

Notes on axioms:
- The `interneuron` parent + the location axioms together let the reasoner infer the hippocampal-interneuron grouping (CL:1001569) without us asserting it directly.
- The bilaminar axon field is the defining anatomical feature; `overlaps` (has some part in) is used for CA1 SO and CA1 SR because the axonal arbour, not the entire cell, occupies these layers (`part of` would be incorrect). See relations guide § Recording the location of neurons.
- `has soma location` captures the CA1 stratum pyramidale soma commitment; the property chain with `part of` extends this to CA1 / hippocampal formation automatically.
- `capable of` GABA secretion encodes the GABAergic neurotransmitter identity (PMID:29321728) as recommended for neurotransmitter axioms in the relations guide.
- Marker axioms (`expresses` for Pvalb, Sst, Tac1) are deliberately omitted: CL currently restricts `expresses` fillers to PRO IDs, and we have not validated PRO CURIEs here. The marker evidence appears in the textual definition instead.

Key references:
- Chamberland & Topolnik 2012 — PMID:23162426 — supports: bistratified cells provide dendritic inhibition; classical functional/morphological type
- Bocchio et al. 2024 — PMID:39401246 — supports: bistratified as a canonical hippocampal PV-expressing interneuron type
- Perez et al. 2020 — PMID:33404500 — supports: soma in CA1 stratum pyramidale (alongside basket and OLM cells)
- Dannenberg et al. 2017 — PMID:29321728 — supports: PV interneuron heterogeneity in hippocampus; bistratified as one of three PV+ types; GABAergic identity
- Ekins et al. 2020 — PMID:33150866 — supports: bistratified as one of four PV+ morphological subtypes
- Chamberland et al. 2023 — PMID:37162922 — supports: PV interneuron classification
- Tzilivaki et al. 2023 — PMID:37467748 — supports: PV/Sst co-expression in bistratified cells
- Que et al. 2021 — PMID:33398060 — supports: continuous PV transcriptomic landscape; morphological subtypes (hBIC, vBIC) identified by patch-seq
- Chamberland et al. 2024 — PMID:38640347 — supports: Sst;;Tac1 intersectional genetics labels bistratified cells; bistratified preferentially target fast-spiking interneurons

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml#bistratified_cell_hippocampus`.*
*Source facts: `reports/hippocampus/bistratified_cell_hippocampus_facts.json`.*

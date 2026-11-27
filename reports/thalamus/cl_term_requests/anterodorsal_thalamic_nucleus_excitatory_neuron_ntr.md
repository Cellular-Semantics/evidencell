# CL new term request: excitatory projection neuron of the anterodorsal nucleus of thalamus

*Drafted from `kb/graphs/thalamus/anterodorsal_thalamic_nucleus_excitatory_neuron.yaml` node `anterodorsal_thalamic_nucleus_excitatory_neuron` on 2026-11-27.*
*Parent (current cl_mapping): thalamic excitatory neuron (CL:4023068) — BROAD*

**Preferred term label**
excitatory projection neuron of the anterodorsal nucleus of thalamus

**Synonyms** (with reference where available)
- anterodorsal thalamic nucleus excitatory projection neuron (exact — the source KB node name) — PMID:40593635
- AD glutamatergic neuron (related — abbreviation-based, not proposed for the ontology) — PMID:40593635
(The source KB records no `synonyms` list for this node; the entries above are drawn from the node name and from the wording used in the cited primary sources.)

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A thalamic excitatory neuron with its soma in the anterodorsal nucleus of thalamus, one of the anterior thalamic nuclei (PMID:40593635; PMID:38427564). It is glutamatergic (PMID:40593635; PMID:36476860) and in mouse expresses Pvalb (PMID:40593635) and Htr2a, which this nucleus expresses more highly than any other thalamic nucleus (PMID:40957902). It is the only thalamic target of the lateral mammillary nucleus, which innervates it bilaterally, and it is reciprocally connected with postsubiculum and presubiculum (PMID:33309908; PMID:25538571; PMID:33069688). Head-direction cells are more prominent among this population than in the anteroventral nucleus (PMID:25195980). Its axons also reach retrosplenial and visual cortex and mammillary regions (PMID:40593635).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
thalamic excitatory neuron (CL:4023068) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_4023068

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
anterodorsal nucleus of thalamus (UBERON:0002679) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002679

**Your ORCID**
[To be added by submitter]

**Additional notes or concerns**

*Read this section first: CL already contains two anterodorsal-named terms, and this request must be judged against them.* A CL search (OLS4, 2026-11-27) for "anterodorsal" returns CL:4301071 'AD Serpinb7 Glut glutamatergic neuron (Mmus)' and its child CL:4304433 'AD Serpinb7 Glut_1 Has2os glutamatergic neuron (Mmus)'. Both are Allen Whole Mouse Brain atlas-derived terms (supertype CS20230722_SUPT_0641 and cluster CS20230722_CLUS_2613 respectively, from Yao et al. 2023), and both are asserted children of the proposed parent CL:4023068. **The source KB's `cl_mapping` notes for this node state that no nucleus-specific CL term exists; that statement is out of date and the curator should correct it.** Per the repository's CL-mapping procedure an existing `cl_mapping` is not edited by this workflow, so the node YAML has been left unchanged and the disagreement is recorded here.

*Why a separate term is nevertheless proposed — and the case against it.* The two existing terms are defined by transcriptomic cluster membership, with the caveat printed in their own definitions that "Location is inferred from registration of MerFish Data. Registration may be inaccurate, giving misleading location to adjacent anatomical regions"; CL:4304433 places its cells "in or close to the regions: Anterodorsal nucleus, stria medullaris". Their differentia are Serpinb7, Eps8l2, C1ql2 and Has2os. The population described here is defined classically, by soma location in the nucleus plus its connectional signature (sole thalamic target of the lateral mammillary nucleus, reciprocal with postsubiculum, head-direction coding), and its recorded markers are different ones — Pvalb and Htr2a. Notably C1ql2, a differentia of the atlas terms, is recorded in the source KB as a marker of the *anteroventral* nucleus population, not this one. The two definitions have not been shown to pick out the same cells, and the source KB records no atlas mapping edge for this node (its `edges` list is empty). Editors who regard the atlas supertype as already covering the nucleus should decline this request rather than merge the two; editors who regard atlas-cluster terms and classically defined nucleus terms as different kinds of class should treat this as a genuine gap. That judgement is CL's to make, and it is put here explicitly rather than buried.

*Htr2a is the strongest molecular differentia on offer.* Ekins et al. 2025 (PMID:40957902) report by MERFISH and Thalamoseq RNA-seq re-analysis, confirmed by RNAScope FISH, that this nucleus expresses Htr2a more highly than all other thalamic nuclei. That is a comparative, within-thalamus claim and is the only marker here with a stated assay. Pvalb comes from a marker statement whose assay is not stated (PMID:40593635), and is in any case widely expressed elsewhere in the brain. Slc17a6 is recorded on the parent KB node (anterior thalamic nuclei excitatory projection neuron) and applies here only by inheritance, so it is not offered as a differentia.

*A transgene non-label that is not a negative marker.* The Grp_KH288-Cre driver labels a subset of anteroventral neurons and none in this nucleus (PMID:30858601). This is BAC-transgenic labelling and does not establish absence of endogenous Grp transcript. The source KB deliberately does not record it as a gene marker, and it is not proposed as one here.

*Internal heterogeneity.* Hintiryan et al. 2025 (PMID:40593635) divide this nucleus into two projection-defined types — AD1 (dorsolateral; postsubiculum, laterodorsal and laterointermediate visual areas, subcortical mammillary regions) and AD2 (ventromedial; retrosplenial, visual, postsubicular, mammillary regions) — and report no marker separating them. Kapustina et al. 2024 (PMID:38427564) report graded dorsomedial-to-ventrolateral transcriptional variation within the nucleus. The requested term covers the nucleus-level population; the two projection types are not proposed as separate terms.

*Head-direction coding is cited but not axiomatised.* CL has no head-direction cell term (searched 2026-11-27), and the cited evidence (PMID:25195980) is a review of in vivo single-unit recordings. Head-direction cells are reported as more prominent in this nucleus than in the anteroventral nucleus, but not as the property of every neuron in it, so the claim cannot support an "all instances" axiom. No intrinsic (slice) electrophysiology is recorded for this population. A perturbation phenotype — hyperexcitability after knockdown of autism and schizophrenia risk genes expressed in this nucleus (PMID:34197733) — is recorded in the source KB as a perturbation result and is deliberately not treated as a baseline electrophysiological property.

*Species.* The source KB sets the node's species to Mus musculus on the basis of its defining sources (PMID:40593635, PMID:38427564). Some cited evidence is rat: the collateralisation analysis showing this nucleus provides the greatest proportion of neurons bifurcating to different retrosplenial areas, up to about 15% of labelled cells (PMID:36089888), and the head-direction recording literature. Each source's species is recorded in its scope in the KB. Taxon-restricting the term is not proposed.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'anterodorsal nucleus of thalamus' (UBERON:0002679)
- subClassOf 'sends synaptic output to region' (RO:0013003) some 'postsubiculum' (UBERON:0035971) — proposed because both projection-defined types of this nucleus, AD1 and AD2, are reported to target postsubicular cortex, so it is the one output region that holds across the whole class. Support is a single source (PMID:40593635); editors who want two independent sources before asserting connectivity should drop it.

Inherited from the parent and so not restated as an assertion (listed only so editors can confirm it is intended): CL:4023068 already places the term under 'glutamatergic neuron' (CL:0000679) and 'glutamatergic projection neuron' (CL:0020141), which is how the source KB records the transmitter phenotype (`nt_type.cl_terms` = CL:0000679).

Axioms considered and deliberately **not** proposed:
- `receives synaptic input in region` (RO:0013002) some 'lateral mammillary nucleus' (UBERON:0001938) — this would be **wrong in direction**. The relation holds between a neuron and the region in which that neuron has input synapses; the mammillothalamic input is received in this nucleus, not in the lateral mammillary nucleus. The correct shape would be `synapsed by` (RO:0002103) some lateral-mammillary-neuron class, and CL has no such class. Please do not insert the inverted form.
- `expresses` some Htr2a / Pvalb — CL permits only PRO identifiers as fillers for `expresses`. Htr2a would be the one worth adding if a PRO identifier is acceptable to editors, given it is the only comparatively quantified, assay-stated marker here; Pvalb is not specific enough to axiomatise.
- `has characteristic` (RO:0000053) some PATO quality — the morphology field records a somatodendritic plan inherited from the parent type plus axonal projection patterns, neither of which PATO captures, and no slice electrophysiology exists for this population.

Key references:
- Hintiryan et al. 2025 — PMID:40593635 — supports: soma location in the anterodorsal nucleus; glutamatergic identity of all projection-defined anterior thalamic types; Pvalb marker; AD1/AD2 projection-defined subdivision and their cortical and subcortical targets (brain-wide anterograde and retrograde connectomics, mouse)
- Kapustina et al. 2024 — PMID:38427564 — supports: a discrete excitatory cluster corresponding to this nucleus, and graded transcriptional variation within it (scRNA-seq, spatial transcriptomics and multiplexed FISH, mouse)
- Ekins et al. 2025 — PMID:40957902 — supports: Htr2a expressed more highly in this nucleus than in any other thalamic nucleus (MERFISH and Thalamoseq RNA-seq re-analysis confirmed by RNAScope FISH, mouse)
- Govek et al. 2022 — PMID:36476860 — supports: glutamatergic identity of the anterior thalamic nuclei, which differentiate first among thalamic nuclei (embryonic scRNA-seq lineage trajectories, mouse)
- Dillingham et al. 2020 — PMID:33309908 — supports: lateral mammillary nucleus projects exclusively and bilaterally to this nucleus (head-direction system)
- Makarenko et al. 2014 — PMID:25538571 — supports: the mammillothalamic projection to this nucleus
- Mathiasen et al. 2020 — PMID:33069688 — supports: reciprocal connections with postsubiculum and presubiculum
- Aggleton et al. 2015 — PMID:25195980 — supports: head-direction cells more prominent in this nucleus than in the anteroventral nucleus (review of in vivo single-unit recording literature, rodent)
- Yanakieva et al. 2022 — PMID:36089888 — supports: this nucleus provides the greatest proportion of neurons bifurcating to different retrosplenial areas, up to about 15% of labelled cells (dual retrograde tracing, rat)
- Yamawaki et al. 2018 — PMID:30858601 — supports: Grp_KH288-Cre labels anteroventral but not anterodorsal neurons (anterograde AAV-ChR2 tracing, mouse)
- Roy et al. 2021 — PMID:34197733 — supports: autism and schizophrenia risk-gene expression in this nucleus and hyperexcitability after knockdown (perturbation phenotype, mouse)

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/thalamus/anterodorsal_thalamic_nucleus_excitatory_neuron.yaml#anterodorsal_thalamic_nucleus_excitatory_neuron`.*
*Source facts: `reports/thalamus/anterodorsal_thalamic_nucleus_excitatory_neuron_facts.json`.*

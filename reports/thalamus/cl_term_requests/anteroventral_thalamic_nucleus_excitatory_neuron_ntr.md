# CL new term request: excitatory projection neuron of the anteroventral nucleus of thalamus

*Drafted from `kb/graphs/thalamus/anteroventral_thalamic_nucleus_excitatory_neuron.yaml` node `anteroventral_thalamic_nucleus_excitatory_neuron` on 2026-11-27.*
*Parent (current cl_mapping): thalamic excitatory neuron (CL:4023068) — BROAD*

**Preferred term label**
excitatory projection neuron of the anteroventral nucleus of thalamus

**Synonyms** (with reference where available)
- anteroventral thalamic nucleus excitatory projection neuron (exact — the source KB node name) — PMID:40593635
- AV glutamatergic neuron (related — abbreviation-based, not proposed for the ontology) — PMID:40593635
(The source KB records no `synonyms` list for this node; the entries above are drawn from the node name and from the wording used in the cited primary sources.)

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A thalamic excitatory neuron with its soma in the anteroventral nucleus of thalamus, one of the anterior thalamic nuclei of the Papez circuit (PMID:40593635; PMID:38427564). It is glutamatergic (PMID:40593635; PMID:36476860) and in mouse expresses C1ql2 and Bdnf (PMID:40593635). It is the principal thalamic source of input to granular retrosplenial cortex, terminating most heavily in layer 1 and particularly layer 1a with sparser branching in deeper layers; single axons are heterogeneous, some arborising only in layer Ia and others also in layers III and IV (PMID:30858601; PMID:22013412; PMID:32964131). It receives input from the medial mammillary nucleus (PMID:33309908). Head-direction cells are recorded among this population, less prominently than in the anterodorsal nucleus (PMID:25195980).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
thalamic excitatory neuron (CL:4023068) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_4023068

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
anteroventral nucleus of thalamus (UBERON:0002685) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002685

**Your ORCID**
[To be added by submitter]

**Additional notes or concerns**

*What gap this fills.* CL has no neuron term scoped to any individual anterior thalamic nucleus. Searching CL (OLS4, 2026-11-27) for "anteroventral thalamic", "anteroventral nucleus of thalamus neuron", "anterior thalamic" and "head direction" returns no cell term for this population; the only CL hit mentioning the anteroventral nucleus of thalamus is CL:4303809 'BST-po Iigp1 Glut glutamatergic neuron (Mmus)', where the nucleus is named only as a possible MERFISH registration neighbour, not as the cell's location. The proposed parent CL:4023068 'thalamic excitatory neuron' is defined simply as an excitatory neuron with soma in the dorsal plus ventral thalamus, so it contains this population without distinguishing it. Its asserted children are all Allen Whole Mouse Brain atlas-derived terms; one of them, CL:4301071 'AD Serpinb7 Glut glutamatergic neuron (Mmus)', covers the neighbouring anterodorsal nucleus, but there is no anteroventral counterpart. This request is therefore for a classically (anatomically and connectionally) defined nucleus-level child, and a sibling request is being drafted for the anterodorsal nucleus.

*Relationship to the atlas-derived terms — please do not treat as equivalent.* The term requested here is defined by soma location in a named nucleus plus projection target, not by a transcriptomic cluster. It is not asserted to be the same class as any Whole Mouse Brain supertype, and the source KB records no atlas mapping edge for this node (its `edges` list is empty). If CL editors prefer to align the two, that alignment needs atlas-mapping evidence that does not yet exist.

*The molecular differentia are weak, and this should be stated plainly.* The only positive markers recorded are C1ql2 and Bdnf, both from a single source (PMID:40593635) whose assay is not stated; the source KB records their `marker_type` as NOT_STATED. Neither is claimed to be exclusive to this nucleus. The real differentia on offer are **anatomical** (soma in the anteroventral nucleus) and **connectional** (dense, layer-1a-biased input to granular retrosplenial cortex; mammillothalamic input from the medial mammillary nucleus). If CL editors require a molecular differentia, this request should be deferred rather than padded. Slc17a6 is recorded on the parent KB node (anterior thalamic nuclei excitatory projection neuron) and applies here only by inheritance, so it is not offered as a differentia.

*A transgene label that is not a marker.* The Grp_KH288-Cre driver labels a subset of anteroventral neurons and none in the anterodorsal nucleus (PMID:30858601). This is BAC-transgenic labelling of a subset, and does not establish endogenous Grp expression. The source KB deliberately does not record it as a gene marker, and it is not proposed as one here.

*Internal heterogeneity.* Hintiryan et al. 2025 (PMID:40593635) divide this nucleus into three projection-defined types — AV1 (dorsomedial; prelimbic, anterior cingulate, anterior retrosplenial), AV2 (ventrolateral; granular retrosplenial, ventral visual stream) and AV3 (dorsolateral; prefrontal and visual cortex) — without reporting a marker unique to any of them. Kapustina et al. 2024 (PMID:38427564) report a dorsomedial-to-ventrolateral transcript gradient that covaries with protein products and long-range inputs, i.e. suspected continuous rather than discrete heterogeneity. The requested term covers the nucleus-level population; the three projection types are not proposed as separate terms.

*Head-direction coding is cited but not axiomatised.* CL has no head-direction cell term (searched 2026-11-27). The cited evidence (PMID:25195980) is a review of in vivo single-unit recordings reporting head-direction cells in this nucleus at lower prevalence than in the anterodorsal nucleus, so the property does not hold of all instances and cannot support an "all instances" axiom. No intrinsic (slice) electrophysiology is recorded for this population at all.

*Species.* The source KB sets the node's species to Mus musculus on the basis of its defining sources (PMID:40593635, PMID:38427564), but some cited evidence is rat — the single-axon reconstruction (PMID:22013412), the anterograde tracing of retrosplenial and anterior cingulate terminations (PMID:32964131) and the head-direction recordings. Each source's species is recorded in its scope in the KB. Taxon-restricting the term is not proposed.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'anteroventral nucleus of thalamus' (UBERON:0002685)

Inherited from the parent and so not restated as an assertion (listed only so editors can confirm it is intended): CL:4023068 already places the term under 'glutamatergic neuron' (CL:0000679) and 'glutamatergic projection neuron' (CL:0020141), which is how the source KB records the transmitter phenotype (`nt_type.cl_terms` = CL:0000679).

Axioms considered and deliberately **not** proposed:
- `sends synaptic output to region` (RO:0013003) some 'retrosplenial granular cortex' (UBERON:0014918) — this is the best-supported connectional fact in the dossier and editors may well want it. It is withheld here only because the source evidence resolves the nucleus into three projection types with different cortical targets (AV1 to prefrontal/anterior cingulate, AV2 to granular retrosplenial and ventral visual stream, AV3 to prefrontal and visual cortex; PMID:40593635), so an "all instances" axiom over the nucleus-level class is not safe on the current evidence. If editors prefer to assert it, PMID:30858601 and PMID:22013412 are the primary support.
- `receives synaptic input in region` (RO:0013002) some 'mammillary body' — the input is specifically from the medial mammillary nucleus, pars lateralis (PMID:33309908; PMID:25538571), and the axiom would be about the presynaptic cell's territory rather than this cell's; left to editor discretion.
- `expresses` some C1ql2 / Bdnf — CL permits only PRO identifiers as fillers for `expresses`, and these markers come from one source with an unstated assay and no exclusivity claim. Not proposed.
- `has characteristic` (RO:0000053) some PATO quality — no PATO-mappable morphology or electrophysiology is recorded; the morphology field describes axonal arborisation patterns, which PATO does not capture, and the arborisation is itself heterogeneous between single axons (PMID:22013412).

Key references:
- Hintiryan et al. 2025 — PMID:40593635 — supports: soma location in the anteroventral nucleus; glutamatergic identity of all projection-defined anterior thalamic types; C1ql2 and Bdnf markers; the AV1/AV2/AV3 projection-defined subdivision (brain-wide connectomics plus molecular markers, mouse)
- Kapustina et al. 2024 — PMID:38427564 — supports: a discrete anteroventral excitatory cluster, and a dorsomedial-ventrolateral transcript gradient covarying with protein products and long-range inputs (scRNA-seq, spatial transcriptomics and multiplexed FISH, mouse)
- Yamawaki et al. 2018 — PMID:30858601 — supports: anteroventral nucleus as the major thalamic source to granular retrosplenial cortex, layer-1/1a-biased termination; Grp_KH288-Cre labelling of a subset (anterograde AAV-ChR2 tracing, mouse)
- Odagiri et al. 2011 — PMID:22013412 — supports: heterogeneity of single anteroventral axons in granular retrosplenial cortex, type 1 arborising only in layer Ia and type 2 also in layers III/IV (single-axon BDA reconstruction, rat)
- Bubb et al. 2020 — PMID:32964131 — supports: heavy termination in layers 1-4 of granular retrosplenial cortex and a light layer-1-restricted projection to anterior cingulate area Cg2 (anterograde tracing, rat)
- Govek et al. 2022 — PMID:36476860 — supports: glutamatergic identity of the anterior thalamic nuclei, which differentiate first among thalamic nuclei (embryonic scRNA-seq lineage trajectories, mouse)
- Dillingham et al. 2020 — PMID:33309908 — supports: input from the medial mammillary nucleus (pars lateralis)
- Makarenko et al. 2014 — PMID:25538571 — supports: mammillothalamic input to the anteroventral nucleus
- Aggleton et al. 2015 — PMID:25195980 — supports: head-direction cells present in the anteroventral nucleus, less prominently than in the anterodorsal nucleus (review of in vivo single-unit recording literature, rodent)

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/thalamus/anteroventral_thalamic_nucleus_excitatory_neuron.yaml#anteroventral_thalamic_nucleus_excitatory_neuron`.*
*Source facts: `reports/thalamus/anteroventral_thalamic_nucleus_excitatory_neuron_facts.json`.*

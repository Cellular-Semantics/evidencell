# CL new term request: neuropeptide Y-expressing GABAergic projection neuron of the intergeniculate leaflet

*Drafted from `kb/graphs/thalamus/igl_npy_geniculohypothalamic_neuron.yaml` node `igl_npy_geniculohypothalamic_neuron` on 2026-11-27.*
*Parent (current cl_mapping): NPY interneuron (CL:4072016) — RELATED*

**Preferred term label**
neuropeptide Y-expressing GABAergic projection neuron of the intergeniculate leaflet

**Synonyms** (with reference where available)
- intergeniculate leaflet NPY-positive geniculohypothalamic neuron (exact — the source KB node name) — PMID:23103793
- NPY-positive neuron of the geniculohypothalamic tract (exact) — PMID:23432696
- IGL NPY neuron (related — abbreviation-based, not proposed for the ontology) — PMID:27916729
(The source KB records no `synonyms` list for this node; the entries above are drawn from the node name and from the wording used in the cited primary sources.)

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A GABAergic projection neuron with its soma in the intergeniculate leaflet of the lateral geniculate complex, one of the two principal GABAergic populations of that leaflet and interspersed with the enkephalinergic population (PMID:23103793; PMID:27916729). It synthesises neuropeptide Y (Npy in rat) and its axons form the geniculohypothalamic tract, terminating in the suprachiasmatic nucleus (PMID:23103793; PMID:23432696; PMID:25856520). In rat every neuropeptide Y-positive neuron of this leaflet shows a marked A-type potassium current (PMID:27208616). Recorded in vivo after antidromic identification of the suprachiasmatic projection, these cells fire at a low, irregular rate in the light, and most increase firing in darkness (PMID:23103793).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
GABAergic projection neuron (CL:0020140) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0020140

Recommended additional asserted parent:
thalamus GABAergic neuron (CL:0020129) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0020129

**Note that this parent is NOT the term recorded in the source KB's `cl_mapping`** — see the first note below. This is the single point on which a curator decision is needed before posting.

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
intergeniculate leaflet of the lateral geniculate complex (UBERON:0035975) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0035975

**Your ORCID**
[To be added by submitter]

**Additional notes or concerns**

*Read this first: the proposed parent differs from the source KB's `cl_mapping`, deliberately.* The KB records `cl_mapping` as RELATED to CL:4072016 'NPY interneuron', with the explicit note that the match is RELATED precisely because CL:4072016 is an **interneuron** term while this population consists of **projection** neurons sending axons out of the leaflet to the suprachiasmatic nucleus. A RELATED mapping by definition does not name a parent — the repository's CL-mapping procedure states that for RELATED mappings the parent must be chosen by a curator — and asserting CL:4072016 as the parent would place a projection neuron under an interneuron class, which is a taxonomic error. CL:4072016 is therefore cited here as the closest *related* term, not as the parent. Two containing terms were found by search (OLS4, 2026-11-27) and are proposed instead: CL:0020140 'GABAergic projection neuron' ("A projection neuron that uses GABA as a vesicular neurotransmitter") and CL:0020129 'thalamus GABAergic neuron' ("A GABAergic neuron that has its soma located in the dorsal plus ventral thalamus"). UBERON places the intergeniculate leaflet under 'dorsal plus ventral thalamus' (UBERON:0001897) via the lateral geniculate body and metathalamus, verified in OLS4, so the second parent holds. **Recommended curator action: add a BROAD `cl_mapping` to CL:0020140 on this node before posting.** The node YAML has been left unchanged, since the repository's procedure forbids this workflow from editing an existing `cl_mapping`.

*What gap this fills.* CL contains no term mentioning the intergeniculate leaflet at all — a CL full-text search for "intergeniculate leaflet" and for "geniculohypothalamic" returns zero cell terms (OLS4, 2026-11-27). The nearest terms are the two proposed parents, neither of which distinguishes this population, and CL:4072016, whose definition locates NPY interneurons in "cortical layers II–III and VI, as well as in various brain regions such as the medial geniculate and inferior colliculus" — not the intergeniculate leaflet, and not as projection neurons. The leaflet is the origin of the geniculohypothalamic tract and the principal non-photic input route to the circadian clock, so this is a substantive gap rather than a naming variant.

*What distinguishes this term from its sibling.* The leaflet's GABAergic neurons divide into two populations with different peptides and different targets: this one, neuropeptide Y-positive and projecting to the suprachiasmatic nucleus, and an enkephalinergic one projecting to the contralateral leaflet (PMID:23103793; PMID:27916729). A sibling new term request is being drafted for the enkephalinergic population. The two should be reviewed together; they are the two halves of one division and neither makes full sense alone.

*Marker evidence is immunohistochemical, not transcriptomic.* The neuropeptide Y assertion rests on protein detection — post hoc NPY immunofluorescence in identified neurons (PMID:23432696) and statements in sources whose assay is not specified (PMID:23103793; PMID:27916729). The source KB records Npy as the rat-convention gene symbol for the protein "NPY" named in the sources, under both `defining_markers` and `neuropeptides`. No transcript-level measurement is claimed. Editors should read the marker as peptide content, which is what the cited work shows.

*A real risk of over-inclusion, which editors should weigh.* Thankachan and Rusak 2005 (PMID:16207879) describe Type II leaflet/ventral-lateral-geniculate neurons carrying large amounts of NPY throughout the soma, which the source KB takes to correspond to this class, and Type III neurons carrying patchy, internalised NPY which they interpret as NPY **recipients, not producers**. NPY immunolabel alone therefore does not identify this class, and the source KB explicitly instructs that Type III cells must not be assigned here. Note also that the anatomy in that study is "IGL/VLG", not the leaflet alone. Any future attempt to ground this term in an NPY-immunoreactivity dataset needs to respect that distinction.

*Pharmacology deliberately excluded from the definition.* Met-enkephalin hyperpolarises putatively NPY-synthesising leaflet neurons via mu-opioid receptors (PMID:27916729), and identified NPY-positive leaflet neurons are excited by the relaxin-3 receptor agonist R3/I5 (PMID:23432696). The source KB keeps the met-enkephalin result out of the electrophysiology description because the supporting quote does not isolate this class. Neither is used as a differentia here.

*Cross-species note, not asserted.* In cat, suprachiasmatic-projecting neurons and NPY-immunoreactive processes are found in the medial ventral lateral geniculate nucleus, which has been proposed as homologous to the rodent intergeniculate leaflet (PMID:8836531). The source KB records this but does not assert it as a location for this rat-defined node, and no taxon restriction is proposed here.

*Species.* The source KB scopes this node to Rattus norvegicus; every cited primary source is rat. CL terms are normally species-neutral and no taxon restriction is proposed, but editors should know the evidence base is single-species.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'intergeniculate leaflet of the lateral geniculate complex' (UBERON:0035975)
- subClassOf 'sends synaptic output to region' (RO:0013003) some 'suprachiasmatic nucleus' (UBERON:0002034) — this is the defining projection of the class (the geniculohypothalamic tract) and is supported by three independent sources (PMID:23103793; PMID:23432696; PMID:25856520), so unlike most connectivity axioms it holds of the class as a whole.
- subClassOf 'expresses' (RO:0002292) some 'neuropeptide Y' (PR:000011387) — if editors prefer a taxon-specific filler, the rat entry is 'pro-neuropeptide Y (rat)' (PR:P07808). Please see the immunohistochemistry caveat above before treating this as a transcriptomic claim.

Inherited from the parent and so not restated as an assertion (listed only so editors can confirm it is intended): 'capable of' (RO:0002215) some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534), which is how the source KB records the transmitter phenotype (`nt_type.cl_terms` = CL:0000617 'GABAergic neuron'). If CL:0020129 'thalamus GABAergic neuron' carries an equivalence axiom over soma location in the dorsal plus ventral thalamus, the soma-location axiom above should autoclassify the term under it through the `has_soma_location o part_of` property chain, and the second asserted parent would then be redundant.

Axioms considered and deliberately **not** proposed:
- `has characteristic` (RO:0000053) some PATO quality for the A-type potassium current — PATO has no term for a specific ionic current, and the morphology field records no somatodendritic description for this population at all ("No somatodendritic description in the evidence"). Nothing here is PATO-mappable.
- `lacks_plasma_membrane_part` some enkephalin — the source KB records no negative marker on this node (the Npy-negative assertion sits on the sibling enkephalinergic node, not here), so there is nothing to axiomatise, and enkephalin is a secreted peptide rather than a plasma membrane component in any case.
- A light-response or circadian-firing axiom — the in vivo firing pattern is a state-dependent response (low and irregular in light, increased in darkness), not a static characteristic, and the definition guidelines warn against qualities that describe a change.

Key references:
- Blasiak et al. 2013 — PMID:23103793 — supports: the leaflet as a GABAergic population divisible into two anatomically and neurochemically distinct groups; NPY-positive neurons forming the geniculohypothalamic tract to the suprachiasmatic nucleus; low irregular firing in light and increased firing in darkness (in vivo extracellular recording with antidromic identification, rat)
- Palus et al. 2017 — PMID:27916729 — supports: the two main GABAergic subpopulations of the leaflet, NPY-synthesising and enkephalinergic; mu-opioid hyperpolarisation of putatively NPY-synthesising cells (slice electrophysiology, rat)
- Blasiak A. et al. 2013 — PMID:23432696 — supports: NPY-containing neurons forming the geniculohypothalamic tract, by post hoc NPY immunofluorescence; excitation by the relaxin-3 receptor agonist R3/I5 (in vitro patch clamp with post hoc identification, rat)
- Chrobok et al. 2016 — PMID:27208616 — supports: a marked A-type potassium current in all NPY-positive leaflet neurons; the two-subpopulation division (whole-cell patch clamp with NPY identification, rat)
- Palus et al. 2015 — PMID:25856520 — supports: abundant leaflet-derived NPY-positive fibres in the suprachiasmatic nucleus (statement citing tract-tracing and immunohistochemistry, rodent)
- Palus-Chramiec et al. 2019 — PMID:30803080 — supports: leaflet GABAergic neurons co-expressing NPY (statement citing Moore et al., 1994, rat)
- Thankachan and Rusak 2005 — PMID:16207879 — supports: the Type II versus Type III distinction and the warning that NPY immunolabel alone does not identify NPY-producing cells (rat/hamster leaflet and ventral lateral geniculate)
- Pu and Pickard 1996 — PMID:8836531 — supports: suprachiasmatic-projecting neurons and NPY-immunoreactive processes in medial ventral lateral geniculate of cat, proposed as homologous to the rodent leaflet

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/thalamus/igl_npy_geniculohypothalamic_neuron.yaml#igl_npy_geniculohypothalamic_neuron`.*
*Source facts: `reports/thalamus/igl_npy_geniculohypothalamic_neuron_facts.json`.*

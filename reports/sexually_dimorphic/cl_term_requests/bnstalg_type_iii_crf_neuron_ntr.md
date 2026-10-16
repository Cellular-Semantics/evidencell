# CL new term request: Cav3.3-expressing corticotropin-releasing neuron of the bed nucleus of the stria terminalis

*Drafted from `kb/graphs/sexually_dimorphic/dlbnst_crf.yaml` node `bnstalg_type_iii_crf_neuron` on 2026-09-11.*
*Parent (current cl_mapping): corticotropin-releasing neuron (CL:4072021) — BROAD*

**Preferred term label**

Cav3.3-expressing corticotropin-releasing neuron of the bed nucleus of the stria terminalis

*Label alternatives for editor consideration (the molecular differentia must stay in the label — see "Additional notes or concerns", point 1):*
- oxytocin receptor-expressing corticotropin-releasing neuron of the bed nucleus of the stria terminalis
- GABAergic corticotropin-releasing neuron of the anterior division of the bed nucleus of the stria terminalis *(not recommended — collides with the broader BNST CRF population term requested separately)*

**Synonyms** (with reference where available)

- Type III BNSTALG neuron (exact) — PMID:21310239 — the primary literature label for this class (KB `synonym_type: ABBREVIATION`); retained as an exact synonym although the electrophysiological Type III class is ~95%, not 100%, Crh-positive
- putative CRF neuron of the BNSTALG (related) — PMID:24009552 — informal term used when introducing the Type III / CRF association (KB `synonym_type: INFORMAL`)

*These are the only two synonyms asserted on the KB node; no others have been added.*

**Definition** (with inline references; PMID:XXXXXX or DOI format)

A corticotropin-releasing neuron whose soma lies in the anterior division of the bed nucleus of the stria terminalis, chiefly its oval nucleus, and which is GABAergic rather than neuroendocrine, expressing Gad1 but no vesicular glutamate transporter (Slc17a6, Slc17a7, Slc17a8) in rat (PMID:24009552). Among neighbouring bed-nucleus neurons it is distinguished in rat by an ion-channel transcript signature: Cacna1i (Cav3.3) in every cell with Cacna1g (Cav3.1) absent, Hcn4 as the only hyperpolarisation-activated subunit, together with Kcnd2, Kcnj12 and Kcnj4, and neither Kcna4 nor Htr7 (PMID:21310239); correspondingly it shows little discernible Ih and the largest inward-rectifier current. Roughly 95% co-express Crh and Oxtr (PMID:24009552), and Crh transcript rises selectively after chronic stress (PMID:30878403).

*(110 words, single paragraph.)*

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)

corticotropin-releasing neuron (CL:4072021) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_4072021

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)

anterior division of bed nuclei of stria terminalis (UBERON:0011173) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011173

Secondary / enrichment: oval nucleus of stria terminalis (UBERON:0011176) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011176

*Anatomy choice and its justification.* The KB node currently carries the broader
UBERON:0001880 'bed nucleus of stria terminalis'. Hazra et al. reconstructed their
recording sites and reported that the sampled neurons lay in the oval (BNSTov),
juxtacapsular (BNSTju) and anterolateral (BNSTal) nuclei:

> the majority of neurons recorded were located within the boundaries of the oval nucleus (BNSTov) of the BNST, however, several cells were recorded that were located in the juxtacapsular (BNSTju) and anterolateral nuclei (BNSTal). <!-- quote_key: 8615463_e974a9fd -->
<!-- quote_key: 8615463_e974a9fd -->

All three of those nuclei are components of UBERON:0011173, so that term is the most
specific single UBERON class that still contains the whole sampled population — it is a
genuine refinement of UBERON:0001880 without over-claiming. UBERON:0011176
'oval nucleus of stria terminalis' is where most recorded cells were found, but not all
of them, so it is offered only as an enrichment statement and is **not** used in the
`has soma location` axiom. Note also that the "anterolateral cell group" (BNSTALG)
grouping used throughout this literature — oval + juxtacapsular + anterolateral
(+ rhomboid) nuclei — has no dedicated UBERON class; neither "anterolateral area of
stria terminalis" nor "juxtacapsular nucleus of stria terminalis" returns a UBERON
term in OLS4 (MBA:546 exists for the mouse juxtacapsular nucleus). A UBERON request
for the anterolateral group would let this axiom be tightened further.

**Your ORCID**

[To be added by submitter]

**Additional notes or concerns**

**1. What gap this fills relative to the parent term.** CL:4072021
'corticotropin-releasing neuron' is defined almost entirely around the hypothalamic
paraventricular nucleus (PVN) parvocellular population and is classified in CL under
'neuroendocrine cell' and 'adrenocorticotropic hormone secreting cell'. An OLS sweep
found no existing CL term for any BNST CRF subtype, nor for any BNST-specific cell
class at all, so a BNST-resident, GABAergic, non-neuroendocrine CRF class has no
representation. Positively contrasting evidence exists: whereas 83% of PVN
parvocellular CRF neurons co-express Oxt and none express Oxtr, this population is
uniformly Oxt-negative and 95% Oxtr-positive:

> . Significantly, unlike parvocellular CRF neurons that showed 83% co-expression with OT mRNA transcripts, none of the Type III CRF neurons tested co-expressed OT. Conversely, whereas 95% of Type III neurons expressed transcripts for OTR (18/19), no parvocellular CRF neurons expressed OTR transcripts. <!-- quote_key: 4940077_383bf7ef -->
<!-- quote_key: 4940077_383bf7ef -->

Editors may also wish to revisit whether the neuroendocrine / ACTH-secreting parentage
asserted on CL:4072021 should be inherited by an extra-hypothalamic GABAergic class, or
whether that parentage belongs on a PVN-specific child of CL:4072021 instead. This
request does not depend on that decision, but the new term's placement under
CL:4072021 will drag in 'epithelial cell' ancestry as the hierarchy currently stands.

**2. Scoping: this is a SUBSET of the BNST CRF population, not a synonym for it.** The
measured quantity is P(Crh+ | Type III) = 0.95 (PMID:24009552). The converse,
P(Type III | Crh+), is **not** measured anywhere in the supporting corpus, and
Silberman et al. 2013 (PMID:23325234) report at least four electrophysiologically
separable subtypes among genetically identified mouse BNST CRF neurons. This term must
therefore not be treated as covering the whole BNST CRF population. A separate, broader
NTR for the BNST CRF population is being drafted concurrently from the sibling KB node
`bnst_crf_neuron`; if both are accepted, that broader term is the appropriate
intermediate parent for this one, sitting between it and CL:4072021.

**3. Species.** All of the Type I–III evidence is **rat** (Sprague-Dawley, adult,
acute slice) — Hazra et al. 2011, Dabrowska et al. 2013, Daniel et al. 2019. Every
marker statement in the definition is therefore explicitly rat-scoped. The Type I–III
scheme has **not** been shown to transfer cleanly to mouse: Silberman et al. note that
mouse BNST CRF neurons fall into more categories than previously described, possibly
reflecting rat/mouse physiological differences, recording site, or recording
conditions. No taxon constraint is proposed, but editors should be aware that the
supporting evidence does not yet license a mouse assertion.

**4. Assay caveat on the ion-channel calls — this is a targeted-assay signature, not a
scRNA-seq marker panel.** The channel-subunit profile comes from single-cell RT-PCR
presence/absence calls on cytoplasm harvested after whole-cell recording, at high cycle
thresholds (some near the detection limit, e.g. Kcnd3 at Ct 39). Those thresholds are
assay-specific and would not transfer directly to droplet scRNA-seq, where low-abundance
channel transcripts are routinely undetected. The discriminative power of the profile is
nonetheless real and unbiased: hierarchical clustering on 16 channel-subunit transcripts,
followed by discriminant function analysis, recovered groups that correlated with the
pre-existing electrophysiological Type I–III classification, and the Type III cluster
contained Type III cells exclusively.

> Similarly, another subgroup of neurons (n = 9) was characterized by their expression of transcripts for only the HCN4 subunit, together with Ca v 3.3, K v 4.2, and Kir2.1, 2.2 and 2.3 subunits, and these neurons corresponded to 9/11 of the Type III neurons recorded. <!-- quote_key: 8615463_6a67aab1 -->
<!-- quote_key: 8615463_6a67aab1 -->

**5. Directionality of the individual channel calls** (all rat, single-cell RT-PCR,
PMID:21310239), for editors weighing which to axiomatise:

| Subunit (gene) | Type III | Type II | Type I | In axioms? |
|---|---|---|---|---|
| Cav3.3 (`Cacna1i`) | 100% (11/11) | 47% | 17% | **yes** |
| Cav3.1 (`Cacna1g`) | absent | 91% | absent | no (negative) |
| HCN4 (`Hcn4`) | only HCN subunit present; 9/11 cluster | — | — | candidate, curator decision |
| Kv4.2 (`Kcnd2`) | present in cluster profile | — | — | no (<100%) |
| Kir2.2 (`Kcnj12`) | 64% | 20% | 0% | no (<100%) |
| Kir2.3 (`Kcnj4`) | 72% | 62% | 17% | no (<100%) |
| Kv1.4 (`Kcna4`) | absent | 6% | absent | no (negative) |
| 5-HT7 (`Htr7`) | absent | present | present | no (negative) |
| Oxtr | 95% (18/19) | — | — | **yes** |
| Oxt | 0% (0/19) | — | — | no — see point 6 |

> Type I-III neurons also showed distinct distribution patterns for the I T channel subunits. Hence, Ca v 3.3 mRNA was expressed in 100% of Type III neurons, and 47% of Type II neurons, whereas only 17% of Type I neurons expressed this subunit. Transcripts for Ca v 3.1 were expressed in 91% of Type II neurons, but were not expressed in either Type I or III neurons. <!-- quote_key: 8615463_a14b307e -->

> Hence, Kir2.1 expression was highest (83%) in Type I neurons compared to other two subtypes (29% in Type II, and 45% in Type III). Conversely, the expression of Kir2.2 and Kir2.3 was highest in Type III neurons (64% and 72%) compared to Type II (20%, and 62%) and Type I neurons (0%, and 17%), respectively. <!-- quote_key: 8615463_bc844471 -->
<!-- quote_key: 8615463_bc844471 -->

Kir2.1 (`Kcnj2`, 45% in Type III) is quoted above for completeness but is not asserted
as a marker on the KB node and is not used in the definition. Kv3.4 (`Kcnc4`, 9% of
Type III) is likewise not asserted.

**6. Why Oxt-absence is NOT axiomatised.** Oxt-negativity (0/19) is genuine, but its
evidential role is the contrast with PVN parvocellular CRF neurons (83% Oxt+), not
discrimination among BNST neighbours — no BNST population is reported Oxt+ anywhere in
this corpus. It therefore does not function as a differentia against prospective sibling
terms under the same parent, and `lacks_plasma_membrane_part` would in any case be the
wrong construct for a secreted peptide. Oxtr-positivity is used as the marker differentia
instead, and the PVN Oxt contrast is carried in prose only (point 1 above).

**7. Crh level in this class is state-dependent, not a fixed binary.** Daniel et al.
2019 showed that Type III alone among the three BNSTALG classes increases Crf mRNA — and
decreases Ptpn5 mRNA — after chronic social stress:

> Additionally, only the Type III neurons exhibited an increase in Crf mRNA and a decrease in striatal-enriched protein tyrosine phosphatase (Ptpn5) mRNA after CSS. <!-- quote_key: 76666373_ccffc91d -->
<!-- quote_key: 76666373_ccffc91d -->

This is a strong argument that the class is a real, stress-responsive unit, but it also
means a fixed Crh expression threshold will misclassify cells depending on the animal's
stress history. The `expresses some Crh` inheritance from CL:4072021 should be read as
"capable of expressing", consistent with normal CL practice.

**8. No morphology evidence.** The classification is physiological and molecular only;
no morphological data are reported for this population in any of the supporting papers.
No morphology axiom or PATO characteristic is proposed, and none should be inferred.

**9. Abundance.** Type III accounted for 21% of the sampled BNSTALG population (Type I
11%, Type II 66%) in rat acute slices (PMID:21310239). This is recording-sample
abundance, not a stereological estimate.

Proposed logical axioms:

- subClassOf 'corticotropin-releasing neuron' (CL:4072021) — parent; asserted as BROAD in the KB
- subClassOf 'GABAergic neuron' (CL:0000617) — all BNSTALG neurons tested expressed Gad1/GAD67 and none expressed Slc17a6/7/8 (quote_key 4940077_5b783374, PMID:24009552)
- subClassOf 'capable of' (RO:0002215) some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534) — the relations-guide pattern for recording neurotransmitter; same evidence as above. Editors may prefer this in place of the direct CL:0000617 assertion, since it autoclassifies.
- subClassOf 'has soma location' (RO:0002100) some 'anterior division of bed nuclei of stria terminalis' (UBERON:0011173) — quote_key 8615463_e974a9fd (PMID:21310239); see anatomy justification above
- subClassOf 'expresses' (RO:0002292) some 'voltage-dependent T-type calcium channel subunit alpha-1I' (PR:000001973) — Cav3.3 in 100% of Type III (11/11); quote_key 8615463_a14b307e (PMID:21310239)
- subClassOf 'expresses' (RO:0002292) some 'oxytocin receptor' (PR:000001635) — 18/19 (95%) Oxtr+; quote_key 4940077_383bf7ef (PMID:24009552)

Candidate axiom, offered for curator decision rather than asserted:

- subClassOf 'expresses' (RO:0002292) some 'potassium/sodium hyperpolarization-activated cyclic nucleotide-gated channel 4' (PR:000000708) — Hcn4 is the only HCN subunit in the Type III cluster profile and is arguably the most characteristic single feature (it pairs with the "little discernible Ih" phenotype), but the cluster covered 9/11 Type III cells, so `expresses some` is a slight over-claim. quote_key 8615463_6a67aab1 (PMID:21310239).

Deliberately omitted axioms (recorded so the omission is legible, not an oversight):

- Absence of Cacna1g (Cav3.1), Kcna4 (Kv1.4), Htr7 (5-HT7) and Oxt. These are the sharpest discriminators against BNSTALG Type II in particular, but `lacks_plasma_membrane_part` is an EL-profile workaround whose use with general targets can cause reasoning errors, and it is inappropriate for a secreted peptide (Oxt). Recorded here in prose and in the table at point 5 instead.
- Kcnd2, Kcnj12, Kcnj4 — expressed in a majority but not all Type III cells (see point 5); `expresses some` would be false for the remainder.
- Any morphology or PATO characteristic — no morphological data exist (point 8).
- Any electrophysiological PATO characteristic for "little discernible Ih" / "largest IK(IR)" — no suitable PATO term was identified, and the ion-channel expression axioms already carry the mechanistic content.

Key references:

- Hazra et al. 2011 · PMID:21310239 · DOI:10.1016/j.mcn.2011.01.011 — supports: soma location (BNSTov/BNSTju/BNSTal reconstruction), the full ion-channel alpha-subunit profile (Cav3.3+/Cav3.1−/Hcn4+/Kcnd2+/Kcnj12+/Kcnj4+/Kcna4−/Htr7−), the unbiased hierarchical-clustering + DFA validation of the Type I–III scheme, "little discernible Ih", and the 21% sample abundance
- Dabrowska et al. 2013 · PMID:24009552 · DOI:10.3389/fnins.2013.00156 — supports: Crh in ~95% of Type III, Oxtr in 18/19 (95%), Oxt in 0/19, GABAergic phenotype (Gad1+, Slc17a6/7/8−), and the PVN parvocellular CRF contrast (83% Oxt+, 0% Oxtr+)
- Daniel et al. 2019 · PMID:30878403 · DOI:10.1016/j.neuropharm.2019.03.013 — supports: Type III-selective increase in Crf mRNA and decrease in Ptpn5 mRNA after chronic social stress (state dependence of the Crh call)
- Silberman et al. 2013 · PMID:23325234 — supports: the scoping caveat at point 2 — at least four electrophysiologically separable subtypes among identified mouse BNST CRF neurons
- PMID:31451580 — supports: CRF increases inhibitory synaptic input onto type III neurons in naive rat dlBNST (functional context; not used in the definition)
- PMID:23554470 — supports: only type II, not type I or type III, responds directly to bath-applied CRF and NPY (differentia against Type II; not used in the definition)

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/sexually_dimorphic/dlbnst_crf.yaml#bnstalg_type_iii_crf_neuron`.*
*Source facts: `reports/sexually_dimorphic/bnstalg_type_iii_crf_neuron_facts.json`.*

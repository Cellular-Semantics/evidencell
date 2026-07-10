# Basolateral amygdala VIP/calretinin interneuron-selective interneuron — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `/Users/do12/Documents/GitHub/evidencell_too/kb/graphs/medial_temporal_lobe_amygdala/bla_vip_calretinin_interneuron.yaml`*

## Introduction

The basolateral amygdala VIP/calretinin interneuron-selective interneuron is a class of small bipolar and bitufted GABAergic cells that co-express calretinin, cholecystokinin and vasoactive intestinal peptide, and that preferentially innervate other interneurons rather than principal cells [1][2]. It is the numerically dominant GABAergic population of the basolateral amygdala — roughly a third of local inhibitory neurons — and so its transcriptomic placement matters for interpreting any amygdalar interneuron atlas [2].

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | basal amygdaloid nucleus [UBERON:0002887] | [1][2] |
| NT type | GABAergic | [1][2] |
| Defining markers | Vip, Calb2 (calretinin), Cck | [1][2][3][4] |
| Negative markers | Pvalb, Sst | — |
| Neuropeptides | Vip, Cck | [1][2] |
| Cell Ontology | GABAergic interneuron (CL:0011005) | — |

*Note on class composition:* this type is grouped as a single class but is acknowledged as molecularly mixed — cells expressing VIP and/or calretinin are pooled together.

<details>
<summary>Details — source evidence for classical type properties</summary>

**Defining markers / neuropeptides / NT / morphology:**

> The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter (McDonald, 1982)(McDonald, 1985)(McDonald, , 1992a(McDonald, ,b, 1996(McDonald, , 2003(Millhouse et al., 1983)(Fuller et al., 1987)(Carlsen et al., 1988)(McDonald et al., 1993). Dual-labeling immunohistochemical studies in the basolateral amygdala suggest that the CBL contains at least four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide (Kemppainen and Pitkänen, 2000;McDonald and Betette, 2001;Mascagni, 2001, 2002;
> — McDonald et al. 2012, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 11544073_ea8d2bb3 -->

**Population fraction / marker panel:**

> we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
> — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [2] <!-- quote_key: 232283078_d4238834 -->

**Vip marker (transcriptomic context):**

> sparse, but specific expression of Grpr in several GABAergic interneurons, such as Vip-expressing GABA-50 and GABA-51, Pvalb-type GABA-41
> — Hochgerner et al. 2023, Two classes of glutamatergic neurons par · [3] <!-- quote_key: 264517392_039d73c7 -->

**Calb2 / Cck co-expression (primate amygdala):**

> both clusters showed increased expression of genes (Fig. 3B) encoding calretinin (CALB2), cholecystokinin (CCK), corticotropin releasing hormone (CRH), cannabinoid receptor 1 (CNR1)
> — Totty et al. 2024, GABAergic neuron types in the primate amygdala show distributed or subregion specific expression patterns · [4] <!-- quote_key: 273531817_447a3097 -->

</details>

Cell Ontology mapping: GABAergic interneuron [[CL:0011005](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011005)] (BROAD).

## Results

Strong, cohort-specific expression of the defining markers Vip and calretinin (Calb2) points to the Vip Gaba clusters of WMBv1, led by 0630 Vip Gaba_2 [CS20230722_CLUS_0630] (Vip 10.99, cohort-pct 0.960; Calb2 8.64, cohort-pct 0.980; see property comparison table), with its parent supertype 0174 Vip Gaba_2 [CS20230722_SUPT_0174] capturing the broader population. The support is marker-based only — no annotation-transfer evidence anchors any candidate — and soma proximity to the amygdala is weak throughout: the atlas Vip Gaba clusters distribute across isocortex, hippocampal formation and olfactory areas rather than concentrating in the basal amygdaloid nucleus, so the classical type corresponds to several distributed Vip Gaba clusters rather than one.

### 0630 Vip Gaba_2 · 🔴 LOW

*Best-matching cluster; primary candidate.* The two canonical markers of the classical type are strongly and specifically expressed here, giving this cluster the top cohort score of its five-member GABAergic cohort (score 8 vs next-best 7). The call rests on marker expression alone.

**Table 1 — Property comparison**

| Property | Classical | Supertype (0174 Vip Gaba_2) | Best cluster (0630 Vip Gaba_2) | Alignment |
|---|---|---|---|---|
| Soma location | basal amygdaloid nucleus [UBERON:0002887] | Isocortex [MBA:315] / Hippocampal formation [MBA:1089] / Olfactory areas [MBA:698] (rf₁₀₀ 0.052) | Hippocampal formation [MBA:1089] / Cortical subplate [MBA:703] / Entorhinal area [MBA:918] (rf₁₀₀ 0.124) | SUPT: DISCORDANT; CLUS: APPROXIMATE |
| NT type | GABAergic | not asserted | GABA | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Vip expression | defining marker | 10.55 (cohort-pct 0.964) | 10.99 (cohort-pct 0.960) | CONSISTENT |
| Calb2 expression | defining marker | 5.63 (cohort-pct 0.904) | 8.64 (cohort-pct 0.980) | CONSISTENT |
| Cck expression | defining marker | 1.50 (cohort-pct 0.446) | 1.03 (cohort-pct 0.305) | APPROXIMATE |
| Pvalb (negative) | ABSENT | 0.58 (cohort-pct 0.795) | 0.00 (cohort-pct 0.000) | SUPT: DISCORDANT; CLUS: CONSISTENT |
| Sst (negative) | ABSENT | 0.87 (cohort-pct 0.145) | 0.83 (cohort-pct 0.159) | DISCORDANT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 0630 Vip Gaba_2 | Atlas metadata | PARTIAL | Vip 10.99 / Calb2 8.64 cohort-high; region_fraction_100um=0.124 | atlas-internal |

*(2 of 2 sampled child clusters of the supertype — 0630 Vip Gaba_2 and 0628 Vip Gaba_2 — show Vip and Calb2 concordant with the classical type; both carry marginal Sst and 0628 additionally shows detectable Pvalb. Best match: CLUS_0630.)*

**Supporting evidence:**
- Vip is a DEFINING atlas marker on this cluster (10.99, cohort-pct 0.960) and calretinin/Calb2 sits at cohort-pct 0.980 (8.64) — the two markers that name the classical type are both cohort-high on 0630 Vip Gaba_2 [CS20230722_CLUS_0630].
- Parvalbumin, a classical negative marker, is undetectable (0.00), consistent with the interneuron-selective interneuron identity.

**Marker evidence provenance:**
- **Vip / Calb2:** classical assertions rest on immunohistochemical co-localization studies [1][2] plus transcriptomic support [3][4]; both are cohort-specific transcript-level signals on the atlas cluster, so the concordance is genuine rather than nominal.
- **Cck:** a classical defining marker but only marginally detectable here (1.03, cohort-pct 0.305; APPROXIMATE) — the fuller CCK co-expression described classically [1] is better matched by 0656 Vip Gaba_9 [CS20230722_CLUS_0656] (see below). *(note: CCK also marks a separate CCK basket-cell type in the BLA, so partial CCK is expected in a Vip/calretinin-selective cluster.)*
- **Sst:** listed as a negative marker on the classical node without a primary citation; the atlas shows low-but-detectable Sst (0.83), a weak discordance discussed below.

**Concerns:**
- Sst is detectable (0.83) despite being a classical negative marker, though at low cohort specificity (cohort-pct 0.159) — weak counter-evidence.
- Location APPROXIMATE (`region_fraction_100um: 0.124`; boundary scatter into hippocampal formation and cortical subplate — could reflect that Vip/calretinin interneurons are a telencephalon-wide type not concentrated in the amygdala; weak counter-evidence).
- No annotation-transfer evidence supports the mapping — the call is cohort-relative marker expression only.

**What would upgrade confidence:**
- AnnotationTransferEvidence from an amygdala-targeted VIP/calretinin dataset scored against CS20230722 (target F1 ≥ 0.5 at cluster level) — establishing an `at_source_sets` source-annotation→type correspondence is the single largest missing anchor.
- A targeted literature trawl for Sst co-expression within the amygdalar VIP/calretinin population, to decide whether the atlas-side detectable Sst is real heterogeneity or contamination.

### 0174 Vip Gaba_2 · 🔴 LOW

*Parent supertype; broader correspondence.* The amygdalar VIP/calretinin interneuron-selective interneuron corresponds broadly to the Vip Gaba_2 supertype 0174 Vip Gaba_2 [CS20230722_SUPT_0174], of which 0630 Vip Gaba_2 is the best-matching child. Because the population is distributed across many Vip Gaba clusters and no atlas node concentrates in the amygdala, the supportable correspondence at this resolution is broader-than, not one-to-one.

**Supporting evidence:**
- Vip (10.55, cohort-pct 0.964) and Calb2 (5.63, cohort-pct 0.904) are cohort-high across the supertype with child-cluster coverage 1.000, i.e. the marker signal is shared by all sampled children.

**Concerns:**
- Location DISCORDANT: the supertype spans Isocortex [MBA:315], Hippocampal formation [MBA:1089] and Olfactory areas [MBA:698] (`region_fraction_100um: 0.052`; distant from the basal amygdaloid nucleus — stronger counter-evidence; the classical type may be the amygdalar instance of this broader Vip Gaba population rather than the population as a whole).
- Pvalb is detectable at supertype level (0.58, cohort-pct 0.795; DISCORDANT) — this dilutes at the child level (0.00 on 0630 Vip Gaba_2), a signature of within-supertype heterogeneity.
- Sst detectable (0.87; DISCORDANT), as for the child cluster.

**What would upgrade confidence:**
- Supertype-level AnnotationTransferEvidence testing whether the classical type maps broadly across Vip Gaba_2 or resolves to a single child cluster.

### 0656 Vip Gaba_9 · 🔴 LOW

*Alternative cluster with fuller marker co-expression.* This cluster is the only candidate on which all three classical markers are cohort-high simultaneously — Vip (8.69, cohort-pct 0.927), calretinin/Calb2 (8.29, cohort-pct 0.967) and Cck (6.29, cohort-pct 0.815) — matching the full VIP+calretinin+CCK co-expression profile described classically [1] more completely than 0630 Vip Gaba_2, but it sits in a different Vip Gaba supertype (0181 Vip Gaba_9) and shares the same weak region signal.

**Supporting evidence:**
- All three defining markers CONSISTENT and cohort-high on 0656 Vip Gaba_9 [CS20230722_CLUS_0656]; parvalbumin undetectable (0.00).

**Concerns:**
- Sst detectable (0.74; DISCORDANT) at low cohort specificity (cohort-pct 0.113).
- Location APPROXIMATE (`region_fraction_100um: 0.119`; boundary scatter into hippocampal formation and cortical subplate).
- No annotation-transfer evidence; the higher CCK here versus lower CCK on 0630 Vip Gaba_2 leaves open whether these are distinct subpopulations of the mixed classical class.

**What would upgrade confidence:**
- AnnotationTransferEvidence discriminating the Vip/Calb2-dominant (0630) from the Vip/Calb2/Cck-high (0656) cluster against a BLA-targeted source dataset.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0630 Vip Gaba_2 [CS20230722_CLUS_0630]` | `0174 Vip Gaba_2` | 761 | 🔴 LOW | Vip/Calb2 cohort-high; top score | Primary |
| `0174 Vip Gaba_2 [CS20230722_SUPT_0174]` | — | 5710 | 🔴 LOW | Vip/Calb2 shared across children | Supports broader mapping |
| `0656 Vip Gaba_9 [CS20230722_CLUS_0656]` | `0181 Vip Gaba_9` | 192 | 🔴 LOW | Vip/Calb2/Cck all cohort-high | Secondary |
| `0628 Vip Gaba_2 [CS20230722_CLUS_0628]` | `0174 Vip Gaba_2` | 1401 | ⚪ UNCERTAIN | Pvalb+Sst detectable; distant region | Eliminated (Pvalb present) |
| `0634 Vip Gaba_3 [CS20230722_CLUS_0634]` | `0175 Vip Gaba_3` | 1780 | ⚪ UNCERTAIN | Lower Calb2; Sst present | Eliminated (weaker calretinin) |
| `0636 Vip Gaba_4 [CS20230722_CLUS_0636]` | `0176 Vip Gaba_4` | 750 | ⚪ UNCERTAIN | Leads no defining marker | Eliminated (distant region) |
| `0175 Vip Gaba_3 [CS20230722_SUPT_0175]` | — | 7526 | ⚪ UNCERTAIN | Cortex/OLF/HPF spread | Eliminated (distant region) |
| `0179 Vip Gaba_7 [CS20230722_SUPT_0179]` | — | 1083 | ⚪ UNCERTAIN | Hippocampal CA3/CA1 | Eliminated (hippocampal, not amygdala) |
| `0181 Vip Gaba_9 [CS20230722_SUPT_0181]` | — | 1441 | ⚪ UNCERTAIN | Supertype Vip diluted (3.03) | Eliminated (Vip diluted at supertype) |
| `0292 IA Mgp Gaba_3 [CS20230722_SUPT_0292]` | — | 443 | 🔴 REFUTED | Vip absent (0.26); high Sst | Eliminated (wrong type — intercalated Mgp) |

</details>

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The basolateral amygdala VIP/calretinin interneuron-selective interneuron is defined as a GABAergic (`definition_basis`: CLASSICAL_MULTIMODAL) population co-expressing Vip, calretinin (Calb2) and Cck, with somata in the basal amygdaloid nucleus [UBERON:0002887] [1][2], and negative for Pvalb and Sst. Marker and neuropeptide assertions draw on immunohistochemical co-localization studies [1][2] with additional transcriptomic context [3][4].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.** No annotation-transfer runs are attached to this node. The node declares no `at_source_sets` source-annotation→type correspondence, so no MapMyCells transfer was scored; the mapping rests on atlas marker expression and region proximity alone.

**Anti-hallucination.**
> All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

<details>
<summary>Evidence base table</summary>

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge…CLUS_0630 | ATLAS_METADATA | PARTIAL | — |
| edge…SUPT_0174 | ATLAS_METADATA | PARTIAL | — |
| edge…CLUS_0656 | ATLAS_METADATA | PARTIAL | — |
| edge…CLUS_0628 | ATLAS_METADATA | PARTIAL | — |
| edge…CLUS_0634 | ATLAS_METADATA | PARTIAL | — |
| edge…CLUS_0636 | ATLAS_METADATA | PARTIAL | — |
| edge…SUPT_0175 | ATLAS_METADATA | PARTIAL | — |
| edge…SUPT_0179 | ATLAS_METADATA | PARTIAL | — |
| edge…SUPT_0181 | ATLAS_METADATA | PARTIAL | — |
| edge…SUPT_0292 | ATLAS_METADATA | PARTIAL | — |

</details>

*Generated by evidencell `db6b114` at 2026-07-09T18:13:44+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/bla_vip_calretinin_interneuron.yaml](kb/graphs/medial_temporal_lobe_amygdala/bla_vip_calretinin_interneuron.yaml).*

</details>

## Discussion

**Primary mapping:** Basolateral amygdala VIP/calretinin interneuron-selective interneuron → 0630 Vip Gaba_2 [CS20230722_CLUS_0630] at LOW confidence. Key support: cohort-high Vip and calretinin (Calb2) atlas expression. Key caveats: no annotation-transfer anchor (AMBIGUOUS_MAPPING) and a population distributed across several Vip Gaba clusters with weak amygdalar soma proximity (DISTRIBUTED_ACROSS_CLUSTERS). The broader correspondence is recorded on the parent supertype 0174 Vip Gaba_2 [CS20230722_SUPT_0174]; a fuller VIP+calretinin+CCK profile is matched by 0656 Vip Gaba_9 [CS20230722_CLUS_0656].

The Cell Ontology has no specific term for this population; GABAergic interneuron [[CL:0011005](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011005)] is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

No annotation-transfer evidence exists on any edge because this node declares no source-annotation→type correspondence.

- **Establish annotation-transfer support.** Identify an external amygdala-targeted VIP/calretinin dataset, declare an `at_source_sets` correspondence for this classical type, and run annotation transfer against CS20230722 (target F1 ≥ 0.5 at cluster level; F1 ≥ 0.7 at supertype). Expected output: `AnnotationTransferEvidence` attached to the 0630 Vip Gaba_2 and 0174 Vip Gaba_2 edges. Resolves open questions 1 and 2. *(note: no external dataset accession is currently declared on the node — the first step is an evidence-extraction gap, i.e. identifying a suitable source dataset, not re-running an existing punt.)*
- **Targeted literature trawl for Sst co-expression** within the amygdalar VIP/calretinin population, to resolve whether the atlas-side detectable Sst (~0.8–1.2 across candidates) is genuine heterogeneity or contamination. Expected output: LiteratureEvidence. Resolves the recurring Sst discordance.

### Open questions

1. Does the amygdalar VIP/calretinin interneuron-selective interneuron correspond to a single Vip Gaba cluster or distribute across several (e.g. 0630 Vip Gaba_2 vs 0656 Vip Gaba_9)? *(applies across the cluster edges)*
2. Is the classical class better represented at supertype (Vip Gaba_2) or cluster resolution, given no atlas node concentrates in the amygdala?
3. Do the Vip/Calb2-high (0630) and Vip/Calb2/Cck-high (0656) clusters represent distinct subpopulations of the molecularly mixed classical class?

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | McDonald et al. 2012 | [22837739](https://pubmed.ncbi.nlm.nih.gov/22837739) | soma location, markers, morphology, NT, neuropeptides |
| [2] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051) | soma location, markers, population fraction |
| [3] | Hochgerner et al. 2023 | [37884748](https://pubmed.ncbi.nlm.nih.gov/37884748) | Vip marker |
| [4] | Totty et al. 2024 | [39463931](https://pubmed.ncbi.nlm.nih.gov/39463931) | Calb2 marker |

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_CLUS_0630 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.4
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Vip (10.99, cohort-pct 0.960) and calretinin/Calb2 (8.64,
    cohort-pct 0.980) are strongly and specifically expressed on
    CS20230722_CLUS_0630, matching the two defining markers of the classical
    type; the cluster narrowly led its 5-member GABAergic cohort (Stage A score
    8 vs next-best 7). Support is marker-based only: no annotation-transfer
    evidence anchors the call, soma proximity to the basal amygdaloid nucleus is
    weak (region_fraction_100um: 0.124, boundary scatter into hippocampal
    formation and cortical subplate), Cck is only marginally detectable (1.03),
    and Sst is present above threshold (0.83) at low cohort-pct (0.159).
  reconciliation_note: >
    Paired with the broader supertype mapping on 0174 Vip Gaba_2; an alternative
    cluster with fuller Cck co-expression is 0656 Vip Gaba_9.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Sst is detectable (0.83) on CS20230722_CLUS_0630 despite being a
        classical negative marker, though at low cohort specificity (cohort-pct
        0.159); no annotation-transfer evidence supports the mapping.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        The classical VIP/calretinin population maps across several Vip Gaba
        clusters rather than concentrating in CS20230722_CLUS_0630; soma
        proximity to the basal amygdaloid nucleus is weak (region_fraction_100um:
        0.124).
  proposed_experiments:
    - >
      Establish a source-annotation to classical-type correspondence (an
      at_source_sets entry) for the amygdalar VIP/calretinin interneuron and run
      annotation transfer against CS20230722, attaching AnnotationTransferEvidence
      to this edge — currently no annotation-transfer support exists.
    - >
      Trawl the literature for Sst co-expression within the amygdalar
      VIP/calretinin population to determine whether the atlas-side detectable
      Sst is genuine heterogeneity or contamination.
  unresolved_questions:
    - >
      Does the amygdalar VIP/calretinin interneuron-selective interneuron
      correspond to a single Vip Gaba cluster or distribute across several (e.g.
      0630 vs 0656)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_SUPT_0174 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] The amygdalar VIP/calretinin interneuron corresponds broadly to
    the Vip Gaba_2 supertype CS20230722_SUPT_0174, whose children carry the
    defining Vip (10.55, cohort-pct 0.964) and Calb2 (5.63, cohort-pct 0.904)
    signal with child-cluster coverage 1.000. The supertype spans isocortex,
    hippocampal formation and olfactory areas rather than concentrating in the
    amygdala (region_fraction_100um: 0.052), and detectable Pvalb (0.58) and Sst
    (0.87) at supertype level reflect molecular heterogeneity; one classical type
    maps to several distributed Vip Gaba clusters, so the correspondence is
    broader-than and not 1:1.
  reconciliation_note: >
    Paired with the child-cluster mapping to 0630 Vip Gaba_2, the best-matching
    leaf within this supertype.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Location is discordant — CS20230722_SUPT_0174 spans isocortex,
        hippocampal formation and olfactory areas (region_fraction_100um: 0.052)
        rather than the basal amygdaloid nucleus; detectable Pvalb (0.58) and Sst
        (0.87) reflect molecular heterogeneity.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        No annotation-transfer evidence anchors the supertype; the mapping rests
        on cohort-relative marker expression only.
  proposed_experiments:
    - >
      Attach annotation-transfer evidence by declaring a source correspondence
      for the amygdalar VIP/calretinin interneuron and scoring it against the Vip
      Gaba supertypes of CS20230722; a supertype-level transfer would test
      whether the classical type maps broadly across Vip Gaba_2 or resolves to a
      single child.
  unresolved_questions:
    - >
      Is the classical VIP/calretinin class better represented at supertype (Vip
      Gaba_2) or cluster resolution, given no atlas node concentrates in the
      amygdala?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_CLUS_0656 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:WEAKEST] CS20230722_CLUS_0656 is the only candidate on which all three
    defining markers are cohort-high simultaneously — Vip (8.69, cohort-pct
    0.927), Calb2 (8.29, cohort-pct 0.967) and Cck (6.29, cohort-pct 0.815) —
    matching the full VIP+calretinin+CCK co-expression profile of the classical
    type more completely than 0630 Vip Gaba_2. It sits in a separate Vip Gaba
    supertype and shares the weak region signal (region_fraction_100um: 0.119),
    with Sst detectable (0.74); support is marker-based only.
  reconciliation_note: >
    Alternative to the 0630 Vip Gaba_2 mapping, with fuller Cck co-expression but
    in a separate Vip Gaba supertype.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Sst detectable (0.74) on CS20230722_CLUS_0656 despite being a classical
        negative marker; soma proximity to the basal amygdaloid nucleus is weak
        (region_fraction_100um: 0.119) and no annotation-transfer evidence
        supports the mapping.
  proposed_experiments:
    - >
      Run annotation transfer from a BLA-targeted VIP/calretinin dataset against
      CS20230722 to test whether the full Vip+Calb2+Cck profile of this cluster
      corresponds to the classical type better than the Vip/Calb2-dominant
      0630 Vip Gaba_2.
  unresolved_questions:
    - >
      Do the Vip/Calb2-high (0630) and Vip/Calb2/Cck-high (0656) clusters
      represent distinct subpopulations of the molecularly mixed classical class?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_CLUS_0628 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0628 matches Vip (11.11) and Calb2 (8.12) but
    carries detectable Pvalb (0.27) and Sst (0.87) and its soma distribute to
    hippocampal, olfactory and isocortical territory (region_fraction_100um:
    0.096, location discordant) — weaker than the sibling 0630 Vip Gaba_2.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_CLUS_0634 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_CLUS_0634 co-expresses Vip, Calb2 and Cck but with
    lower calretinin specificity (Calb2 3.41) and detectable Sst (1.15); region
    proximity to the basal amygdaloid nucleus is weak (region_fraction_100um:
    0.109).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_CLUS_0636 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_CLUS_0636 shows the Vip/Calb2/Cck profile but does not
    lead on any defining marker and its soma sit in cortical subplate and
    olfactory areas (region_fraction_100um: 0.142); covered by the retained Vip
    Gaba mappings.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_SUPT_0175 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0175 spans isocortex, olfactory and hippocampal
    territory (region_fraction_100um: 0.065) with lower Calb2 specificity (4.19);
    its child 0634 Vip Gaba_3 is the relevant leaf but neither concentrates in
    the amygdala.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_SUPT_0179 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0179 localizes to hippocampal formation and
    fields CA3/CA1 (region_fraction_100um: 0.016), far from the basal amygdaloid
    nucleus, despite carrying Vip (6.82); eliminated on location.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_SUPT_0181 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] At supertype level CS20230722_SUPT_0181 shows diluted Vip (3.03)
    driven by a minority of children, and soma sit outside the amygdala
    (region_fraction_100um: 0.095); the marker-rich child 0656 Vip Gaba_9 carries
    the signal instead.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_CS20230722_SUPT_0292 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Vip is essentially absent on CS20230722_SUPT_0292 (0.26), and this
    intercalated-type Mgp Gaba_3 supertype shows high Sst (3.14) — inconsistent
    with a VIP/calretinin interneuron-selective interneuron.
```
<!-- verdict-block-end -->

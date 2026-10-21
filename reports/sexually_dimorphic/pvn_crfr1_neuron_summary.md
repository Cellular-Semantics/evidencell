# PVN corticotropin-releasing factor receptor 1 (CRFR1) neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

PVN CRFR1 neurons are paraventricular hypothalamic cells defined by expression of the corticotropin-releasing factor receptor 1 (Crhr1). They show a male-biased sexual dimorphism that emerges around puberty, persists into old age, and is sensitive to adult gonadectomy in males but not females; the population co-expresses estrogen receptor alpha (moderate) and androgen receptor (high), consistent with regulation by circulating gonadal steroids [1]. Because Crhr1 marks the postsynaptic recipient of CRH input rather than CRH-producing neurons, the population is biologically distinct from the canonical "corticotropin-releasing neuron" defined by CRH secretion, and its placement against the WMBv1 hypothalamic taxonomy is an open question.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | [1] |
| Markers | Crhr1; Esr1 (moderate co-expression); Ar (high co-expression) | [1] |
| Sex bias | Male-biased (males > females); emerges at puberty; reduced by adult gonadectomy in males | [1] |
| Cell Ontology mapping | corticotropin-releasing neuron [CL:4072021] (RELATED) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location, sexual dimorphism, marker co-expression:** CRFR1 reporter mouse line; immunohistochemistry against the reporter, ERα, and androgen receptor; gonadectomy and restraint-stress activation by phosphorylated CREB [1].
  > Using a corticotropin-releasing factor receptor 1 (CRFR1) reporter mouse line, we report a sexually dimorphic distribution of CRFR1 expressing cells within the paraventricular hypothalamus (PVN; males > females). … CRFR1 cells show moderate co-expression with estrogen receptor alpha (ERα) and high co-expression with androgen receptor, indicating potential mechanisms through which circulating gonadal hormones might regulate CRFR1 expression and function.
  > — Rosinger et al. 2019, Introduction · [1] <!-- quote_key: 143424909_2b990710 -->
</details>

### Cell Ontology mapping

Cell Ontology mapping: corticotropin-releasing neuron [[CL:4072021](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4072021)] (RELATED).

The closest existing CL term (CL:4072021) defines neurons by CRH **secretion**, whereas this population is defined by CRFR1 **receptor** expression — biologically distinct, since CRFR1+ PVN cells receive CRH input rather than producing it. No exact CL term currently exists and this type is a candidate for a new CL contribution.

---

## Results

The strongest available placement is to the PVN-resident glutamatergic supertype 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585], driven by atlas-side concordance of soma location (MBA:38) and of the steroid-hormone-receptor profile (Esr1, Ar) reported by Rosinger 2019 [1]; this remains a LOW-confidence call because Crhr1 itself is not in the atlas precomputed expression panel and the supertype-level Crhr1 mean (0.84) implies that CRFR1+ cells are a minority subset of the supertype. No annotation transfer evidence is available, so resolution of which child cluster within 0585 (or among its sister supertypes 0586/0587/0589) best represents the dimorphic CRFR1+ population is deferred to a Crhr1-targeted transcriptomic or post-hoc immunostained sequencing experiment.

### Property alignment + Evidence support — 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | 175/645 cells in PVN, additional 74 in adjacent anterior hypothalamic nucleus | CLUS_2366: 17/64 cells in PVN, region_fraction_100um=0.810 | CONSISTENT |
| NT type | not asserted | not asserted (Glut at cluster level) | Glut | NOT_ASSESSED |
| Crhr1 expression | defining marker | mean 0.84 (atlas-internal; minority subset) | not available | NOT_ASSESSED |
| Esr1 expression | defining marker (moderate) | mean 3.65 (DEFINING_SCOPED atlas marker) | not available | NOT_ASSESSED |
| Ar expression | defining marker (high) | mean 4.95 | not available | NOT_ASSESSED |
| Sex ratio | male-biased | not available | not available | NOT_ASSESSED |

*(Atlas Crhr1 mean of 0.84 across SUPT_0585 was reported by Stage A discovery — see Supporting evidence below. Per-child-cluster Crhr1, Esr1, and Ar means were not extracted into property_comparisons, so cluster-level alignment is not resolvable from the current facts.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + location | Atlas metadata | PARTIAL | Esr1=3.65 (DEFINING_SCOPED), Ar=4.95, Crh=2.5, Crhr1=0.84; 175/645 PVN cells | atlas-internal |

**Supporting evidence**

- **Atlas metadata (atlas-internal):** SUPT_0585 has Paraventricular hypothalamic nucleus [MBA:38] as primary painted location (175 of 645 cells, region_fraction_100um=0.665). It is the highest-ranked rank-1 candidate within the PVN region cohort. The steroid-receptor profile reported by Rosinger 2019 — moderate Esr1, high Ar — aligns with atlas-internal precomputed means Esr1=3.65 (also a DEFINING_SCOPED atlas marker on this supertype) and Ar=4.95. Crh=2.5 is consistent with the PVN neuroendocrine identity of this supertype.

**Marker evidence provenance**

- **Crhr1.** Established as the defining marker by Rosinger 2019 [1] using a Crhr1 reporter mouse line, with morphological localization to PVN and quantitative cell counts by sex. Single-study evidence at protein level (via the reporter). Crhr1 is absent from the Stage A expression_detail and from the precomputed_expression block on the candidate supertype, so transcript-level cross-check is not currently possible. Atlas-internal Crhr1 mean of 0.84 on SUPT_0585 indicates Crhr1+ cells are a minority of the supertype — consistent with a receptor-defined subpopulation embedded within a broader PVN glutamatergic supertype, but not direct concordance.
- **Esr1.** Reported by Rosinger 2019 [1] as moderately co-expressed with the Crhr1 reporter via immunohistochemistry — protein-level evidence on the morphologically confirmed PVN CRFR1+ population. Atlas-side Esr1 mean=3.65 on SUPT_0585 (DEFINING_SCOPED) is broadly consistent, but does not establish that the Esr1-high cells within SUPT_0585 are the same subset as the Crhr1+ cells.
- **Ar.** Reported by Rosinger 2019 [1] as highly co-expressed at protein level (immunohistochemistry on reporter-positive cells). Atlas-side Ar mean=4.95 is consistent. As with Esr1, supertype-level concordance does not resolve whether the Crhr1+ subset specifically carries the high Ar signal.

**Concerns**

- **Single primary source.** All marker, location, and dimorphism claims rest on Rosinger 2019 [1]. Caveat `SINGLE_DATASET` on the edge caps achievable confidence at MODERATE pending replication; in the absence of any transcriptomic confirmation it is currently LOW.
- **Subset embedding.** Atlas Crhr1 mean of 0.84 across SUPT_0585 implies CRFR1+ cells are a small fraction of this supertype. The mapping is therefore one-to-subset rather than one-to-one with the supertype as a whole.
- **Sister supertype ambiguity.** The unresolved question carried on the edge ("Is SUPT_0589 a better or co-equal mapping target?") notes that the rank-0 candidate cluster CLUS_2382 (parent SUPT_0589) carries a male-biased sex ratio of 2.7, consistent with the dimorphism reported by Rosinger 2019. CLUS_2382 / SUPT_0589 do not currently appear as edges on this node in the graph; they should be emitted at both ranks before any further mapping pass.
- **Sex-ratio not assessed at supertype level.** Male/female ratios are only computed at cluster level (rank 0), so the supertype-level evidence cannot directly confirm the male-bias signature.

**What would upgrade confidence**

- A transcriptomic experiment targeting Crhr1+ PVN cells (FACS-sorted from a Crhr1 reporter line or post-hoc immunostained after sequencing), with cluster-level annotation transfer to WMBv1, would convert the present location-and-steroid-receptor alignment into direct cell-identity evidence (target: F1 ≥ 0.7 at supertype, F1 ≥ 0.5 at cluster). Expected output: AnnotationTransferEvidence on the edge.
- Per-child-cluster precomputed expression of Crhr1, Esr1, and Ar from the WMBv1 reference store, and per-cluster male/female ratio, would identify the best-matching child cluster within SUPT_0585 and discriminate it from SUPT_0586/0587/0589. Expected output: refreshed property_comparisons with cluster-level node_b_values.
- A second primary literature source (replication of the PVN CRFR1 dimorphism, ideally via transcriptomic profiling) would lift the SINGLE_DATASET cap. Expected output: additional LiteratureEvidence on the classical node.

### Property alignment + Evidence support — 2366 PVH-SO-PVa Otp Glut_1 [CS20230722_CLUS_2366] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Cluster (this row) | Alignment |
|---|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | 17/64 cells in PVN; an additional 15 in PVN descending division; region_fraction_100um=0.810 | CONSISTENT |
| NT type | not asserted | Glut | NOT_ASSESSED |
| Crhr1 expression | defining marker | no atlas expression data | NOT_ASSESSED |
| Esr1 expression | defining marker | no atlas expression data | NOT_ASSESSED |
| Ar expression | defining marker | no atlas expression data | NOT_ASSESSED |
| Sex ratio | male-biased | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas location | Atlas metadata | PARTIAL | region_fraction_100um=0.810; 17/64 cells in PVN | atlas-internal |

**Supporting evidence**

- **Atlas metadata (atlas-internal):** CLUS_2366 is the highest-scoring rank-0 (cluster) candidate within the MBA:38 cohort, with the tightest PVN proximity (region_fraction_100um=0.810) of any candidate cluster within SUPT_0585's children that surfaced. As a child of the primary supertype it is the natural cluster-level entry point.

**Concerns**

- **No marker evidence at cluster level.** Crhr1, Esr1, and Ar are all absent from the cluster's atlas expression panel; the cluster-level call rests entirely on location and on parent-supertype steroid-receptor concordance.
- **Small absolute cell count.** n=64 cells at this cluster reduces statistical power for any per-cluster sex-ratio or marker assessment.
- **No direct evidence that CLUS_2366 captures the male-biased CRFR1+ subset rather than another fraction of SUPT_0585.** The supertype-internal heterogeneity flagged by the parent edge (CRFR1+ as a minority subset) cannot be resolved from existing facts.

**What would upgrade confidence**

- Per-cluster precomputed Crhr1, Esr1, Ar means and per-cluster male/female ratio for all children of SUPT_0585 (and of sister supertypes 0586/0587/0589), to identify which child cluster carries both the steroid-receptor signature and the male bias.
- Annotation transfer from a Crhr1+ PVN sorted/captured dataset against WMBv1 at cluster level (target: F1 ≥ 0.5 with CLUS_2366 as the best cluster).

### Property alignment + Evidence support — 0587 PVH-SO-PVa Otp Glut_3 [CS20230722_SUPT_0587] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Alignment |
|---|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | 472/2093 cells in PVN, 139 in PVN descending division; region_fraction_100um=0.975 | CONSISTENT |
| NT type | not asserted | not asserted (atlas Glut at lower levels) | NOT_ASSESSED |
| Crhr1 / Esr1 / Ar expression | defining markers | no atlas expression data on this edge | NOT_ASSESSED |
| Sex ratio | male-biased | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas location | Atlas metadata | PARTIAL | region_fraction_100um=0.975; 472/2093 PVN cells | atlas-internal |

**Supporting evidence**

- **Atlas metadata (atlas-internal):** SUPT_0587 carries the cleanest PVN spatial fingerprint of any candidate (region_fraction_100um=0.975), with the largest absolute count of PVN-located cells. It is a sister supertype to the primary candidate SUPT_0585 within the broader PVH-SO-PVa Otp Glut subclass and therefore plausibly carries part of the CRFR1+ population.

**Concerns**

- **No steroid-receptor concordance carried forward.** Unlike SUPT_0585, this edge does not record atlas-side Esr1 / Ar / Crh expression values, so the receptor-profile bridge from Rosinger 2019 [1] to atlas data is not available here. Without that bridge, the candidate is supported by location alone.
- **The cell type is a receptor-defined subset, not a region.** Higher PVN spatial enrichment alone does not establish identity with the Crhr1+ dimorphic population; the SUPT_0585 candidate's stronger steroid-receptor signature is currently the better biological bridge.

**What would upgrade confidence**

- Atlas-side Crhr1, Esr1, Ar means and sex ratio for SUPT_0587 and its child clusters, comparable to the data already available on SUPT_0585. If Esr1 and Ar are also elevated on SUPT_0587, this candidate would rise to co-equal status with SUPT_0585.
- Annotation transfer from a Crhr1+ PVN dataset; if cells distribute across both SUPT_0585 and SUPT_0587, that would support a one-to-many broadMatch onto the PVH-SO-PVa Otp Glut subclass rather than to either supertype alone.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 target | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] | — | 645 | 🔴 LOW | PVN location; Esr1=3.65, Ar=4.95, Crh=2.5 (atlas) | Primary |
| 2366 PVH-SO-PVa Otp Glut_1 [CS20230722_CLUS_2366] | 0585 PVH-SO-PVa Otp Glut_1 | 64 | 🔴 LOW | Best child of SUPT_0585; PVN region_fraction_100um=0.810 | Secondary (best child within primary) |
| 0587 PVH-SO-PVa Otp Glut_3 [CS20230722_SUPT_0587] | — | 2093 | 🔴 LOW | Highest PVN spatial enrichment (0.975); no marker bridge | Co-equal location candidate |
| 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] (duplicate edge) | — | 645 | ⚪ UNCERTAIN | Impoverished duplicate of primary edge | Eliminated (legacy/fresh-emit ID collision; merge upstream) |
| 0586 PVH-SO-PVa Otp Glut_2 [CS20230722_SUPT_0586] | — | 744 | ⚪ UNCERTAIN | PVN location only; no marker bridge | Eliminated (no steroid-receptor evidence) |
| 1549 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1549] | 0423 BST-MPN Six3 Nrgn Gaba_4 | 218 | ⚪ UNCERTAIN | GABAergic; primarily BST/medial preoptic | Eliminated (wrong subclass; GABA not glutamatergic) |
| 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] | 0423 BST-MPN Six3 Nrgn Gaba_4 | 215 | ⚪ UNCERTAIN | GABAergic; primarily medial preoptic | Eliminated (wrong subclass) |
| 1561 BST-MPN Six3 Nrgn Gaba_6 [CS20230722_CLUS_1561] | 0425 BST-MPN Six3 Nrgn Gaba_6 | 282 | ⚪ UNCERTAIN | GABAergic; weak PVN proximity (0.378) | Eliminated (wrong subclass; weak location) |
| 1563 BST-MPN Six3 Nrgn Gaba_6 [CS20230722_CLUS_1563] | 0425 BST-MPN Six3 Nrgn Gaba_6 | 157 | ⚪ UNCERTAIN | GABAergic; very weak PVN proximity (0.111) | Eliminated (wrong subclass; distant region) |
| 0414 PVR Six3 Sox3 Gaba_4 [CS20230722_SUPT_0414] | — | 388 | 🔴 REFUTED | DISCORDANT location; striatum/pallidum dominant | Eliminated (distant region) |
| 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | — | 933 | 🔴 REFUTED | DISCORDANT location; periventricular preoptic, MPN | Eliminated (preoptic, not PVN) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** PVN CRFR1 neurons are defined by Crhr1 receptor expression in the paraventricular hypothalamic nucleus [MBA:38], with co-expression of Esr1 (moderate) and Ar (high), and a male-biased sex ratio that emerges at puberty and is androgen-sensitive in adulthood (`definition_basis: CLASSICAL_NEUROCHEMICAL`) [1].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against MBA:38, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:14:07+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_pvn_crfr1_neuron_to_cs20230722_supt_0585 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_CLUS_2366 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_CLUS_1549 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_CLUS_1550 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_CLUS_1561 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_CLUS_1563 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0585 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0587 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0586 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0414 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0486 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** PVN corticotropin-releasing factor receptor 1 (CRFR1) neuron → 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] at LOW confidence. Key support: PVN soma location alignment plus atlas-internal concordance of Esr1 (3.65, DEFINING_SCOPED) and Ar (4.95) with the steroid-receptor profile reported by Rosinger 2019 [1]. Key caveats: SINGLE_DATASET (the classical type rests entirely on one primary source), and AMBIGUOUS_MAPPING (Crhr1 mean of 0.84 on the supertype indicates CRFR1+ cells are a minority subset, and sister supertype SUPT_0589 — not currently edged on this node — carries a male-biased child cluster that should be assessed in parallel).

corticotropin-releasing neuron [[CL:4072021](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4072021)] is a related but non-identical Cell Ontology term. CL:4072021 defines neurons by CRH **secretion**, whereas the PVN CRFR1 node is defined by CRFR1 **receptor** expression — these are biologically distinct populations: CRFR1+ PVN neurons receive CRH input, they do not necessarily secrete CRH. The mapping is RELATED only, and no CL term for CRFR1-receptor-expressing neurons currently exists; this type is a candidate for a new CL term.

### Proposed experiments and follow-ups

1. **Targeted transcriptomic profiling of Crhr1+ PVN cells.**
   - **What:** capture Crhr1-expressing PVN cells (Crhr1 reporter line FACS, or post-hoc immunostaining of sequenced PVN cells) and run cluster-level annotation transfer against WMBv1.
   - **Target:** F1 ≥ 0.7 at supertype, F1 ≥ 0.5 at cluster.
   - **Expected output:** AnnotationTransferEvidence on the primary edge.
   - **Resolves:** primary mapping confidence (currently LOW); open questions 1 and 2 below.

2. **Per-child-cluster expression and sex-ratio extraction within candidate supertypes.**
   - **What:** pull precomputed Crhr1, Esr1, Ar means and male/female ratio for every child cluster of SUPT_0585, SUPT_0586, SUPT_0587, and SUPT_0589 from the WMBv1 reference store.
   - **Target:** identify the child cluster with combined high Crhr1, elevated Esr1 + Ar, and male-biased ratio.
   - **Expected output:** refreshed property_comparisons; possible upgrade of CLUS_2366 (or a sibling cluster) to MODERATE.
   - **Resolves:** open question 1.

3. **Emit candidate edges for SUPT_0589 and its child cluster CLUS_2382.**
   - **What:** run `just emit-stage-b` for SUPT_0589 (rank 1) and CLUS_2382 (rank 0). The current evidence (CLUS_2382 male/female ratio 2.7) suggests SUPT_0589 is a co-equal target for the male-biased CRFR1+ population but is not currently edged on this node.
   - **Expected output:** two new MappingEdge entries, then re-run mapping assessment.
   - **Resolves:** open question 2.

4. **Replication of PVN CRFR1 sexual dimorphism.**
   - **What:** secondary literature search (cite-traverse) for independent confirmation of the male-biased Crhr1 distribution in PVN, ideally via a transcriptomic or in-situ hybridization study.
   - **Expected output:** additional LiteratureEvidence on the classical node.
   - **Resolves:** SINGLE_DATASET caveat.

### Open questions

1. Which cluster within the PVH-SO-PVa Otp Glut subclass shows the highest Crhr1 expression combined with male-biased sex ratio?
2. Is SUPT_0589 (parent of male-biased CLUS_2382, ratio 2.7) a better or co-equal mapping target compared to SUPT_0585?
3. Does the CRFR1+ population distribute across multiple sister supertypes within the PVH-SO-PVa Otp Glut subclass (supporting a broadMatch onto the subclass) or concentrate in one supertype (supporting a closeMatch)?
4. Curator follow-up: resolve the legacy/fresh-emit duplicate-ID collision on SUPT_0585 (`edge_pvn_crfr1_neuron_to_cs20230722_supt_0585` carries substantive evidence; `edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0585` is impoverished and should be removed).

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rosinger et al. 2019 — A sexually dimorphic distribution of corticotropin-releasing factor receptor 1 in the paraventricular hypothalamus | [31055007](https://pubmed.ncbi.nlm.nih.gov/31055007/) | soma location, defining markers (Crhr1, Esr1, Ar), male-biased dimorphism, pubertal emergence, gonadectomy effect |

---

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_cs20230722_supt_0585 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] PVN soma location (175/645 cells in MBA:38) and
    atlas-internal Esr1=3.65 (DEFINING_SCOPED) plus Ar=4.95 align with the
    moderate-Esr1 / high-Ar steroid-receptor profile reported by Rosinger
    2019; however, atlas-internal Crhr1 mean of 0.84 indicates the
    defining-marker-positive population is a minority subset of this
    supertype, capping confidence at LOW pending direct transcriptomic
    confirmation.
  reconciliation_note: >
    Paired with secondary candidate CLUS_2366 (best child cluster within
    this supertype by PVN proximity). Sister supertype SUPT_0589 is
    flagged as a co-equal candidate via its male-biased child CLUS_2382
    (ratio 2.7) but is not currently edged on this node; emit and
    re-assess.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        Classical type rests on a single primary source (Rosinger 2019,
        PMID:31055007). Confidence capped at MODERATE pending secondary
        literature validation; currently LOW because no transcriptomic
        confirmation of Crhr1 on the candidate supertype is available.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Atlas-internal Crhr1 mean of 0.84 across SUPT_0585 indicates
        CRFR1+ cells are a minority subset. SUPT_0589 (parent of
        male-biased CLUS_2382, ratio 2.7) is an alternative or
        co-equal mapping target requiring assessment.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Per-child-cluster Crhr1, Esr1, Ar expression and per-cluster
        sex ratio are not in property_comparisons, so the best child
        cluster within SUPT_0585 cannot be resolved from current
        facts.
  proposed_experiments:
    - >
      Crhr1-targeted transcriptomic profiling of PVN cells (Crhr1
      reporter line FACS or post-hoc immunostained sequencing) with
      cluster annotation transfer to WMBv1; target F1 >= 0.7 at
      supertype, F1 >= 0.5 at cluster.
    - >
      Extract per-child-cluster precomputed Crhr1 / Esr1 / Ar means
      and male/female ratio for SUPT_0585, SUPT_0586, SUPT_0587, and
      SUPT_0589 from the WMBv1 reference store; identify the cluster
      with combined receptor signature and male bias.
    - >
      Emit candidate edges for SUPT_0589 (rank 1) and CLUS_2382
      (rank 0) and re-run mapping assessment; CLUS_2382 male/female
      ratio of 2.7 suggests co-equal candidacy with SUPT_0585.
    - >
      Secondary literature search for independent confirmation of
      the PVN CRFR1 male-biased dimorphism, ideally via
      transcriptomic or in-situ hybridization data.
  unresolved_questions:
    - >
      Which cluster within the PVH-SO-PVa Otp Glut subclass shows
      highest Crhr1 expression combined with male-biased sex ratio?
    - >
      Is SUPT_0589 a better or co-equal mapping target compared to
      SUPT_0585?
    - >
      Does the CRFR1+ population concentrate in one supertype or
      distribute across the PVH-SO-PVa Otp Glut subclass (supporting
      broadMatch onto the subclass rather than to a single supertype)?
    - >
      Curator removal of duplicate edge
      edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0585 — legacy/fresh-emit
      ID collision on taxonomy_type CS20230722_SUPT_0585.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_CLUS_2366 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Best child cluster of the primary supertype SUPT_0585 by
    PVN proximity (region_fraction_100um=0.810; 17 of 64 cells in MBA:38);
    selected as the cluster-level entry point for the primary mapping
    pending direct receptor-targeted evidence.
  reconciliation_note: >
    Paired with primary survivor SUPT_0585 (parent supertype, broadMatch
    1:n). Cluster-level call rests on location alone; no atlas
    expression data for Crhr1, Esr1, or Ar on this cluster.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Cluster-level Crhr1 / Esr1 / Ar means and male/female ratio
        are not available in property_comparisons; cannot confirm
        this cluster carries the receptor-defined male-biased subset
        rather than another fraction of SUPT_0585.
    - caveat_type: SINGLE_DATASET
      description: >
        Inherits the SINGLE_DATASET cap of the classical node
        (Rosinger 2019 only).
  proposed_experiments:
    - >
      Per-cluster Crhr1, Esr1, Ar expression and male/female ratio
      pull for all children of SUPT_0585, comparing CLUS_2366 against
      siblings.
    - >
      Crhr1-targeted annotation transfer (see primary edge); confirm
      CLUS_2366 as best cluster at F1 >= 0.5.
  unresolved_questions:
    - >
      Does CLUS_2366 specifically capture the male-biased CRFR1+ subset
      of SUPT_0585, or is the subset distributed across multiple
      sibling clusters?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0587 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:WEAKEST] Highest PVN spatial enrichment (region_fraction_100um
    =0.975; 472/2093 PVN cells) of any candidate, but lacks the
    steroid-receptor expression bridge that supports the primary
    SUPT_0585 call. Co-equal location candidate pending atlas
    Crhr1/Esr1/Ar pull.
  reconciliation_note: >
    Alternative to primary SUPT_0585 within the same PVH-SO-PVa Otp
    Glut subclass. If atlas Esr1/Ar means on SUPT_0587 are also
    elevated, this candidate rises to co-equal; in that case the
    primary edge predicate may need migration to skos:broadMatch
    onto the subclass.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        No atlas-side Esr1/Ar/Crh expression carried on this edge to
        bridge to Rosinger 2019 steroid-receptor profile. Location
        alone is insufficient because the cell type is defined by
        receptor expression, not by region.
    - caveat_type: SINGLE_DATASET
      description: >
        Inherits the SINGLE_DATASET cap of the classical node
        (Rosinger 2019 only).
  proposed_experiments:
    - >
      Pull atlas-internal Crhr1, Esr1, Ar means and child-cluster
      sex ratios for SUPT_0587, comparable to the data on SUPT_0585.
    - >
      Crhr1-targeted annotation transfer (see primary edge); if
      cells distribute across SUPT_0585 and SUPT_0587, migrate
      primary predicate to broadMatch onto the parent subclass.
  unresolved_questions:
    - >
      Is SUPT_0587 a co-equal candidate to SUPT_0585 once atlas
      steroid-receptor expression is assessed?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0585 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Impoverished duplicate of
    edge_pvn_crfr1_neuron_to_cs20230722_supt_0585 (same taxonomy_type
    CS20230722_SUPT_0585; legacy/fresh-emit ID collision). Carries
    only location data; the lowercase-id edge carries the substantive
    Esr1/Ar/Crh atlas evidence and curator-authored caveats. Cut
    pending curator removal.
  caveats:
    - caveat_type: OTHER
      description: >
        Duplicate edge — same taxonomy_type as
        edge_pvn_crfr1_neuron_to_cs20230722_supt_0585. Schedule for
        curator removal.
  unresolved_questions:
    - >
      Curator removal of duplicate edge
      edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0585 (uppercase id)
      in favour of legacy edge with substantive evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0586 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] Sister supertype within the PVH-SO-PVa Otp Glut subclass
    with PVN location (region_fraction_100um=0.610) but no
    steroid-receptor expression evidence carried on this edge; without
    a marker bridge to Rosinger 2019, location alone is insufficient
    for a receptor-defined type.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Same PVH-SO-PVa Otp Glut subclass as primary SUPT_0585; could
        carry part of the CRFR1+ population but no atlas marker
        evidence to support.
  unresolved_questions:
    - >
      Does the CRFR1+ population also include SUPT_0586 (broader
      subclass-level mapping)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_CLUS_1549 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] GABAergic cluster in the BST-MPN Six3 Nrgn Gaba_4
    supertype; wrong subclass for a PVN glutamatergic CRFR1+
    neuroendocrine type. PVN proximity (region_fraction_100um=0.821)
    reflects BST-MPN adjacency rather than identity.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        GABAergic and predominantly BST / medial preoptic; not the
        PVN glutamatergic CRFR1+ population. Survives only on
        location proximity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_CLUS_1550 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.08
  rationale: >
    [tier:CUT] GABAergic cluster in the BST-MPN Six3 Nrgn Gaba_4
    supertype; wrong subclass and primary location is medial preoptic
    rather than PVN (region_fraction_100um=0.521).
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        GABAergic; primary spatial signal in medial preoptic
        nucleus rather than PVN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_CLUS_1561 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] GABAergic cluster in BST-MPN Six3 Nrgn Gaba_6 supertype;
    wrong subclass and weak PVN proximity (region_fraction_100um=0.378
    with strict region_fraction=0.083 — boundary scatter).
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        GABAergic; primary spatial signal in medial preoptic rather
        than PVN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_CLUS_1563 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.03
  rationale: >
    [tier:CUT] GABAergic cluster in BST-MPN Six3 Nrgn Gaba_6 supertype;
    wrong subclass and very weak PVN proximity
    (region_fraction_100um=0.111; striatum among top-3 locations).
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        GABAergic; spatial distribution into striatum is inconsistent
        with the PVN neuroendocrine identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0414 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.02
  rationale: >
    [tier:CUT] DISCORDANT location — primary painted locations are
    striatum and pallidum rather than PVN
    (region_fraction_100um=0.040; strict region_fraction=0.011). Not
    a PVN-resident population.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DISCORDANT location; striatum / pallidum dominant.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pvn_crfr1_neuron_to_CS20230722_SUPT_0486 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.02
  rationale: >
    [tier:CUT] DISCORDANT location — primary painted locations are
    periventricular preoptic and medial preoptic
    (region_fraction_100um=0.020). Not PVN.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DISCORDANT location; preoptic rather than paraventricular.
```
<!-- verdict-block-end -->

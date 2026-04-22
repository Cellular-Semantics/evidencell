# CTX-HPF Taxonomy Reconciliation Report

**Taxonomy:** CS202106160 / CCN202106160 — Mouse Cortex + Hippocampal Formation
**Paper:** Yao et al. 2021 (doi:10.1016/j.cell.2021.04.021)
**Date:** 2026-04-22
**Purpose:** Reconcile three representations of the same taxonomy to assess reliability
of cross-taxonomy annotation transfer (AT) edges between WMBv1 and CTX-HPF.

---

## 1. Sources examined

| Source | Format | Origin | Clusters | Supertypes | Subclasses | Classes |
|--------|--------|--------|----------|------------|------------|---------|
| CAS JSON | CAS v5.3.0 | Allen structure graph (official) | 387 | -- | 42 | 3 |
| Table S3 | XLSX | Paper supplementary (Yao 2021) | 391 (+ 608 empty rows) | 105 | 43 | 4 |
| WMB CTX_* | JSON fields | WMBv1 KG node properties | 29 (hippocampus slice) | 12 | 5 | -- |

**Table S3 ref.cluster_label** column contains labels from an **older clustering version**
(pre-publication), providing a fourth implicit version.

## 2. Accession and ID systems

### Cluster level

| Source | ID format | Example |
|--------|-----------|---------|
| CAS | `CS202106160_<N>` | CS202106160_79 |
| S3 | numeric `cluster_id` | 79 |
| S3 | old CCN accession `cell_type_accession_label` | CCN19103010000079 |
| WMB | `CTX_cluster_id` (numeric) | 79.0 |

**Finding:** All three sources share the same numeric cluster ID space. CAS accession
terminal numbers = S3 cluster_id = WMB CTX_cluster_id. **The numeric IDs are the reliable
join key.**

### Subclass level

| Source | ID format | Example |
|--------|-----------|---------|
| CAS | mixed: `CS202106160_<N>` (22) or `subclass_label:<HASH>` (20) | CS202106160_444 / subclass_label:86d5f48b05 |
| S3 | numeric `subclass_id` (1-43) | 7 |
| WMB | `CTX_subclass_id` (numeric) | 4.0 |

**Finding:** CAS and S3 use **completely different numbering** for subclasses. CAS terminal
numbers (e.g. 444) do not correspond to S3 subclass_id (e.g. 7). All 22 CS-format
subclass accessions have terminal numbers in the 396-608 range, while S3 uses 1-43. They
can only be joined by **label matching**, which succeeds for all 42 shared subclasses.

20 CAS subclass accessions use hash-based format (`subclass_label:HASH`) with no numeric
ID at all.

### Supertype level

Supertypes exist **only in S3** (105 types with numeric IDs 1-105). CAS has no supertype
labelset. WMB carries `CTX_supertype_id` and `CTX_supertype_label` but these use a
**different numbering and different names** from S3 (see Section 4).

### Class level

S3 has 4 classes (GABAergic, Glutamatergic, Non-Neuronal, Low Quality). CAS has 3 (no
Low Quality). Class accessions in CAS are all hash-based (`class_label:HASH`).

## 3. Cluster-level label agreement

### CAS vs S3 (published)

**387/387 shared clusters: 100% label match.** The 4 S3-only clusters are:
- 381_SMC-Peri (minor non-neuronal type)
- 389, 390, 391 (Low Quality — correctly excluded from CAS)

CAS and S3 cluster labels are perfectly synchronised.

### CAS/S3 vs WMB CTX_cluster_label

**Only 6/29 hippocampal clusters match.** WMB labels carry `_N` suffixes
(e.g. `78_Sst_2`) that don't appear in CAS/S3 (`78_Sst HPF`), and some gene names
differ (WMB: `Ndnf HPF`, CAS/S3: `Ntng1 HPF`).

### S3 ref.cluster_label vs published cluster_label

**372/388 clusters (96%) were renumbered** between the ref (older) and published versions.
Only 16 retained the same numeric prefix. The ref version uses a completely different
cluster numbering scheme.

### WMB CTX_cluster_label vs S3 ref.cluster_label

**WMB labels match neither the published labels nor the ref labels.** WMB appears to
reference a **third, intermediate version** of the taxonomy that was loaded into the WMB
knowledge graph. It uses the published numeric IDs but with modified label strings.

## 4. Hierarchy membership

### Cluster -> Subclass

| Comparison | Agreement |
|------------|-----------|
| CAS vs S3 | 387/387 (100%) |
| WMB CTX_subclass vs CAS/S3 | 49/49 (100%, hippocampus slice) |

**Cluster-to-subclass membership is fully consistent** across all three sources.

### Cluster -> Supertype

| Comparison | Agreement |
|------------|-----------|
| WMB CTX_supertype vs S3 supertype (label) | 6/29 (21%) |
| WMB CTX_supertype vs S3 supertype (ID) | 6/29 (21%) |

**Supertype assignments are deeply inconsistent.** The mismatches fall into three patterns:

1. **WMB abbreviated** (missing subclass prefix): WMB "Ctsc" vs S3 "Sst Ctsc HPF",
   WMB "Lpl" vs S3 "Pvalb Lpl". These may be the same supertype with the subclass
   prefix stripped — 10 cases.

2. **Different gene names**: WMB "Ndnf HPF" vs S3 "Ntng1 HPF", WMB "Car10" vs S3
   "Vip Cp Rspo1", WMB "Ptprk" vs S3 "Vip Cbln4 HPF". These suggest genuinely
   different supertype definitions or a rename — 11 cases.

3. **Different supertype assignment**: cluster #30 is WMB "Krt73" (supertype 8) but
   S3 "Ntng1 HPF" (supertype 10) — different supertypes entirely. Cluster #77 is
   WMB "Th" but S3 "Sst Lmo1 HPF". Cluster #78 is WMB "Myh8 HPF" but S3
   "Sst Lmo1 HPF". These indicate the **supertype groupings themselves changed** — 7 cases.

Since supertype IDs also disagree (WMB sup_id != S3 supertype_id for 23/29 clusters),
the WMB is referencing a different supertype classification entirely.

### Supertype -> Subclass (S3 only)

Within S3, every supertype maps to exactly one subclass (105/105 single-parent). The
supertype level fits cleanly between cluster and subclass in the published hierarchy.

### ref.cluster_label grouping vs published subclass

6 ref-version cluster groups span multiple published subclasses:
- `197_L4/5 IT CTX` -> {L4/5 IT CTX, L5 IT CTX}
- `207_L5 IT CTX` -> {L4/5 IT CTX, L5 IT CTX}
- `211_L5 IT TPE-ENT` -> {L5/6 IT TPE-ENT, L2/3 IT RHP}
- `227_L6 IT CTX` -> {L6 IT CTX, L5 IT CTX}
- `311_L6 NP CT CTX*` -> {L6 CT CTX, L5/6 NP CTX}
- `323_L6 CT CTX` -> {L6 CT CTX, L6b CTX}

This confirms the older clustering had **different subclass boundaries** from the
published version.

## 5. Version timeline (inferred)

```
ref version (pre-publication)
  - Different cluster numbering (372/388 clusters renumbered)
  - Different subclass boundaries (6 groups span multiple published subclasses)
  - Labels in S3 ref.cluster_label column
       |
       v
WMB intermediate version
  - Adopted published cluster numeric IDs
  - But carries modified labels (_N suffixes, gene name changes)
  - Different supertype IDs and labels from published S3
  - This is what WMB CTX_* fields reference
       |
       v
Published version (Yao 2021 / CAS)
  - CAS JSON = S3 cluster labels (387/387 match)
  - CAS cluster->subclass = S3 cluster->subclass (387/387 match)
  - S3 has supertypes, regional proportions, cell counts not in CAS
  - S3 has ref.cluster_label showing the older version
```

## 6. Implications for evidencell

### Cross-taxonomy annotation transfer edges (WMB -> CTX)

The 49 AT edges we built join WMB clusters to CTX clusters via `CTX_cluster_id`. The
**numeric cluster IDs are reliable** — they match across all three sources. However:

- The AT algorithm in WMB was likely run against the **intermediate version**, not the
  published taxonomy. Cell set composition may have shifted between versions.
- Supertype-level cross-references from WMB (`CTX_supertype_label`) are unreliable —
  they reference a different supertype classification.
- Subclass-level cross-references from WMB (`CTX_subclass_label`) are reliable —
  they match CAS/S3 for all 49 hippocampus clusters.

**Recommendation:** Treat AT edges as **approximate cross-references** (confidence: LOW,
relationship: OVERLAPS). The cluster-level join is solid; supertype-level should not be
used. Record WMB-side labels in `name_in_source` for audit trail.

### CTX taxonomy enrichment from Table S3

S3 is synchronised with CAS at cluster level (100% agreement). Safe to enrich CTX
taxonomy nodes with:
- **Regional cell proportions** (HIP, RHP columns) — properties of the published clusters
- **Cell counts** (10X, Smart-seq) — properties of the published clusters  
- **Sex ratios** — properties of the published clusters
- **Supertype names as descriptive metadata** on cluster nodes (not as hierarchy nodes)

**Not safe:** Inserting supertypes as hierarchy nodes with synthetic accessions, or
treating S3 supertype assignments as matching the AT version.

### Re-running annotation transfer

For definitive cross-taxonomy AT with proper F1 scores, the cleanest path would be to
re-run MapMyCells using the published CAS taxonomy. This requires:
- The CellxGene dataset (matrix_file_id: `CellXGene_dataset:ece4094a-8f3d-430d-babe-467fb6fd5feb`)
- Or asking Allen for a version-matched taxonomy + reference data

This would produce clean, version-matched AT results without the three-version ambiguity.

## 7. Summary table

| Question | Answer |
|----------|--------|
| Do cluster numeric IDs match across sources? | Yes (all three) |
| Do cluster labels match? | CAS=S3 (100%), WMB differs (21%) |
| Do subclass IDs match? | No — CAS and S3 use different numbering |
| Do subclass labels match? | Yes (all 42 shared) |
| Do subclass memberships match? | Yes (387/387 CAS=S3, 49/49 WMB=CAS/S3) |
| Do supertype IDs/labels match? | No — WMB vs S3 disagree (79%) |
| Do supertype memberships match? | Cannot verify (WMB supertypes are different entities) |
| How many taxonomy versions exist? | At least 3 (ref, WMB intermediate, published) |
| Is the CAS authoritative? | Yes, for the published taxonomy |
| Is S3 compatible with CAS? | Yes, for clusters and subclasses |
| Are WMB CTX_* AT edges trustworthy? | Cluster IDs: yes. Labels/supertypes: no |

---

*Generated by evidencell taxonomy reconciliation analysis, 2026-04-22.*

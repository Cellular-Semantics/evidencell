# Schema Critique — celltype_mapping.yaml v0.4

**Date**: 2026-03-11
**Schema reviewed**: `schema/celltype_mapping.yaml` v0.4
**KB examples reviewed**: `GPi_shell_neuron.yaml`, `GPi_shell_neuron_Mmus.yaml`, `CB_MLI_types.yaml`

Review goals:
1. Properties and their evidence should be clear on nodes
2. Edge evidence should record explicitly where properties between nodes align, approximately align, or do not align
3. Annotation transfer evidence handled correctly
4. Formality of entity records: when IDs vs free text

---

## What is working well — do not change

- **`GeneDescriptor`** (`symbol` + `ncbi_gene_id`): already implements the name-in-source + official ID pattern correctly. `symbol` is the source gene name; `ncbi_gene_id` is the cross-species stable identifier. The pattern is correct.
- **`atlas_nt_type` vs `nt_type`** distinction: `atlas_nt_type: "Glut-GABA"` (verbatim from atlas) vs `nt_type: "GABA-Glut (dual)"` (curatorial) is the right design. Preserves source naming while allowing standardisation.
- **`anatomical_annotation` on `AtlasMetadataEvidence`**: captures verbatim atlas source text (e.g. `"GPi shell and surrounding GPi core neurons"`). Correct.
- **Evidence type taxonomy** (`EvidenceType` enum) and **typed `Caveat` structure**: solid. Keep.
- **`AnnotationTransferEvidence`**: present in schema and working in mouse GPi example. Correct scope.
- **Free-string `taxonomy_level`** (v0.4 fix): correct. Atlas-specific level names preserved without forcing an enum.
- **Location split** (`CellTypeColocation` on node for relative colocation; `AnatomicalLocation` for absolute location; `SpatialColocationEvidence` for spatial evidence from a dataset): the split is already done correctly in v0.4. No further splitting needed.

---

## Gap 1 — Node property provenance

**Problem**: `CellTypeNode` asserts marker lists, NT type, anatomy, etc. with no source citation. For classical nodes there is no way to know which paper established which property. `prior_reference` exists for `PRIOR_TRANSCRIPTOMIC` nodes but classical nodes have nothing equivalent. The edge evidence records *why properties match*, but there is no record of *where the node's properties came from*.

**Fix**: Add `definition_references` (list of DOI/PMID strings) to `CellTypeNode`. Not full evidence items — just source citations for the node's stated properties.

```yaml
# on CellTypeNode, alongside nt_type / defining_markers etc:
definition_references:
  - "https://doi.org/10.1016/j.neuron.2017.03.017"
  - "PMID:28384468"
```

For atlas nodes, `atlas` + `cell_set_accession` + `metadata_url` (on evidence items) already implicitly cite the source. No additional field needed there.

---

## Gap 2 — Property alignment on edges (most important gap)

**Problem**: Edge evidence items have a free-text `explanation`. The only structured property comparison is `nt_consistent_with_classical: boolean` on `AtlasMetadataEvidence`. There is no machine-readable record of *which specific properties were compared and how well they matched*. This makes the basis for `confidence` judgments opaque and unreportable.

The three cases the schema needs to handle clearly:
- Properties agree (same biology, possibly different naming convention)
- Properties approximately agree (different spatial resolution, partial marker overlap, cross-species naming)
- Properties conflict (genuine discordance — this is evidence *against* the mapping)

**Fix**: Add a `PropertyComparison` class and `property_comparisons` list at the `MappingEdge` level. This sits alongside the `evidence` list as a structured summary of the property-by-property comparison that underlies the `confidence` judgment.

### New enum: `PropertyAlignment`

```yaml
PropertyAlignment:
  permissible_values:
    CONSISTENT:
      description: Properties agree (same value or equivalent, modulo naming convention)
    APPROXIMATE:
      description: >
        Properties broadly agree but differ in resolution, naming convention, or species;
        or one is a subset of the other. E.g. "GPi shell" vs atlas-annotated "GPi";
        Sst in classical description vs Sst in 2/3 atlas clusters.
    DISCORDANT:
      description: Properties conflict — constitutes evidence against the mapping
    NOT_ASSESSED:
      description: Property not evaluated for this edge
```

### New class: `PropertyComparison`

```yaml
PropertyComparison:
  description: >
    A structured comparison of one property between two nodes on a mapping edge.
    Complements evidence items: evidence items provide the justification detail;
    property_comparisons give a machine-readable property-level alignment summary.
    At minimum, cover: nt_type, location, and all defining markers.
  attributes:
    property:
      required: true
      description: >
        Name of the property compared. Suggested values:
        nt_type, location, marker_{gene}, morphology, electrophysiology,
        projection_target, ccf_distribution. Free text — be specific.
    node_a_value:
      required: true
      description: >
        Value of this property as stated for type_a (use node text, not paraphrase).
    node_b_value:
      required: true
      description: >
        Value of this property as stated for type_b (verbatim from node or source metadata).
    alignment:
      required: true
      range: PropertyAlignment
    notes:
      description: >
        Brief explanation of the alignment call.
        Required for APPROXIMATE and DISCORDANT.
```

### Add to `MappingEdge`

```yaml
property_comparisons:
  multivalued: true
  inlined_as_list: true
  range: PropertyComparison
  description: >
    Structured property-by-property comparison between type_a and type_b.
    Provides machine-readable basis for the confidence judgment.
    At minimum, cover: nt_type, location, and all defining markers.
```

### Example (GPi shell mouse edge)

```yaml
property_comparisons:
  - property: nt_type
    node_a_value: "GABA-Glut (dual)"
    node_b_value: "Glut-GABA"
    alignment: CONSISTENT
    notes: "Same dual-transmitter biology; WMBv1 lists glutamatergic co-transmitter first by convention"
  - property: location
    node_a_value: "Internal segment of globus pallidus, shell region"
    node_b_value: "GPi (MERFISH annotated)"
    alignment: APPROXIMATE
    notes: "Atlas annotation covers whole GPi; shell localisation is sub-regional. MERFISH registration uncertainty adds noise."
  - property: marker_Tbr1
    node_a_value: "Tbr1 (positive)"
    node_b_value: "Tbr1 (TF marker, all 3 clusters)"
    alignment: CONSISTENT
  - property: marker_Sst
    node_a_value: "Sst (positive)"
    node_b_value: "Sst neuropeptide in 2/3 clusters"
    alignment: APPROXIMATE
    notes: "Sst present in 2/3 clusters of the supertype, not universal"
  - property: marker_Pvalb
    node_a_value: "Pvalb (absent)"
    node_b_value: "Pvalb not listed as positive marker"
    alignment: CONSISTENT
```

**Consequence**: `nt_consistent_with_classical: boolean` on `AtlasMetadataEvidence` is superseded by `property_comparisons`. Deprecate it (mark as deprecated in schema comment, keep for backward compat).

---

## Gap 3 — Name-in-source convention: genes correct, regions ambiguous

**Problem**: For genes the pattern is correct (`symbol` = source name, `ncbi_gene_id` = official). For anatomical regions `AnatomicalLocation.name` is curatorial free text — there is no explicit convention that it should prefer the source's own wording over invented descriptions.

**Fix 1**: Rename `AnatomicalLocation.name` → `region_name` and update the description:

```yaml
region_name:
  required: true
  description: >
    Name of this anatomical region, preferring the source's own terminology
    where possible. E.g. "GPi shell region" from the paper rather than an
    invented curatorial label. When a source name is not available, use a
    standard anatomical name consistent with UBERON.
```

**Fix 2**: Add a naming convention comment to the schema header:

```yaml
# NAMING CONVENTION:
# For all named entities, record the name as it appears in the source
# (name_in_source) alongside any official ID. This is critical because source
# names encode curatorial intent even when ID mappings are uncertain or wrong.
#
# Entity-specific conventions:
#   Genes:    GeneDescriptor.symbol = source gene symbol (name_in_source);
#             ncbi_gene_id = official cross-species ID (strongly recommended)
#   Regions:  AnatomicalLocation.region_name = source-preferred name;
#             uberon_term / allen_atlas_term = official IDs (when verifiable)
#   Atlas NT: CellTypeNode.atlas_nt_type = verbatim from atlas spreadsheet;
#             CellTypeNode.nt_type = curatorial/standardised version on classical nodes
#   Taxonomy: cell_set_accession is the stable source ID; name is the human label
```

---

## Gap 4 — Free text vs ID policy not stated

**Fix**: Add to schema header alongside naming convention:

```yaml
# FREE TEXT vs ID POLICY:
# Official IDs (OntologyTerm, ncbi_gene_id) are strongly recommended for shared
# entities that appear across multiple mappings: genes, brain regions, species,
# ontology terms. They enable cross-graph queries and validation.
#
# Free text is sufficient (and preferred over guessed IDs) when:
#   - The concept is specific to a single source/atlas and has no standard term
#   - The mapping to an official term is genuinely uncertain (novel region, ambiguous homology)
#   - The field captures source-verbatim text that may conflict with official labels
#
# Never invent an ID that has not been verified against the authoritative source.
# An absent ncbi_gene_id is better than a wrong one.
# Use the `notes` field to flag IDs pending verification.
```

---

## Gap 5 — `AnnotationTransferEvidence` missing species fields

**Problem**: Annotation transfer is frequently cross-species (primate → mouse WMBv1). There are no `source_species` / `target_species` fields. Species can be inferred from node context but is not explicit on the evidence item.

**Fix**: Add to `AnnotationTransferEvidence`:

```yaml
source_species:
  range: OntologyTerm
  description: >
    NCBITaxon term for the species of the source dataset.
    Required when source and target species differ.
target_species:
  range: OntologyTerm
  description: NCBITaxon term for the species of the target atlas.
```

---

## Summary of changes

| # | Change | Type | Backward-compat? |
|---|---|---|---|
| 1 | Add `definition_references: [string]` to `CellTypeNode` | New field | Yes |
| 2 | Add `PropertyAlignment` enum | New enum | Yes |
| 3 | Add `PropertyComparison` class | New class | Yes |
| 4 | Add `property_comparisons` list to `MappingEdge` | New field | Yes |
| 5 | Rename `AnatomicalLocation.name` → `region_name` | Rename | **No** — existing YAML needs field rename |
| 6 | Add naming convention + free text policy to schema header | Documentation | Yes |
| 7 | Add `source_species` / `target_species` to `AnnotationTransferEvidence` | New fields | Yes |
| 8 | Deprecate `nt_consistent_with_classical` (superseded by #4) | Deprecation | Yes (keep field, add comment) |

The only breaking change is item 5 (`region_name` rename). All three existing KB YAML files need a one-line field rename: `name:` → `region_name:` inside any `AnatomicalLocation` block.

---

## Deferred (from scratch_notes.md — already resolved in v0.4)

- ~~Split `SpatialColocationEvidence`~~: already done via `CellTypeColocation` + `AnatomicalLocation`
- ~~Switch gene IDs HGNC → NCBIGene~~: done in v0.4 (`ncbi_gene_id`)
- ~~`TaxonomyLevel` enum~~: removed in v0.4, now free string
- ~~Incorrect hierarchy text in examples~~: `Class > Group` in HMBA BG is now correctly noted

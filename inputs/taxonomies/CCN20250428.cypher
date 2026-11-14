// CCN20250428 — HMBA Basal Ganglia consensus taxonomy (primate; human, macaque, marmoset)
// Fetch from brain_cell_KG (neo4j). Run via: just fetch-taxonomy-kg inputs/taxonomies/CCN20250428.cypher CCN20250428
// Returns canonical column names: node, parent_curie, cl, anat, level
//
// Same pattern as CCN20230722.cypher with WMB: → BG: and MBA: → DHBA:. Verified
// 2026-11-11 against the live KG (post brain_cell_KG 2026-10-27 rebuild):
//   rows=113  with_parent=109  with_cl=87  anat_entries=86  levels=4
//   levels: Group 61 (terminal) < Subclass 36 < Class 12 < Neighborhood 4
//
// BG specifics, versus WMBv1:
//   - Anatomy is DHBA (developing human brain atlas), not MBA. brain_cell_KG
//     transferred the HMBA Group soma locations from the CL/PCL class onto the
//     BG: cell sets (bg_group_location_mappings.owl, 2026-10-27), using the
//     same obsolete_some_soma_located_in / obsolete_cell_ratio edge pattern as
//     WMBv1, so no two-hop path via exemplar_data_of is needed any more.
//   - Group level only: 86 location edges over all 61 Groups; five regions
//     (DHBA:10333 striatum, DHBA:10343 GPe, DHBA:12251 SN, DHBA:10466 STH,
//     DHBA:10344 GPi). Non-Group nodes carry no anatomy (anat = []).
//   - Ratios only, no cell_count. cell_ratio is the fraction of the Group's
//     cells in that region, rounded to 1 d.p. upstream; per-Group sums are
//     0.9–1.0 because the upstream "Adj" (adjacent-tissue) fraction is not a
//     location and is carried separately as n2o:adjacentCellRatio. Do not
//     assume the ratios sum to 1.
//   - Provenance per edge in the KG: evidence = EFO:0008992 (MERFISH), comment =
//     "Location assignment based on CCF broad region.". The source column is
//     the taxonomy release citation (Johansen, Fu et al. 2025, bioRxiv
//     10.64898/2025.12.15.694496 — whose HMBA_BG_consensus_annotation.csv
//     carries the spatial_regional_proportions) so that
//     AnatomicalLocation.sources.ref is a citation, as PropertySource.ref
//     requires; the EFO assay code is mapped to the method string at ingest
//     (_SPATIAL_METHOD_BY_DOI).
//   - No nt_type property on any BG node. NT is derived at ingest from the
//     cluster label (field_mapping.json: nt_type_from_label) and qualified
//     with taxonomy_meta nt_provenance. No NT column here.
//   - Markers: marker_gene_evidence (curator rationale genes) on 42/61 Groups
//     only; mapped to defining_markers in field_mapping.json. The precomputed
//     stats panel (just add-expression) is the real marker source for BG.
//   - The CASE WHEN guard keeps collect() from emitting an all-null entry
//     for nodes with no anatomy.
MATCH (node:Individual)-[:has_labelset]->(labelset)
WHERE node.curie STARTS WITH "BG:"
OPTIONAL MATCH (node)-[:subcluster_of]->(parent:Individual) WHERE parent.curie STARTS WITH "BG:"
OPTIONAL MATCH (node)-[:composed_primarily_of]->(cl:Cell) WHERE cl.curie =~ "CL:\\d{7}"
OPTIONAL MATCH (node)-[r:obsolete_some_soma_located_in]->(anat) WHERE anat.curie STARTS WITH "DHBA:"
WITH node, parent, cl, labelset,
     collect(CASE WHEN anat IS NULL THEN null ELSE {
       anat_id:    anat.curie,
       anat_label: anat.label,
       cell_ratio: toFloat(head(r.obsolete_cell_ratio)),
       source:     "https://doi.org/10.64898/2025.12.15.694496",
       evidence:   head(r.evidence),
       notes:      head(r.comment)
     } END) AS anat
RETURN cl, node, parent.curie AS parent_curie, labelset.short_form AS level, anat

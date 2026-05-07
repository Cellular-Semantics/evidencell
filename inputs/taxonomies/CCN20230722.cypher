// Cypher query to export WMBv1 (CCN20230722) taxonomy from brain_cell_KG
// Returns canonical column names: node, parent_curie, cl, anat, level
// Run with: just fetch-taxonomy-kg inputs/taxonomies/CCN20230722.cypher CCN20230722
//
// Notes on KG schema (post-2026-04 rebuild):
//   - WMB nodes are labelled (Cell_cluster:Individual); previous (WMB) label removed.
//     Filter by curie pattern instead of label for robustness.
//   - Taxonomy level is now exposed via -[:has_labelset]->(labelset) — old labels
//     like "CCN20230722_supertype" are gone. Filter on has_labelset to drop the
//     5 labelset meta-nodes and 2 duplicate NEUR_* nodes lacking the edge.
//   - Parent edge renamed: subclass_of → subcluster_of.
//   - Anatomy edge renamed: was unspecified rel type → obsolete_some_soma_located_in.
//   - r.cell_ratio → r.obsolete_cell_ratio (aliased back to cell_ratio for ingest).
//   - WMB nodes now carry top-level cell_count (10x per-node count) which rides
//     along inside the returned `node` map and is mapped to TaxonomyNode.n_cells.
//   - Spatial sources merged: a single edge per (cluster, MBA region) carries
//     parallel lists for cell_count, obsolete_cell_ratio, and source (DOIs).
//     Order is aligned across the three lists — index i is one source's
//     contribution. Yao 2024 and Zhuang 2023 are the two known DOIs; future
//     spatial datasets will append additional list entries. evidencell expands
//     each (region, source) pair into its own AnatomicalLocation entry on
//     ingest (see taxonomy_db._extract_node).
MATCH (node:Individual)-[:has_labelset]->(labelset)
WHERE node.curie STARTS WITH "WMB:"
OPTIONAL MATCH (node)-[:subcluster_of]->(parent:Individual) WHERE parent.curie STARTS WITH "WMB:"
OPTIONAL MATCH (node)-[:composed_primarily_of]->(cl:Cell) WHERE cl.curie =~ "CL:\\d{7}"
OPTIONAL MATCH (node)-[r:obsolete_some_soma_located_in]->(anat) WHERE anat.curie STARTS WITH "MBA:"
RETURN cl, node, parent.curie AS parent_curie, labelset.short_form AS level,
       collect({cell_count: r.cell_count, cell_ratio: r.obsolete_cell_ratio,
                source: r.source,
                anat_label: anat.label, anat_id: anat.curie}) AS anat

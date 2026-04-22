// Cypher query to export WMBv1 (CCN20230722) taxonomy from brain_cell_KG
// Returns canonical column names: node, parent_curie, cl, anat
// Run with: just fetch-taxonomy-kg inputs/taxonomies/CCN20230722.cypher CCN20230722
MATCH (node:WMB:Individual)
OPTIONAL MATCH (node)-[:subclass_of]->(parent:WMB)
OPTIONAL MATCH (node)-[:composed_primarily_of]->(cl:Cell) WHERE cl.curie =~ "CL:\\d{7}"
OPTIONAL MATCH (node)-[r]->(anat:MBA)
RETURN cl, node, parent.curie AS parent_curie,
       collect({cell_count: r.cell_count, cell_ratio: r.cell_ratio,
                anat_label: anat.label, anat_id: anat.curie}) AS anat

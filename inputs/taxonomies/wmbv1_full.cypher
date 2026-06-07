// Query used to generate wmbv1_full.json from brain_cell_KG.
//
// Spatial annotation edges (`obsolete_some_soma_located_in`) carry parallel
// arrays indexed by `source` DOI:
//   - cell_count[i]            soma strictly in region (legacy count)
//   - obsolete_cell_ratio[i]   cell_count[i] / cluster cell_count
//                              (upstream renamed from `cell_ratio`)
//   - countInOrNear100um[i]    soma in or within 100µm of region (current
//                              authoritative spatial count)
//   - source[i]                DOI of the contributing study
//
// Per-edge (not per-source):
//   - cellCountCompleteness   null on CCF2020-painted leaf domains
//                             (authoritative); 'exact' on rollup edges
//                             whose descendants are all painted; or
//                             'lower_bound' on rollup edges with
//                             non-painted descendants. See issue #95.
//
// Within evidencell we retain the internal name `cell_ratio` for the
// legacy ratio (audit / continuity) and additionally surface the new
// 100µm count + ratio. Upstream applies the region-inclusion threshold;
// we precalc the ratio in Cypher but do no filtering here. See
// https://github.com/Cellular-Semantics/evidencell/issues/93.
MATCH (wmb:Individual:CCN20230722)
OPTIONAL MATCH (wmb)-[:subcluster_of]->(wmb_parent:Individual:CCN20230722)
OPTIONAL MATCH (wmb)-[:composed_primarily_of]->(cl:Cell)
  WHERE cl.curie =~ "CL:\\d{7}"
OPTIONAL MATCH (wmb)-[r:obsolete_some_soma_located_in]->(anat:MBA)
RETURN cl,
       wmb,
       wmb_parent.curie,
       collect({
         anat_id: anat.curie,
         anat_label: anat.label,
         cell_count: r.cell_count,
         cell_ratio: r.obsolete_cell_ratio,
         count_in_or_near_100um: r.countInOrNear100um,
         ratio_in_or_near_100um: CASE
           WHEN head(wmb.cell_count) IS NULL OR head(wmb.cell_count) = 0 THEN null
           ELSE [x IN r.countInOrNear100um | toFloat(x) / head(wmb.cell_count)]
         END,
         source: r.source,
         cell_count_completeness: head(r.cellCountCompleteness)
       }) AS anat

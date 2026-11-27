// Cypher query to export WMBv1 (CCN20230722) marker sets from brain_cell_KG (#274)
// Returns one row per (marker set, class it hangs off), with the class's
// exemplar cell sets. Run with:
//   just fetch-taxonomy-kg inputs/taxonomies/CCN20230722_marker_sets.cypher CCN20230722 \
//       --output inputs/taxonomies/CCN20230722_marker_sets.json
// Parsed by evidencell.marker_sets at ingest (path declared as marker_sets_file
// in inputs/taxonomies/CCN20230722_meta.yaml).
//
// Graph shape (checked 2026-11-27):
//   (cls:Class)-[:has_exemplar_data]->(cellset:CCN20230722)
//   (cls)-[:has_marker_set]->(m:Class)-[:has_part]->(g:Gene {curie: NCBIGene:…})
//   m.label         "Car3,Satb2,Lgr5 (Yao)." | "Lgr5 (Yao - within subclass)."
//                   | "Inhba, Tfap2b (NSforest)." | "… (CAS evidence)." (unscored)
//   m.precision / m.recall / m.F4beta_score — single-element lists; recall is a
//   string (WMBO types all three xsd:string). F4beta_score is F-beta with
//   beta = 0.5. The copy on the has_marker_set edge disagrees with the set's
//   own value on 3 CL-class sets; the set's value is the one returned.
//
// Exemplars: every PCL class has one has_exemplar_data target. Some CL classes
// have 2–3: the most specific cell set plus its subcluster_of ancestors
// (entailed links the KG materialises for CL terms only). All targets are
// returned with `finest` (targets no other target is a subcluster_of*
// ancestor of) and `ancestors_ok` (every other target is an ancestor of the
// finest); the ingest asserts exactly one finest target and ancestors_ok.
// Do not use exemplar_data_of: it also links same-cell ancestor cell sets.
MATCH (cls:Class)-[:has_exemplar_data]->(i:CCN20230722)
WHERE NOT cls:CCN20230722 AND (cls)-[:has_marker_set]->()
WITH cls, collect(i) AS cs
WITH cls, cs,
     [x IN cs WHERE none(y IN cs WHERE y <> x AND exists((y)-[:subcluster_of*]->(x)))] AS finest
WITH cls, cs, finest,
     all(f IN finest WHERE all(y IN cs WHERE y = f OR exists((f)-[:subcluster_of*]->(y)))) AS ancestors_ok
MATCH (cls)-[:has_marker_set]->(m)
OPTIONAL MATCH (m)-[:has_part]->(g:Gene)
RETURN cls.curie AS via_class,
       [x IN cs | x.curie] AS exemplars,
       [x IN finest | x.curie] AS finest,
       ancestors_ok,
       m.curie AS set_id,
       m.label AS set_label,
       m.database_cross_reference AS xref,
       m.algorithm AS algorithm,
       m.precision AS precision,
       m.recall AS recall,
       m.F4beta_score AS f_beta,
       [x IN collect(g) WHERE x IS NOT NULL | {curie: x.curie, label: x.label}] AS genes
ORDER BY set_id

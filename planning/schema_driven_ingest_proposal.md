# Schema-driven ASTA ingest — proposal

**Issue:** #202 · **Status:** proposal for review (2026-11-15) · **Related:** #196 / #203, #204, #183, #163, #154, #116

## Summary

ASTA report ingest becomes a single pass that writes the most complete content it
can, straight into small graph files under `kb/graphs/{region}/`. Three ideas
drive it:

1. **Identity decisions come first.** Before any node is written, each type the
   report proposes is reconciled against what the KB already holds: new, the same
   as an existing node, a subtype or supertype of one, or overlapping. That is the
   decision that is expensive to undo (ids are minted; #154, #116), so it gets its
   own step and its own review.
2. **Everything else is driven by the schema.** Each authorable `CellTypeNode`
   slot carries an ingest question as a schema annotation. Code pulls the
   questions plus the relevant schema slice into the authoring prompt. The prompt
   keeps only workflow policy.
3. **Hierarchy uses existing mapping edges.** Lit-to-lit subtype relations are
   written as `MappingEdge`s with `skos:broadMatch`, following a written
   convention that lives outside the schema. No new schema for subtypes for now
   (the #183 design stays parked).

`survey.md` and `evidence-extraction.md` are folded in and deprecated.

**Main finding from the downstream survey:** "questions + schema slice" can
carry nearly all of the authoring guidance, *provided* downstream code reads the
controlled fields the schema already has instead of the verbatim ones.
Today `find-candidates` treats two verbatim fields (`GeneDescriptor.symbol`,
`nt_type.name_in_source`) as controlled vocabulary. If those stay as they are,
the prompt has to carry hand-written rules that contradict the schema
descriptions. That is the same drift #202 sets out to remove.

---

## 1. Decisions this proposal builds on

| Decision | Where recorded |
|---|---|
| Ingest questions live in the schema, as slot annotations | #202 comment, 2026-11-15 |
| Fold `survey` and `evidence-extraction` into one authoring step; deprecate both, keeping them to reuse if ASTA API search returns | #202 scope-update comment |
| Lit-to-lit hierarchy uses current `MappingEdge` + an ingest convention outside the schema; no new subtype schema for now | This proposal. To be noted on #183 |
| Accept ASTA quotes as accurate, pending an eval | #202 "do first" list |
| `at_source_sets` generalisation is a separate design | #204 |

---

## 2. Downstream contract

This is what the tools after ingest actually read from a classical node, from a
code survey of `src/evidencell/`. Every tool reads YAML as plain dicts. None of
them goes through the pydantic models, so a misnamed key fails silently.

### 2.1 Fields that drive behaviour

| Field | Read by | Requirement in practice |
|---|---|---|
| `id`, `name`, `definition_basis` | everything | `id` canonical in exactly one file. `at-coverage` keeps only `definition_basis` starting with `CLASSICAL` (`at_metrics.py:1242`) |
| `defining_markers[]`, `negative_markers[]`, `neuropeptides[]` `.symbol` | find-candidates, emit-stage-b, gen-facts | find-candidates matches exact, case-sensitive mouse atlas symbols with **no alias resolution**. emit-stage-b *does* resolve aliases (`marker_aliases`). So `PV` scores in Stage B but is missed at candidate retrieval |
| `nt_type.name_in_source` | find-candidates (hard filter, `taxonomy_db.py:2721`), emit-stage-b, gen-facts | Prefix-compatible with atlas NT labels (`GABA`, `Glut`, `GABA-Glyc`, …). "inhibitory" or "glycinergic" filter out every candidate. `nt_type.cl_terms` is not read |
| `anatomical_location[]` `.id`, `.label`, `.name_in_source`, `.compartment` | find-candidates, emit-stage-b, gen-facts | MBA ids preferred. UBERON is mapped to MBA where an xref exists; DHBA/HOMBA ids match nothing. `AXON_TARGET`/`DENDRITE` are excluded from scoring (gen-facts ignores compartment, a bug) |
| `sex_bias` | find-candidates | Optional scoring criterion |
| `at_source_sets[]` `.dataset_accession`, `.source_label`, `.correspondence` | find-candidates, emit-stage-b, at-coverage | Both keys are needed, or the entry is skipped |
| `cl_mapping`, `proposed_cl_term` | gen-facts / reports, cl-term-request | |
| `sources[].ref`, `.quote_key` | validate, qc, gen-facts | `PMID:`/`DOI:` form. Key is `{corpus_id}_{hash}` and present in the region store |

### 2.2 Written but read by no code

`synonyms`, `species`, `colocated_types`, `nt_type.cl_terms`, `morphology`,
`electrophysiology` (gen-facts reads stale keys, see §8),
`definition_references`, `prior_*`, `marker_type`, and every `PropertySource`
field except `ref`/`quote_key`.

These still matter, for curation, CL term requests, node review and future
consumers. But a missing value in one of them breaks nothing now, so the ingest
design does not have to treat them as load-bearing.

### 2.3 Lit-to-lit edges today

There are 11 edges and 6 `LIT_TYPE` stubs (IGL, OLM, cerebellum).

- **Validation:** fine, as long as the other endpoint is in the same file as a
  canonical node or a stub.
- **Mapping consumers:** pool-candidates, at-metrics and refresh-expression-pcs
  ignore them harmlessly. refresh-property-comparisons reports and skips them.
- **Problems:** see §6.3. In short, gen-facts and reports show them as atlas
  mapping candidates, stubs get rendered as empty reports, `gen-toc` drops them,
  and the parent side can't see them.

### 2.4 Side effects ingest must respect

- **`orphan_node` WARN.** It fires for any canonical node with no edge in its own
  file, so every freshly ingested node triggers it. That's expected and noisy;
  see §8.
- **Rationale hash.** It covers every field of a lit node. Any edit to an
  existing node marks its mapped edges `rationale_stale`. That's correct when
  content changes, and wasteful when an edit only reformats. Merges must
  `Edit` in place, never rewrite the file.

---

## 3. Can questions + schema slices replicate everything else?

**Mostly yes.** What remains splits into four kinds. Only the last needs new
machinery.

| Kind of guidance | Example | Where it should live |
|---|---|---|
| **Facts about valid values** | marker symbol conventions; NT vocabulary; MBA-first anatomy; `NOT_STATED` vs guessing | **Schema descriptions.** Some are missing or wrong today (§3.1) |
| **What to ask, and what to do with partial evidence** | "Which species?", "record as a lead; never construct a label" | **Schema annotations** (§4) |
| **Workflow policy** | one node per file; write via the Write tool; quote_keys only; no atlas mapping edges at ingest; merge = in-place Edit | **Workflow prompt.** Short, stable, not schema facts |
| **KB context and identity** | which nodes exist; is this the same type; is it a subtype | **New step with KB context** (§5 Step 3), plus the hierarchy convention (§6) |

### 3.1 Where descriptions and downstream disagree today

A generated slice only helps if the descriptions are right. The survey found these
gaps:

| Slot | Schema says | Downstream needs | Fix |
|---|---|---|---|
| `GeneDescriptor.symbol` | "exactly as it appears in the source" (human `SST`, protein-style allowed by implication) | find-candidates needs mouse atlas symbols, no aliasing | **Fix code, not the description.** find-candidates should resolve aliases the way emit-stage-b does (`marker_aliases`), and ideally by `ncbi_gene_id` (`planning/gene_id_normalisation_plan.md`). Recording the source's symbol is right for provenance |
| `NeurotransmitterType.name_in_source` | "exactly as written in the source" | find-candidates uses it as a controlled filter | **Fix code.** Filter on `nt_type.cl_terms`, the controlled field, which already exists. The slice then asks for both: the verbatim label and the CL terms |
| Anatomy ontology preference | MBA → DHBA/HBA → UBERON rule lives in a **YAML comment** block above `HasMarkerType` | gen-facts and find-candidates expect MBA; SchemaView cannot see comments | Move it into the `AnatomicalLocation` class description. The `CellTypeNode.anatomical_location` description already summarises it |
| `definition_basis` | no description | the agent must choose CLASSICAL_* vs PRIOR_TRANSCRIPTOMIC; at-coverage filters on it | Add a description (description-cleanup PR) |
| `species` | "NCBITaxon term" | single-valued; pooled-species nodes can't express their species | Description says what to do when sources disagree (§4.3). Multivalued is an open question |

With these fixed, the slice carries the conventions and the prompt needs no
special rules about symbols, NT labels or anatomy.

---

## 4. Questions in the schema

### 4.1 Annotation keys

These go on `CellTypeNode` attributes. Nested classes (`MarkerSource`,
`AnatomicalLocation`, …) are pulled in by the slice generator through the slot's
range, so their descriptions travel with the question that uses them.

| Key | Meaning |
|---|---|
| `ingest_question` | The question the authoring agent answers for this slot |
| `ingest_if_partial` | What to do when the evidence is incomplete: a sentinel value, or "record as a lead in unplaced findings; never construct an identifier" |
| `ingest_alternatives` | Other slots the same question can resolve into. The slice includes their descriptions so the agent can tell them apart |
| `ingest_skip` | Reason the slot is *not* asked at ingest (atlas-only, set by another step, derived) |

**Coverage rule, enforced by a test:** every `CellTypeNode` slot has exactly one
of `ingest_question` or `ingest_skip`, and every `ingest_alternatives` entry
names a real slot. A new slot without a decision fails CI. That closes failure
mode (a) in #202 for good: a slot can no longer be hidden by omission.

Workflow-keyed variants (`extraction_question`, …) are added only if a second
workflow needs different wording.

Checked: SchemaView exposes slot annotations (`induced_slot(...).annotations`),
and `gen-pydantic` copies them into `_models.py` as `linkml_meta`. The new CI
drift check covers that.

### 4.2 Example

```yaml
      species:
        range: OntologyTerm
        description: >
          NCBITaxon term for the species the defining evidence comes from.
          When sources span species, use the species of the defining
          evidence and record each source's species in its `scope`.
        annotations:
          ingest_question: >-
            Which species do the cited sources describe for this type?
          ingest_if_partial: >-
            If sources pool species, set the species of the defining
            evidence and add an unplaced finding "multi-species" listing
            the others. Never leave species null because sources differ.
```

### 4.3 Question catalogue (draft wording)

Groups follow the order the authoring agent works through them.

| # | Slot(s) | Question | Partial / notes |
|---|---|---|---|
| Q1 | `definition_basis` (alt: `prior_dataset_accession`, `prior_cluster_label`, `prior_reference`) | How is this type defined in the sources: by anatomy/morphology/physiology, by several modalities, or as a cluster in a prior transcriptomic dataset? | PRIOR_TRANSCRIPTOMIC only with accession + label from the source |
| Q2 | `species` | Which species do the cited sources describe? | See §4.2 |
| Q3 | `anatomical_location` | Where are the somata located, and are any other compartments (axon targets, dendrites) described? | Provisional parent term when no child term exists; the gap goes to unplaced findings, not `notes` |
| Q4 | `colocated_types` | Which other cell types are described as intermingled with or adjacent to this one? | Only types named in a quote |
| Q5 | `nt_type` | What neurotransmitter does this type release, as stated by the sources, and which CL NT classes does that correspond to? | Inference from well-established facts allowed, with the inference stated in `sources[].method`. Keeps today's "always attempt NT", since NT drives candidate filtering |
| Q6 | `defining_markers` (alt: `neuropeptides`, `negative_markers`) | Which genes or gene products are reported as expressed by this type, and which are reported as absent? | `marker_type` from the `MarkerType` slice (`NOT_STATED`, `TRANSGENE_REPORTER`). Protein names are recorded as the source writes them; resolution is the code's job (§3.1) |
| Q7 | `morphology` | What soma, dendrite and axon morphology is described? | |
| Q8 | `electrophysiology` | What firing or intrinsic electrophysiological properties are described? | |
| Q9 | `synonyms` | What other names or abbreviations do the sources use for this type? | Each with the quote where the name is used |
| Q10 | `sex_bias` | Do the sources report a sex difference in cell number or marker expression? | Only when stated |
| Q11 | `at_source_sets` (alt: Q1's `prior_*`) | Does a cited source identify this type as a labelled set of cells or samples in a published dataset with a molecular readout? Which dataset, which labels exactly as given, which assay, and how does each set correspond? | **Usually a lead.** No accession or exact label → unplaced finding `dataset-lead`. Only AT-eligible assays go into the slot until #204 lands |
| Q12 | `definition_references` | Which papers establish or characterise this type? | Derived from the sources cited above; the top 3–5 |
| — | `cl_mapping` | *(Step 4, CL lookup, using OLS)* | `ingest_skip: set by CL lookup step` |
| — | `proposed_cl_term` | | `ingest_skip: cl-term-request workflow` |
| — | `notes` | | `ingest_skip: residual`. Only caveats and contradictions. A finding that answers a question goes to its slot or to unplaced findings |
| — | `id`, `name` | | `ingest_skip: set by identity step` |
| — | atlas slots (`atlas`, `taxonomy_*`, `cell_set_accession`, `n_cells`, `markers`, `merfish_markers`, `precomputed_expression`, …), `is_terminal`, `reference_stub` | | `ingest_skip: atlas / structural` |

Hierarchy (subtype or supertype) is not a node slot. It comes from the identity
step (§5 Step 3) and is written as edges (§6).

### 4.4 Slice generator

`src/evidencell/schema_slice.py`, behind the recipe `just schema-slice --class CellTypeNode --questions`.

- **Per question:** the slot description, range, required/multivalued flags,
  question, partial rule, and alternatives with their descriptions.
- **Per range class reached (one level by default):** its attribute
  descriptions, with enums expanded to permissible values and their
  descriptions.
- **Output:** compact markdown, deterministic and sorted, so the prompt diff is
  reviewable.
- **Budget:** about 7k tokens for the whole classical slice (#202 estimate).
  Per-question trimming is available if needed.
- **Tests:** golden-file test on a small fixture schema; coverage test (§4.1);
  slice-size guard.

---

## 5. Redrafted `asta-report-ingest`

```
PDF
 ├─ Step 1  deterministic parse                      (unchanged)
 ├─ Step 2  reference resolution + quote store merge (unchanged)
 ├─ Step 3  proposed types + IDENTITY RECONCILIATION (new; KB context)
 │          [GATE: identity]  default on (open question O1)
 ├─ Step 4  CL lookup                                (unchanged; skips MERGE targets already mapped)
 ├─ Step 5  schema-driven authoring, one subagent per node
 │          → kb/graphs/{region}/{node_id}.yaml (new or merged)
 │          → lit-to-lit hierarchy edges (§6)
 │          → answers_{node_id}.json + unplaced_findings.json
 ├─ Step 6  review: ingest-lint (code) + review subagent (fresh context)
 └─ Step 7  summary → PR; handoff to at-coverage / map-cell-type
```

### Step 3: proposed types and identity reconciliation (new)

**Input.**
- The PDF and extracted quotes, as today's Step 1b.
- **Region context** from a new recipe, `just region-context {region}`, built on
  the KB index (#163). It prints one line per canonical node:
  `id | name | synonyms | markers | locations | NT | CL term`. This is the code
  form of survey Step 0.
- **Cross-region candidates.** Nodes elsewhere in the KB that share the CL term
  or a synonym, so that a type ingested under another region is not duplicated.

**Subagent (thinking model).** For each type the report proposes, decide one of:

| Decision | Meaning | What Step 5 does |
|---|---|---|
| `NEW` | Not in the KB | Mint an id; write a new file |
| `MERGE_INTO: <id>` | Same type as an existing node | Edit the existing file: append sources; never rewrite or rename |
| `SUBTYPE_OF: <id>` | Proper subset of an existing node, or of another proposed node | New node, plus a hierarchy edge (§6) |
| `SUPERTYPE_OF: [<id>…]` | Broader than existing node(s) | New node; a hierarchy edge in each child's file (§6) |
| `OVERLAPS: [<id>…]` | Partial overlap, neither contains the other | Decide NEW or MERGE; the overlap goes to unplaced findings (no edge at ingest) |
| `OUT_OF_SCOPE` | Mentioned in passing, not characterised | Not written; listed in the summary |

Each decision carries a rationale and the quote_keys it rests on. Hierarchy
decisions *must* cite at least one quote that states the relation. Output:
`identity_decisions.json`, which replaces `proposed_types.json` as the step's
output.

**Gate.** The identity table is short, and it is the decision that is costly to
reverse. Recommendation: pause here by default and show the table, with
`gate: none` to skip. Today's optional end-of-run gate becomes redundant.

### Step 5: schema-driven authoring (replaces 3b; absorbs evidence-extraction)

One subagent per node, dispatched in parallel. Per-node dispatch keeps context
tight: slice (~7k tokens) + that node's quotes + the existing file when merging.
Reports propose 1–6 types, so the cost stays bounded.

**Each subagent gets:**
- the generated question slice (§4.4);
- its identity decision, and for `MERGE_INTO` the existing node file;
- the region's quotes added by this run (and, for merges, the quotes already
  cited on the node);
- the hierarchy convention (§6) when its decision is SUBTYPE_OF / SUPERTYPE_OF;
- a short workflow-policy block (one node per file, Write/Edit only, quote_keys
  only, no atlas mapping edges, merge = in-place Edit, skip refs already cited
  for the same property).

**It writes:**
- the node file, hook-validated on every write. "Write as much as the report
  supports": no 1–3 quotes-per-property cap, but no duplicate refs per
  property either;
- hierarchy edges in the child's file;
- `answers_{node_id}.json`, one entry per question:
  `{question, status: FILLED | NO_EVIDENCE | LEAD | UNPLACED, slots_written, quote_keys, note}`;
- unplaced findings appended to `unplaced_findings.json`, tagged by question
  (e.g. `multi-species`, `dataset-lead`, `connectivity`, `development`,
  `overlap`).

**Carried over from evidence-extraction:** synonyms (now Q9); the
fields-populated / no-evidence manifest (now `answers_*.json`); skipping refs
already on the node (merge dedup); and paper-quality signals, which become
`scope` content and `species`, not a filter. `at_source_sets` authoring is now
Q11.

### Step 6: review

**6a. `just ingest-lint {run_dir}` (code, new).** It reports and never edits:
- every quote cited in this run occurs in the report text (mechanical substring
  check);
- marker symbols resolve to atlas genes, after aliases, against the region's
  taxonomy DB gene list;
- `nt_type.cl_terms` is present, and `name_in_source` is compatible with the
  atlas NT vocabulary (until §3.1's code fix lands);
- anatomy ids resolve to MBA (directly or via a UBERON xref) for mouse nodes;
- nodes with `at_source_sets` have a `CLASSICAL_*` basis (at-coverage filter);
- every hierarchy-edge snippet is a verbatim substring of a stored quote from the
  cited ref (`node_diff.snippet_is_stored`), with the endpoint stub present;
- every question has an answer entry.

**6b. Review subagent (fresh context, Agent-dispatched).** For each node it gets
the slice, the node file, the dereferenced quotes, the identity decision and the
lint report. It checks:
- each source's quote supports the property it's attached to, including
  `marker_type` vs method and `scope` vs quote (the #196 audit is one instance);
- each identity / hierarchy decision is supported by its cited quotes;
- nothing in `notes` answers a question that has a slot.

It writes `review_report.md`. Findings go back to the authoring subagent for
**one** fix round, then to the PR.

**6c. ASTA-vs-paper faithfulness.** Not in the regular path unless the
quote-accuracy eval says it's needed.

### Step 7: summary and handoff

The PR summary carries:
- the identity table;
- per-node answer coverage;
- unplaced findings grouped by tag, which are input for schema-gap triage;
- dataset leads, which are input for the follow-up step in #204;
- the review report.

Handoff goes to `just at-coverage` → `map-cell-type`. Survey and
evidence-extraction drop out of the handoff.

---

## 6. Hierarchy convention (outside the schema)

This would live in `docs/lit_hierarchy_edges.md`, included in the Step 5 prompt
when a decision is SUBTYPE_OF / SUPERTYPE_OF. It writes down the convention the
11 existing edges already follow.

### 6.1 Rules

- **Direction:** child = `lit_type`, parent = `taxonomy_type`.
  `relationship: skos:broadMatch`, `mapping_cardinality: "1:n"`
  (refresh-predicates rule 1 agrees).
- **Location:** the edge lives in the **child's** file. If the parent is
  canonical elsewhere, the child's file carries a stub:
  `{id, name, definition_basis: <parent's real basis>, reference_stub: LIT_TYPE}`.
- **Edge id:** `edge_{child}_to_{parent}`.
- **Justification and confidence:** `mapping_justification:
  semapv:UnreviewedManualMapping`. `confidence` is a judgement on the quotes:
  HIGH for an explicit statement in two or more independent sources, MODERATE
  for one explicit statement, LOW for inference. The mapping rubric (AT F1,
  location bands) does not apply.
- **Evidence:** `LITERATURE` items with `reference` in PMID form. `snippet` must
  be copied verbatim from a stored quote's text (lint checks this). A short
  `explanation` states the relation. `supports: SUPPORT`.
- **SAME_AS is not an edge.** It's a merge.
- **No overlap edges at ingest.** Overlaps go to unplaced findings; a curator
  decides later.
- **New parent and children from the same report:** each gets its own file, and
  each child file stubs the parent.

### 6.2 Out of scope for now

`quote_key` on `LiteratureEvidence`, `owl:SubClassOf` semantics, and a subtype
slot all stay with #183. The cost of not doing them is accepted for now:
hierarchy edges borrow mapping semantics, and their snippets are checked by lint
and review rather than by the hook.

### 6.3 Downstream fixes the convention needs

The convention is usable today but renders badly. Small, independent dev fixes:

- **Stubs treated as classical nodes:** `render._classical_nodes` should exclude
  `reference_stub` nodes. Today they produce empty `{stub}_summary.md` files
  and extra index rows.
- **Hierarchy shown as mapping:** lit-to-lit edges should appear in a
  "Hierarchy" section of gen-facts and reports, not as atlas mapping candidates.
  The parent side should list its children, which needs a reverse lookup by
  `taxonomy_type` in `kb_index`.
- **`gen-toc` drops them:** show them, or document the omission.
- **`rationale_writeback` closeMatch edges:** they don't add a `LIT_TYPE` stub
  for the far endpoint, so they fail structural checks when it's canonical in
  another file.
- **Mapping consumers:** should explicitly skip edges whose `taxonomy_type` is
  not an atlas node, rather than relying on the absence of AT metrics.

---

## 7. Deprecation and documentation

Both files stay as material to reuse; Step 5 now covers their roles.

- `workflows/survey.md` and `workflows/evidence-extraction.md` get a status
  banner: deprecated / on hold, why, which parts were reused where, and that
  they are the starting point if ASTA API search returns.
- `asta-report-ingest.md` is redrafted per §5. The "Known gap: cross-report
  node identity" section is deleted because Step 3 closes it.
- `CLAUDE.md` overview table, inputs table and typical-workflow diagram, plus
  `WORKFLOW.md`, are updated in the same PR.

---

## 8. Downstream bugs found by the survey (file separately)

These are independent of this design, but several of them make ingested content
invisible, so they should land early.

| Bug | Where | Effect |
|---|---|---|
| gen-facts reads `morphology_notes` / `electrophysiology_class`, which were removed in v0.8.0 | `render.py:1626-1627` | Morphology and ephys always empty in facts, reports and the cl-term-request workflow |
| gen-facts ignores `compartment` | `render.py` soma location | Axon targets shown as soma locations |
| find-candidates has no marker alias resolution (emit-stage-b has it) | `taxonomy_db.py` | Protein-named markers missed at retrieval but scored later |
| find-candidates filters on verbatim `nt_type.name_in_source` | `taxonomy_db.py:2721` | Wording-dependent candidate loss. Should use `cl_terms` |
| at-coverage skips non-`CLASSICAL*` nodes | `at_metrics.py:1242` | Declared correspondences on other bases silently ignored |
| Species never checked against atlas species | find-candidates | Rat or human nodes scored against the mouse atlas without warning |
| gen-facts omits `synonyms`, `species`, `nt_type.cl_terms`, `definition_references` | `render.py` | cl-term-request grounds on gen-facts and cannot see them |
| `orphan_node` WARN fires on every freshly ingested node | `qc_content.py` | Noise. Exempt nodes with no mapping yet, or downgrade to INFO |

---

## 9. Implementation sequence

| PR | Content | Depends on |
|---|---|---|
| **A** | Description cleanup (#202 prerequisite) plus §3.1 description fixes: anatomy preference into `AnatomicalLocation`, a `definition_basis` description, a `species` rule. Lint test for history text | — |
| **B** | Downstream fixes, part 1: gen-facts stale keys + compartment; find-candidates alias resolution + NT filter on `cl_terms`; stub/lit-to-lit rendering (§6.3) | — (parallel with A) |
| **C** | Question annotations on all `CellTypeNode` slots; coverage test; `schema_slice.py` + `just schema-slice` + tests | A |
| **D** | `just region-context` (KB index), `just ingest-lint`, hierarchy convention doc | C (lint reads the answer files) |
| **Experiment** | Re-run PVT_Glut on a scratch branch with the redrafted workflow. Before/after: share of labelled `notes` paragraphs matching an existing slot; `species` / `synonyms` fill rate; `marker_type` honesty; identity decisions vs what the curator did by hand in #200 | B, C, D |
| **E** | Redrafted `asta-report-ingest.md`; deprecation banners; CLAUDE.md / WORKFLOW.md | Experiment |
| **parallel** | ASTA quote-accuracy eval (decides 6c) | — |

---

## 10. Open questions

- **O1 — identity gate default.** On by default (recommended: cheap to review,
  costly to reverse), or PR review only?
- **O2 — authoring granularity.** One subagent per node (recommended) or one
  batched subagent? The experiment can compare cost and quality.
- **O3 — where unplaced findings live.** A per-run `research/` artefact
  (recommended for now) or a node slot later?
- **O4 — `species` cardinality.** The experiment's `multi-species` count decides
  between multivalued and splitting pooled nodes.
- **O5 — lint → hook.** Should any ingest-lint check become a pre-edit hook check
  (e.g. hierarchy-edge snippet against the store) before #183 adds
  `quote_key` to edge evidence?
- **O6 — cross-region identity.** How wide should Step 3's candidate search be?
  Matching CL term or synonym across all regions is proposed; the KB index makes
  it cheap.

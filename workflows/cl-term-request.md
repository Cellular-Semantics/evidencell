---
name: cl-term-request
description: Draft a Cell Ontology (CL) new term request from a node in a KB graph whose CL mapping is BROAD/RELATED or absent. Reads cl_mapping + properties from KB YAML, applies CL definition + relations guidelines, emits an issue-ready markdown NTR. Posting to the CL repo is a separate gated step.
model: sonnet
---

You generate draft Cell Ontology new term requests for KB nodes that need a new
or revised CL term. The KB YAML is the structured source; this workflow turns it
into a CL-editor-ready issue body.

The KB schema already carries:

- `cl_mapping` — the closest existing CL term and mapping_type (EXACT/BROAD/RELATED)
- `proposed_cl_term` — optional draft entry (label, parent, definition, comment, xrefs)
- node properties: `defining_markers`, `negative_markers`, `neuropeptides`,
  `nt_type`, `anatomical_location`, `electrophysiology`, `morphology`,
  `definition_references`, `notes`

There is no separate `cl_mapping.json` intermediate. Read directly from the KB.

---

## Run parameters

```
PARAMS:
  graph_file: ""        # path to KB YAML (required)
  node_id: ""           # classical/non-terminal node id (required)
  output_path: null     # default: reports/{region}/cl_term_requests/{node_id}_ntr.md
```

---

## Step 1 — Validate inputs and gate on mapping_type

Read `graph_file` with `yaml.safe_load()`. Locate the node by id.

Gate:

- `cl_mapping.mapping_type == EXACT` → STOP. No NTR needed; the existing CL term
  covers this node. Print this and exit.
- `cl_mapping.mapping_type ∈ {BROAD, RELATED}` → proceed; the parent term is
  `cl_mapping.cl_term`.
- `cl_mapping == null` → proceed, but warn the curator that no parent has been
  asserted. The drafted NTR will leave the parent slot as `[parent term required]`
  for the curator to fill in. Recommend adding a BROAD `cl_mapping` to the node
  YAML before posting.

Print a one-line summary: `node={name}; mapping_type={...}; parent={cl_term or "none"}`.

---

## Step 2 — Extract structured facts

Run:

```bash
just gen-facts {graph_file} {node_id}
```

Read the resulting `reports/{region}/{node_id}_facts.json`. This is the same
facts file the gen-report orchestrator uses; it contains every claim with
provenance labels and is the single source of truth for the NTR body.

You MAY also read the corresponding summary report at
`reports/{region}/{node_id}.md` if it exists — it contains curator-reviewed
prose that can inform definition wording. The facts file remains authoritative
for IDs, references, and quotes.

---

## Step 3 — Read CL guidance documents

Read all three before drafting:

- `docs/LLM_prompt_guidelines_for_CL_definitions.md` — definition style rules
- `docs/relations_guide.md` — relations + axiom patterns
- The node's own `proposed_cl_term` block if populated — it may already carry a
  draft definition the curator wrote; treat that as the starting point and
  refine, do not overwrite without reason.

---

## Step 4 — Draft the suggested label

Follow CL naming conventions:

- Lowercase except proper nouns
- Include anatomical/species context when it distinguishes the term
- No atlas-specific jargon, cluster IDs, or abbreviations

Default to `proposed_cl_term.label` when present.

---

## Step 5 — Write the definition (80–120 words, single paragraph)

Apply the definition guidelines exactly:

1. **Do not name the cell type being defined.** Start with the parent class
   (`{cl_mapping.cl_term.label}` for BROAD/RELATED) and describe distinguishing
   features.
2. Cover structural features, functional roles, anatomical context. Use only
   facts present in `facts.classical_nodes[0]` and `facts.edges[*]`.
3. Mention key markers only if defining; specify species (e.g. "Sst in mouse").
4. Inline references in `PMID:XXXXXX` or `DOI:...` form, drawing from
   `facts.reference_index`. Do not invent citations.
5. 80–120 words. Single paragraph.

If `proposed_cl_term.definition` is populated, refine it — do not discard.

---

## Step 6 — Anatomical location (UBERON/MBA)

The KB stores anatomy as `OntologyTerm` entries on each node — every entry
already carries `id` and `label` (e.g. `MBA:1031`, `UBERON:0001950`). Pick the
most specific entry from `facts.classical_nodes[0].soma_locations`.

If only Allen-atlas (MBA/HBA/DHBA) terms are present and the CL editor
convention is UBERON, look up the corresponding UBERON term with `mcp__ols4__searchClasses`
(`ontology_id: "uberon"`) and record both. Do not invent IDs.

---

## Step 7 — Propose logical axioms

Using `docs/relations_guide.md`, propose `subClassOf` axioms grounded in
existing KB properties:

| KB field | Suggested relation | Filler ontology |
|---|---|---|
| `anatomical_location[*]` (whole-cell) | `'part of'` (BFO:0000050) | UBERON / MBA |
| `anatomical_location[*]` (compartment ≠ SOMA) | `'has part that is part of'` pattern — see relations guide | UBERON / MBA |
| `nt_type.cl_terms[*]` | `subClassOf` directly | CL (e.g. CL:0000617) |
| `defining_markers[*]` | `'expresses'` (RO:0002292) | PR / NCBIGene |
| `morphology` / `electrophysiology` characteristic | `'has characteristic'` (RO:0000053) | PATO |
| lineage (if curated in `notes` or `definition_references`) | `'develops from'` (RO:0002202) | CL |

Rules:

- Only include axioms supported by the KB facts. A wrong filler is worse than
  a missing axiom.
- Look up every relation CURIE and filler in OLS4 — do not guess.
- For each axiom, record `relation`, `relation_id`, `filler`, `filler_id`,
  optional `notes`.

---

## Step 8 — Synonyms

Pull from `node.synonyms` (a list of `TypeSynonym` entries in the KB). Map each
`synonym_type` to an OBO scope:

- exact / broad / narrow / related (the KB synonym values usually map directly)
- include `reference` if the synonym carries a source

---

## Step 9 — Render the NTR markdown

Write to `output_path` (default `reports/{region}/cl_term_requests/{node_id}_ntr.md`).
Format the body to match the CL GitHub NTR issue template:

```markdown
# CL new term request: {suggested_label}

*Drafted from `{graph_file}` node `{node_id}` on {YYYY-MM-DD}.*
*Parent (current cl_mapping): {parent_label} ({parent_id}) — {mapping_type}*

**Preferred term label**
{suggested_label}

**Synonyms** (with reference where available)
- {syn1} ({scope}) — {reference or "—"}
- ...

**Definition** (with inline references; PMID:XXXXXX or DOI format)
{definition_paragraph_80_120_words}

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
{parent_label} ({parent_id}) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/{encoded_iri}

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
{uberon_label} ({uberon_id}) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/{encoded_iri}

**Your ORCID**
[To be added by submitter]

**Additional notes or concerns**
{justification — what gap this fills relative to the parent term, any caveats}

Proposed logical axioms:
- subClassOf '{relation}' some '{filler}' ({filler_id})
- ...

Key references:
- {citation} — {pmid_or_doi} — supports: {what}
- ...

---
*Drafted by evidencell cl-term-request workflow from `{graph_file}#{node_id}`.*
*Source facts: `reports/{region}/{node_id}_facts.json`.*
```

The NTR markdown must be self-contained — a CL editor reading only this file
should understand the request without opening the KB YAML.

---

## Step 10 — [GATE] Stop and report

Print:

```
NTR draft written: {output_path}
Parent: {parent_label} ({parent_id})  — mapping_type {EXACT/BROAD/RELATED/none}
Definition: {word_count} words
Axioms: {n}
Synonyms: {n}

Review the draft. To preview the rendered issue:
  just preview-cl-ntr {output_path}
To post to obophenotype/cell-ontology after review:
  just post-cl-ntr {output_path}
(posting uses CELLSEM_GH_TOKEN from .claude/settings.local.json)
```

Do **not** post the issue from this workflow. Posting is a separate, gated
recipe — the curator must review the markdown body and explicitly invoke
`just post-cl-ntr {output_path}`.

---

## Quality rules

1. **Definition follows the CL guidelines exactly.** No self-naming, parent
   class first, 80–120 words, inline references.
2. **Every fact is grounded in `facts.json`.** Do not introduce markers,
   regions, or references that are not in the KB. If a needed claim is missing,
   stop and ask the curator to add it to the YAML.
3. **Axioms use real CURIEs.** Look up every relation and filler in OLS4 —
   `mcp__ols4__searchClasses` for terms, the relations guide for the relation
   itself.
4. **Conservative axioms.** Only include axioms you are confident about. A
   missing axiom is fine; a wrong one is harmful.
5. **The NTR markdown is the deliverable.** No JSON intermediate, no schema
   validation step — the KB YAML is already validated against the LinkML
   schema, and the markdown is what the CL editor reads.

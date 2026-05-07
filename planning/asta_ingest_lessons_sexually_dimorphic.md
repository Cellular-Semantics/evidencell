# ASTA Ingest Lessons — sexually_dimorphic pilot run (2026-04-25)

Issues and improvements identified during the first full run of `asta-report-ingest`
on a sexually dimorphic neuron report. Covers the ingest pipeline, validation hook
failures, and structural workflow gaps.

---

## 1. References.json PMID format bug

**What happened:** The references resolution agent (Step 2) stored PMIDs as
`"pmid": "PMID:29201072"` (with the `PMID:` prefix). The validation hook
(`validate.py:check_ref_pmids`) strips the prefix from YAML `ref:` values and
looks up bare digits, so the lookup always failed — every PMID cite in the KB YAML
was rejected.

**Fix applied:** Strip the `PMID:` prefix from all `pmid` values in
`references/sexually_dimorphic/references.json` (one-off Python patch; 38 entries
fixed).

**Root cause:** The resolution agent prompt doesn't specify a canonical PMID format.
The hook expects bare digits; the agent inferred the prefixed form.

**Dev request:** Update the Step 2 agent prompt (or the references resolution
template) to explicitly specify `"pmid": "<digits-only>"` (no prefix). Consider
adding a post-ingest normalisation step that validates and strips prefixes from
all fields in references.json before any KB writes are attempted.

---

## 2. References.json DOI format inconsistency

**What happened:** DOIs were stored as `"doi": "DOI:10.1007/s12031-012-9923-1"`
(with the `DOI:` prefix). The hook's lookup builds a set from `entry.get("doi")`
verbatim, so the set contains `"doi:10.1007/..."` (lowercased). If a YAML `ref:`
field uses `DOI:10.1007/...` format, the regex extracts `10.1007/...` and the
lookup fails for the same reason as the PMID issue.

**Why it didn't block this run:** All DOI refs in the KB YAML used the full URL
form (`https://doi.org/...`) — the hook's `_DOI_RE` only matches strings starting
with `DOI:`, so https:// refs are silently skipped. This is a latent bug: if future
nodes cite papers with `DOI:` prefix refs, they will fail validation even though
the entry is present in references.json.

**Dev request:** Normalise DOI storage in references.json to bare path format
(`10.XXXX/...`) and update `check_ref_pmids` to handle https://doi.org/ refs in
addition to the `DOI:` prefix form. The YAML convention should also be standardised
— either always use `DOI:` prefix or always use the URL form.

---

## 3. Conference abstract identification needs a formal filter step

**What happened:** Three corpus entries in the references store were conference
abstracts (Endocrine Society annual meeting), identified by DOI pattern
`jendso/bv*` and absence of a PMID. The ASTA report drew on these abstracts and
the Step 3b agent faithfully included nodes and property sources citing them.

The filter (drop nodes whose primary evidence is abstract-only) was applied
manually at Step 4 / GATE rather than being automated.

**Excluded nodes:**
- `bnst_kiss1_neuron` — sex bias quantification (`139.4 vs 43.70 cells`) was
  abstract-only (Zdon 2024, jendso/bvae163.1280)
- `lateral_septum_kiss1_neuron` — entire characterisation was abstract-only
  (Zdon 2025, jendso/bvaf149.1673)

**Improvement:** Add an optional sub-step between Step 2 (references) and Step 3b
(KB draft), or explicitly at Step 3b, that:
1. Flags corpus entries matching abstract-DOI patterns (`jendso/bv*`, `JS.YYYY-*`,
   no PMID) in the paper catalogue.
2. Propagates the flag to any proposed node whose *sole* supporting evidence comes
   from abstract-only corpus entries.
3. At the Step 4 GATE, surface flagged nodes as "ABSTRACT-ONLY — confirm whether
   to include or hold".

This avoids silently including poorly substantiated types in the KB draft and makes
the curation decision explicit.

---

## 4. Non-dimorphic nodes in a "sexually dimorphic" ingest

**What happened:** `arc_kndy_neuron` was included in the proposed KB because it
appears in the report as a reference population — but the report itself states it is
NOT sexually dimorphic in cell number. The Step 3b agent correctly described this in
the notes, but the node still entered the draft.

Similarly `mpoa_galanin_neuron` had no quantified sex ratio and `poa_pacap_vip_neuron`
was fish-only evidence with mammalian homology assumed.

**Improvement:** The GATE prompt (Step 4) for topically-scoped ingests (e.g.
"sexually dimorphic survey") should include an explicit qualifier check:

> "For each proposed node, does it exhibit a quantified sex bias in cell number,
> marker expression, or electrophysiology supported by peer-reviewed literature?
> If not, mark as EXCLUDE with reason."

This surfaces the filter decision to the curator at the right point rather than
requiring post-hoc manual pruning.

---

## 5. Monolithic KB draft vs. per-node draft files

**What happened:** Step 3b wrote all 14 proposed nodes into a single
`proposed_kb_sexually_dimorphic.yaml`. The GATE then selected 9 qualifying nodes,
requiring a filtered version to be written to `kb/draft/`.

This is workable but slightly awkward: the proposed KB contains nodes that will
never enter the KB, creating a divergence between the research artifact and the
actual KB.

**Improvement options (trade-offs):**
- Keep monolithic proposed KB (current) — simple, single file, but contains noise.
- Write per-node proposed files, assemble into KB only after GATE — more modular,
  better traceability, but more files.
- Add a `kb_status: EXCLUDED | INCLUDED` field on each node in the proposed KB —
  low overhead, self-documenting.

Recommendation: the `kb_status` field approach is cheapest and keeps the research
artifact intact. The actual KB file only contains INCLUDED nodes.

---

## 6. Rate limits on Step 3b opus subagent

**What happened:** The Step 3b subagent hit a rate limit mid-run on the 14-node
batch. However it had already completed writing both output files before the limit.
No data was lost.

**Risk:** If the limit hits before file writes complete, partial output could be
written. The proposed KB file has no checksum or completion marker.

**Improvement:** Step 3b could write a `step3b_complete: true` flag at the top of
the proposed KB (or a separate sentinel file) only after all nodes are written.
The orchestrator checks for this flag before proceeding to Step 4.

---

## 7. `nt_type` missing from some nodes

Several nodes were written without an `nt_type` field (e.g. `sdn_poa_calbindin_neuron`,
`bnst_crf_neuron`). The schema allows this but the `find-candidates` DB query uses
NT type as a scoring dimension — missing NT type means no NT-match score, weakening
candidate retrieval in map-cell-type.

**Improvement:** At Step 3b, instruct the agent to always attempt to resolve NT type
from the literature even if not directly stated (e.g. BNST CRF neurons are GABAergic
— this is well-established and can be inferred). If unresolvable, note explicitly
in the node's `notes` field why NT type is omitted, so the mapper knows to query
without it.

---

## 8. MBA term assignment for subnuclei

Several nodes used the parent MBA term (e.g. `MBA:464` for both SDN-POA and MPOA,
`MBA:174` for dlBNST, ovBNST, and alBNST) because dedicated child terms don't exist
in the Allen MBA ontology at the resolution of classical subnuclei.

This means `find-candidates` anatomy scoring will match these nodes broadly against
any cluster in the parent structure, which is correct but may generate false positives.

**Improvement:** Document in node `notes` when an MBA term is provisional (parent
substituted for a non-existent subnucleus term). The map-cell-type Step 0b
refinement subagent should be instructed to treat adjacent-subregion matches
cautiously for these nodes.

---

## Workflow step that works well

Step 2 (references resolution with full-text retrieval + quote extraction) produced
a high-quality reference store: 46 corpus entries, 98 quotes, with clean provenance.
The content-hashed quote key system worked correctly — no duplicate keys across the
batch. The `pdf_corpus_ids.json` → `references.json` path is solid.

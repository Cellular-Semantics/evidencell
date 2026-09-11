# Handoff plan — minimal ASTA ingest for `trilaminar_cell_hippocampus`

*Written 2026-09-11 by a curation session that lacked the Asta Semantic Scholar MCP.*
*Target: a fresh session that HAS `mcp__Asta_semanticscholar__*` available.*
*Scope deliberately narrow: update `references/hippocampus/references.json` and rewrite ONE KB node. Nothing else.*

---

## 0. Context — what already happened

- **Input report:** `inputs/deepsearch/trilaminar_hippocampal_cells.pdf` (17 pp, untracked).
- **Reference resolution is already done.** `trilaminar_reference_resolution.txt` at repo root holds a corpus-ID → DOI/PMID table for all
  18 corpus IDs linked from the PDF, resolved via the Asta MCP `get_paper_batch` on 2026-09-11. **Read it first —
  do not redo the resolution.** It also records which quoted passages cite Sik et al. 1995.
- **A CL new term request has already been filed** from this report:
  [obophenotype/cell-ontology#3744](https://github.com/obophenotype/cell-ontology/issues/3744)
  — "CL new term request: hippocampal trilaminar cell". Draft retained at
  `reports/hippocampus/cl_term_requests/trilaminar_cell_hippocampus_ntr.md`.
  **The KB node must end up consistent with what that issue asserts.** If you find a reason to diverge,
  say so rather than silently differing — the issue is public and may need a follow-up comment.
- **The KB node has NOT been touched.** It still contains the two defects this ingest exists to fix.

### Why this is a minimal ingest, not a full `asta-report-ingest` run

`workflows/asta-report-ingest.md` is 745 lines, 5 steps, 3 subagents. Most of it does not apply:

| Step | Action |
|---|---|
| 1 — deterministic PDF extraction | **RUN IT** |
| 1b — proposed-types subagent | **SKIP** — the node already exists; no new types are being proposed |
| 2 — reference resolution | **HALF** — resolution is done (`trilaminar_reference_resolution.txt`); run only the quote-merge half |
| 3 — CL lookup subagent | **SKIP** — done, NTR #3744 filed |
| 3b — quote→property matching | **RUN, narrowed to one node** |
| 4 — `[GATE]` human review | **RUN** — but it is now a small diff review |
| 5 — handoff options | **SKIP** |

---

## 1. Hard rules

1. **Never hand-edit `references/hippocampus/references.json`.** Always go through
   `src/evidencell/references.py::write_quote_to_refs()`. It is idempotent, computes the content-hashed
   `{corpus_id}_{sha256[:8]}` key, and builds the paper entry via `_build_paper_entry()` so the field shape
   is enforced in code. The orchestrator's Step 2 currently has a subagent merging this JSON by hand and
   the workflow itself records the result: *"Three prior pilots have shipped wrong field shapes here …
   every one was caught only after KB writes started failing."* Do not become the fourth.
2. **Do not edit the big graph YAML by hand either.** Write a single-node fragment, then fold it in with a
   driver. See §4.
3. **Curation mode is in force.** Writable: `kb/graphs/**`, `references/**`, `reports/**`, `research/**`,
   `planning/content-notes/**`. Out of scope: `src/`, `schema/`, `justfile`, `.claude/`, `workflows/`.
   New drivers therefore go in `research/_drivers/` (which is writable), NOT `src/`. Promoting them to
   `src/` + a `just` recipe is a later dev-mode task.
4. **No schema changes.** If something seems to need one, stop and file a dev-request issue.

---

## 2. Step 1 — deterministic extraction

```bash
uv run python -m evidencell.extract_asta_report \
    inputs/deepsearch/trilaminar_hippocampal_cells.pdf \
    --output-dir research/hippocampus/trilaminar_20260911/ --pretty
```

Writes `extracted_quotes.json` (quotes keyed by author_key), `reference_list.json`, `pdf_corpus_ids.json`.
Seconds, no LLM. Sanity-check the counts; if `total_quotes == 0` or `total_papers < 3` the PDF layout
differs from expectation — fall back to reading the PDF directly (same output shape).

---

## 3. Step 2 — reference merge

> **CORRECTION (2026-09-11, after this plan was first written).** This section originally assumed the
> Asta Semantic Scholar MCP was required. **It is not.** The only missing metadata was author lists, and
> Europe PMC supplies them: `mcp__artl-mcp__get_europepmc_paper_by_id` returns full author lists with
> separate `firstName`/`lastName` — verified on PMID:32016558 (Katona 2020) and, by bare DOI, on the
> bioRxiv-only record `10.1101/431957` (Qian 2018). So use an 18-call loop over
> `get_europepmc_paper_by_id` instead of one `get_paper_batch`; there is no Asta dependency.
>
> Europe PMC also returns `commentCorrectionList` preprint→published links, which resolves both
> "DOI-only" caveats below: **Qian et al. 2018 was published as *Nature Methods* 17(1):101–106,
> PMID:31740815**, and Hewitt's preprint duplicates PMID:33991454. Prefer the published records.
>
> The `get_paper_batch` instruction in 3a is retained below only as a fallback for a session that does
> have Asta. Everything about field shapes, the author-extraction trap, and §3b onward is unaffected.

### 3a. Author resolution (fallback: Asta batch call)

`write_quote_to_refs()` takes `paper_meta` with `title, year, authors, pmid, doi, author_keys,
resolution_confidence`. **`trilaminar_reference_resolution.txt` has everything except `authors`.** Author shape has broken this
pipeline before — see `planning/minirefs_author_rendering_fix.md` and
`planning/asta_ingest_lessons_sexually_dimorphic.md` §1–2 — hence `_normalise_authors()`.

Make ONE batch call to fill the gap:

```
mcp__Asta_semanticscholar__get_paper_batch(
    ids=[<the 18 corpus IDs from trilaminar_reference_resolution.txt>],
    fields="title,authors,year,externalIds"
)
```

`authors` comes back as `[{"authorId": ..., "name": ...}, ...]`. **Extract `name` from each dict into a
list of full-name strings.** Do not comma-join into one string; do not append "et al.".

Two records are bioRxiv-only and may return no PMID — that is expected, not an error:
- `232081762` Hewitt et al. 2021 preprint — DOI `10.1101/2021.02.26.433114`
- `92215919` Qian et al. 2018 — DOI `10.1101/431957`

Note also: `232081762` and `234597703` are the preprint and published versions of the **same** Hewitt
paper; the report treats them as separate references ("Hewitt et al." / "Hewitt et al._1"). Prefer the
published record (`234597703`, PMID:33991454) for citation; keep the preprint only if a quote is unique to it.

### 3b. Then write a driver, not manual edits

Put it at `research/_drivers/merge_trilaminar_refs.py`. It should:

1. Load `extracted_quotes.json`, `trilaminar_reference_resolution.txt`'s resolution table (or a small JSON you derive from it), and the
   author data from the batch call.
2. For each quote, call:
   ```python
   write_quote_to_refs(
       refs_path=Path("references/hippocampus/references.json"),
       corpus_id=<digits only, no prefix>,
       quote_text=<verbatim>,
       section=<report section heading>,
       source_method="asta_report",
       added_by="asta_ingest_trilaminar_20260911",
       paper_meta={...},
   )
   ```
3. Support `--dry-run` (report what would be added) and be safely re-runnable.

Field-shape contract, for the `paper_meta` you pass: `pmid` is digits only (**no `PMID:` prefix**), `doi` is
the bare path (**no `DOI:` prefix, no `https://`**), `author_keys` is a list, `authors` is a list of full-name
strings.

### 3c. Expected scale

**4 of 18 corpus IDs are already in `references.json`** — leave them alone beyond quote merging:

| Corpus ID | Paper | PMID |
|---|---|---|
| `10664418` | Sik et al. 1995 | 7472426 |
| `234597703` | Hewitt et al. 2021 (published) | 33991454 |
| `42026795` | Harris et al. 2017 | 29912866 |
| `4934764` | Katona et al. 2017 | 27997999 |

The other **14 are new**, including the two papers carrying most of the definition:
**Ferraguti et al. 2005 (PMID:16280590)** and **Katona et al. 2020 (PMID:32016558)**.

### 3d. Three sources to down-weight

These are retrieval false positives or incidental mentions. Ingest their quotes if you like, but do **not**
let them drive property assertions:

- `9667774` Meskenaite et al. 2016 (PMID:27445724) — **homing pigeon** neurogenesis; uses "trilaminar
  complex" for a *brain region*, unrelated to this cell type. The report's entire opening section is built
  on this and is spurious.
- `6963749` Kaliszewski et al. 2016 (PMID:28066183) — SOD1 acetylation; one incidental list mention.
- `289175303` Li et al. 2026 (PMID:42268975) — Rett syndrome snRNA-seq. Genuinely useful for the
  Chrm2/Gad2 colocalisation and the two-morphology observation; not a trilaminar-cell paper.

---

## 4. Step 3 — rewrite the KB node

**Target:** node `trilaminar_cell_hippocampus` in
`kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml` (~line 1669 for `definition_references`).

### 4a. This is a REPLACE, not an additive merge

The existing merge precedent, `research/_drivers/merge_ingest_into_mapping.py::merge_node()`, **unions**
fields — it has no removal path. Two required changes are *deletions*, so a union would silently preserve
the bad data:

- **`Pvalb` must leave `defining_markers`.** It is wrong. Parvalbumin appears in this literature as a marker
  of this cell type's postsynaptic **targets** ("a strong bias towards interneurons as targets, including
  parvalbumin-expressing cells" — Katona et al. 2020), and the associated transcriptomic cluster is
  explicitly *Pvalb-negative*. It almost certainly entered the node as a target-read-as-marker extraction
  error. It moves to `negative_markers`.
- **`PMID:28646648` must leave `definition_references`.** It is the node's ONLY current reference and it is an
  orphan: absent from `references.json`, and matching none of the 18 corpus IDs in `trilaminar_reference_resolution.txt`. (An earlier
  session guessed it was Katona et al. 2017 — it is not; that paper is PMID:27997999.) Replace, don't augment.

So: **delete the existing node, insert the rewritten one.** Write
`research/hippocampus/trilaminar_20260911/fragment_trilaminar_cell_hippocampus.yaml` as a *standalone,
schema-valid* single-node document, then fold with a driver
(`research/_drivers/fold_node_fragment.py`) that:

1. locates the node by `id` in the target graph,
2. **removes** it,
3. inserts the fragment's node in the same list position,
4. leaves every other node and all edges untouched,
5. uses `ruamel.yaml` with `preserve_quotes=True`, `width=4096`, `indent(mapping=2, sequence=4, offset=2)`
   — matching `merge_ingest_into_mapping.py` so the diff stays minimal,
6. supports `--dry-run` and prints a unified diff.

**Shape the fragment as a valid standalone per-cell-type file.** The next planned refactor splits the KB into
one file per cell type; if the fragment is already a valid standalone document (proper header + one node),
that refactor becomes a `git mv` plus deleting the fold driver, rather than a rewrite. Do not invest in
clever merge semantics that are about to become dead code.

### 4b. Current node state (the "before")

```yaml
id: trilaminar_cell_hippocampus
name: Trilaminar cell
definition_basis: CLASSICAL_MULTIMODAL
species: null
anatomical_location:                      # 1 entry; its only source is a quote that does NOT support it
  - id: UBERON:0014552                    #   "The group of unlabeled interneurons recorded in stratum
    compartment: SOMA                     #    oriens MAY INCLUDE O-LM cells, horizontal bistratified,
                                          #    basket and axo-axonic cells and various long-range
                                          #    projecting GABAergic cell types" — a statement of ambiguity
nt_type: {name_in_source: GABAergic, cl_terms: [CL:0000617], sources: []}   # sources EMPTY
defining_markers:  [Pvalb, M2R]           # NO sources on either; Pvalb is WRONG
negative_markers:  [Sst]                  # NO sources
neuropeptides: []
cl_mapping: null
definition_references: [PMID:28646648]    # orphan — see 4a
is_terminal: false
notes: 'Stub from cite-traverse (2026-04-10). ...'
morphology:        {description: ...}     # NO sources
electrophysiology: {description: ...}     # NO sources
```

Essentially every assertion on this node is currently unsourced. That is what the ingest fixes.

### 4c. Target node content

All property blocks get `sources` with `ref` + `method` + `scope` + `quote_key`. **Fill `quote_key` from
`extracted_quotes.json` / the keys returned by `write_quote_to_refs()` — never invent one.** The pre-edit hook
rejects any `quote_key` or PMID not in `references.json`, so §3 must complete before this write.

- **`name`** — keep `Trilaminar cell`. Consider `synonyms`: `hippocampal trilaminar cell`,
  `CA1 trilaminar cell` (matching NTR #3744's proposed label).
- **`species`** — leave `null`. Morphology/physiology is rat (Sik, Ferraguti, Jinno, Katona); Li et al. is
  mouse; Katona et al. 2020 reports the molecular phenotype in both.
- **`anatomical_location`** — expand from 1 entry to 5, and **replace the non-supporting source**:
  | UBERON | label | compartment |
  |---|---|---|
  | `UBERON:0014552` | CA1 stratum oriens | `SOMA` (soma at oriens/alveus border) |
  | `UBERON:0014552` | CA1 stratum oriens | `AXON_TARGET` |
  | `UBERON:0014548` | pyramidal layer of CA1 | `AXON_TARGET` |
  | `UBERON:0014554` | CA1 stratum radiatum | `AXON_TARGET` |
  | `UBERON:0002191` | subiculum | `AXON_TARGET` (the long-range projection) |

  The three CA1 strata *are* the "trilaminar" differentia — encode them, don't leave them in prose.
  All five UBERON IDs verified present in the cached OAK uberon.db.
- **`nt_type`** — keep GABAergic / `CL:0000617`; **add** sources: Sik et al. 1995 (symmetric synapses at EM)
  and Li et al. 2026 (Chrm2 colocalises with Gad2).
- **`defining_markers`** — `Chrm2` (use the gene symbol; `M2R` is the protein alias) sourced to Ferraguti
  2005 / Jinno 2007 / Katona 2020 / Li 2026. Optionally `Ntng1` sourced to Katona 2020 via Harris 2017 —
  but mark it tentative in `notes`: it rests on a transcriptomic cluster Katona et al. describe as
  *"similar to"* this type, not a measurement on identified cells. **`Pvalb` is deleted.**
- **`negative_markers`** — `Sst`, `Pvalb`, `Vip`, `Npy`, `Calb1`, all `modifier: ABSENT`, sourced to
  Jinno 2007 and Katona 2020.
- **`neuropeptides`** — `[]`. These cells specifically *lack* NPY; that is a differentia against VIP-LRP cells.
- **`morphology`** — rewrite. Soma oblong/elongated at the oriens/alveus border; dendrites largely confined to
  stratum oriens (horizontal in the classic description, radial variants reported); the defining mismatch
  between a restricted dendritic tree and a broad three-layer axonal arbor; axon >3.3 mm rostrocaudally,
  densest in oriens, with an extensive caudal projection through the alveus branching across all layers of
  the subiculum. Quantitative detail available: dendritic field ~930 µm mediolateral × 1500 µm
  anteroposterior (Ferraguti 2005); axon ~56,000 µm with 15,767 boutons distributed oriens 12.8% /
  pyramidale 16.7% / radiatum 68.4%, up to 19% of synapses onto pyramidal somata (Booker & Vida 2018).
- **`electrophysiology`** — rewrite. State-dependent: complex spike bursts during theta, strong discharge
  during sharp-wave/ripple events (Ferraguti 2005); in freely moving rats, **reduced** firing during movement
  with prolonged bursts **>200 Hz** during slow-wave sleep (Katona 2020). Commissural stimulation evokes an
  early EPSP → IPSP → late depolarising sequence (Sik 1995). **No sag/rebound response to hyperpolarisation**
  (Hewitt 2021, citing Gloveli 2005) — a clean discriminator against OLM and LTh cells, which are defined
  partly *by* prominent Ih sag.
- **`cl_mapping`** — remains `null` (no suitable existing parent; `CL:4023121 sst chodl` is excluded because
  these cells are Sst-negative). **Add `proposed_cl_term`**, following the `ca2_pc_hippocampus` /
  `ca3_pc_hippocampus` precedent in the same repo:
  ```yaml
  proposed_cl_term:
    label: hippocampal trilaminar cell
    parent_cl_term: {id: CL:1001569, label: hippocampal interneuron, name_in_source: hippocampal interneuron}
    cl_id: 'https://github.com/obophenotype/cell-ontology/issues/3744'
    status: SUBMITTED
  ```
- **`definition_references`** — replace the orphan with the real set (the 3–5 most informative):
  `PMID:7472426` (Sik 1995), `PMID:16280590` (Ferraguti 2005), `PMID:32016558` (Katona 2020),
  `PMID:17699661` (Jinno 2007), `PMID:30084021` (Booker & Vida 2018).
- **`notes`** — must capture, at minimum:
  1. **Nomenclature hazard.** Slomianka et al. 2011 (PMID:21597968) records that a deep CA1 *pyramidal*
     subpopulation (Ctip2, Sox5, M1 receptor, SST, NPY) has *also* been called "trilaminar cells" — a
     glutamatergic population, not this type. "Radial trilaminar cells" may be a variant or a separate
     entity. Ferraguti 2005, following Somogyi 2005, stipulated the name be reserved for the Sik 1995 type.
  2. **Closest confusable:** the M2+ VIP-LRP (Type I) cell of Francavilla et al. 2018 (PMID:30487571) —
     shares soma position, horizontal dendrites, SST-negativity, mGluR8a+ inputs; separated by absence of
     VIP/NPY/CB, much denser mGluR8a decoration, and the three-layer axon.
  3. **mGluR8a is an input property, not expression** — it decorates the presynaptic terminals innervating
     these cells. Do not enter it as a `defining_marker`.
  4. **CA3 occurrence** reported by Katona 2020 (rat and mouse), but the type is defined in CA1.
  5. **Septal projection direction is disputed** — Ferraguti 2005 and Slomianka 2011 refer to output to
     septum (also olfactory bulb, hypothalamus); Katona 2020 reports mGluR8a-enriched GABAergic input
     *from* the medial septum. Only the CA1→subiculum projection is asserted.
  6. **The orphan `PMID:28646648` was removed** during this ingest — record that, so it isn't reinstated.

---

## 5. Step 4 — QC gate

```bash
just inspect kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml   # round-trip sanity
just validate kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml  # LinkML
just qc                                                                       # validate-all + validate-terms
git diff --stat && git diff kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml
```

The pre-edit hook (`.claude/hooks/validate_mapping_hook.py`) also fires automatically on the fold write and
checks: YAML parse, structural integrity, `quote_key` presence in `references.json`, PMID/DOI presence in
`references.json`, LinkML conformance, and CL/UBERON CURIE resolution via OAK. If OAK DBs aren't cached,
run `just fetch-oak-dbs`.

**Review the diff before committing.** Expect: one node replaced in place, references.json grown by ~14 paper
entries plus quotes, two new drivers under `research/_drivers/`, one fragment + extraction artifacts under
`research/hippocampus/trilaminar_20260911/`. Anything else in the diff is a bug.

---

## 6. Explicitly OUT of scope

Do not do these as part of this ingest. Each is a separate decision.

- **The `Ntng1.Chrm2` → WMBv1 mapping edge.** Harris et al. 2017 (= GEO:GSE99888) is already ingested as
  two AT runs here, and its `Ntng1.Chrm2` class — the Sst−/Pvalb−/Chrm2+/Ntng1+ cluster Katona 2020 ties to
  this cell type — already has scored results in
  `kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/f1_matrix_harris_class.csv`:
  supertype `0198 RHP-COA Ndnf Gaba_6` F1 = 0.96 (n = 66, group purity 0.96, target purity 0.97);
  cluster `0704 RHP-COA Ndnf Gaba_6` F1 = 0.97; class `06 CTX-CGE GABA` purity 0.99 (consistent with the
  reported CGE origin). That is a strong correspondence — but the link to the *morphologically defined* type
  is Katona's inference from shared markers, not a measurement, and the Allen subclass label is
  retrohippocampal/cortical-amygdalar while the source cells are CA1 by dissection. NTR #3744 states both
  caveats and deliberately does not propose a cross-reference. Decide separately whether to author an
  `at_source_sets` entry and run `map-cell-type`.
- **`cite-traverse` / primary-literature Round 2.** The orchestrator's recommended follow-up; not needed to
  land the reference and node updates.
- **Any `src/`, `schema/`, `justfile` or `workflows/` change** — out of curation scope. If the fold driver
  proves generally useful, file a dev-request issue to promote it to `src/` + a `just` recipe.
- **Touching other nodes.** The report has knock-on relevance for `olm_cell_ca1`,
  `axo_axonic_cell_hippocampus` (both proposed as targets of trilaminar inhibition during ripples) and
  `lth_cell_hippocampus` (Hewitt 2021 argues LTh cells are *not* trilaminar cells). Note these for later;
  leave them alone now.

---

## 7. Files to read first

| File | Why |
|---|---|
| `trilaminar_reference_resolution.txt` | corpus-ID → DOI/PMID resolution table; **do not redo this work** |
| `reports/hippocampus/cl_term_requests/trilaminar_cell_hippocampus_ntr.md` | what we told CL; the node must agree |
| `src/evidencell/references.py` | `write_quote_to_refs()` — the only sanctioned path into references.json |
| `research/_drivers/merge_ingest_into_mapping.py` | fold-driver precedent (note: additive; we need replace) |
| `workflows/asta-report-ingest.md` §Step 1, §Step 2, §Step 3b Part B | the steps being reused |
| `CLAUDE.md` | curation-mode writable zones, anti-hallucination hooks |

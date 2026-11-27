#!/usr/bin/env python3
"""Seed references/hypothalamus/ ahead of migrating hypothalamic nodes out of
kb/graphs/sexually_dimorphic/.

This is a verbatim copy, not a new ingest: every migrating node's cited papers
and quotes already exist, validated, in references/sexually_dimorphic/. We are
not minting new quote_keys from raw text (that is what write_quote_to_refs()
is for), we are duplicating already-validated records into a sibling store so
that qc_content's per-region "does this file's region have a store" check
passes the moment the KB YAML files move. Uses the same low-level primitives
(save_paper/append_quote) and read-reload-verify idiom as
src/evidencell/migrate_refs.py. references/sexually_dimorphic/ is never
touched -- this script is purely additive.

Usage:
    uv run python research/_drivers/migrate_hypothalamus_refs.py --dry-run
    uv run python research/_drivers/migrate_hypothalamus_refs.py
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from evidencell.references import load_papers, load_quotes, save_paper, append_quote, _write_json  # noqa: E402
from evidencell.validate import _collect_quote_keys, _collect_refs, _collect_flat_refs  # noqa: E402

SRC_REGION = "sexually_dimorphic"
DST_REGION = "hypothalamus"

# The 36 nodes added fresh by PR #257 (verified via
# `git diff --name-only --diff-filter=A main...HEAD -- kb/graphs/sexually_dimorphic/`)
NEW_FILES = [
    "arc_agrp_npy_neuron.yaml", "arc_crabp1_neuron.yaml", "arc_me_sst_neuron.yaml",
    "arc_npgl_neuron.yaml", "arc_pomc_gabaergic_neuron.yaml",
    "arc_pomc_glutamatergic_neuron.yaml", "arc_pomc_neuron.yaml",
    "arc_pomc_tac2_neuron.yaml", "arc_tida_dopamine_neuron.yaml",
    "dmh_cck_neuron.yaml", "dmh_compact_refeeding_neuron.yaml", "dmh_grp_neuron.yaml",
    "dmh_lepr_neuron.yaml", "dmh_pdyn_neuron.yaml", "dmh_ppp1r17_neuron.yaml",
    "hypothalamic_th_neuron.yaml", "lh_pv_glutamatergic_neuron.yaml",
    "lha_gabaergic_neuron.yaml", "lha_glutamatergic_neuron.yaml",
    "lha_leprb_nts_neuron.yaml", "lha_mch_neuron.yaml", "lha_orexin_neuron.yaml",
    "mammillary_body_neuron.yaml", "periventricular_dopamine_neuron.yaml",
    "poa_aromatase_i2_cluster.yaml", "pvh_brs3_pb_projecting_neuron.yaml",
    "pvn_avp_neuron.yaml", "pvn_crh_neuron.yaml", "pvn_oxt_neuron.yaml",
    "pvn_preautonomic_neuron.yaml", "pvn_trh_neuron.yaml",
    "rostral_zi_th_gabaergic_neuron.yaml", "tmn_histaminergic_neuron.yaml",
    "vmh_dorsomedial_lepr_neuron.yaml", "vmh_tuberal_anterolateral_glut_neuron.yaml",
    "vmhvl_neuron.yaml",
]

# Pre-existing, genuinely hypothalamic, zero documented sex_bias -- curator
# decision to migrate alongside the new nodes rather than leave stranded.
JUDGMENT_CALL_FILES = [
    "arc_aromatase_neuron.yaml",
    "mpoa_esr1_neuron.yaml",
    "pvn_crfr1_neuron.yaml",
    "vmhvl_esr1_pr_neuron.yaml",
]

MIGRATING_FILES = NEW_FILES + JUDGMENT_CALL_FILES


def _pmid_doi_from_ref(ref: str) -> tuple[str | None, str | None]:
    ref = ref.strip()
    if ref.upper().startswith("PMID:"):
        return ref.split(":", 1)[1].strip(), None
    if ref.upper().startswith("DOI:"):
        return None, ref.split(":", 1)[1].strip().lower()
    return None, None


def collect_needed(kb_dir: pathlib.Path, filenames: list[str]) -> tuple[set[str], set[str], dict[str, str]]:
    """Return (needed_corpus_ids_from_quote_keys, needed_quote_keys, ref_strings_by_kind)."""
    quote_keys: set[str] = set()
    pmids: set[str] = set()
    dois: set[str] = set()

    for name in filenames:
        doc = yaml.safe_load((kb_dir / name).read_text(encoding="utf-8"))
        quote_keys.update(_collect_quote_keys(doc))
        for ref in _collect_refs(doc):
            pmid, doi = _pmid_doi_from_ref(ref)
            if pmid:
                pmids.add(pmid)
            if doi:
                dois.add(doi)
        for _field, raw in _collect_flat_refs(doc):
            pmid, doi = _pmid_doi_from_ref(raw)
            if pmid:
                pmids.add(pmid)
            if doi:
                dois.add(doi)

    corpus_ids_from_quotes = {qk.rsplit("_", 1)[0] for qk in quote_keys}
    return corpus_ids_from_quotes, quote_keys, {"pmids": pmids, "dois": dois}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    # Node YAMLs already moved to their destination folder in a prior commit;
    # content is unchanged by the move, so read citations from wherever the
    # files currently live.
    kb_dir = ROOT / "kb" / "graphs" / DST_REGION
    src_refs = ROOT / "references" / SRC_REGION
    dst_refs = ROOT / "references" / DST_REGION

    corpus_ids_from_quotes, quote_keys, ref_sets = collect_needed(kb_dir, MIGRATING_FILES)

    src_papers = load_papers(src_refs)
    src_quotes = load_quotes(src_refs)

    # Resolve PMID:/DOI: refs to corpus_ids via the source store's paper identity.
    corpus_ids_from_refs: set[str] = set()
    unresolved_pmids, unresolved_dois = [], []
    for corpus_id, entry in src_papers.items():
        pmid = str(entry.get("pmid") or "")
        doi = str(entry.get("doi") or "").lower()
        if pmid and pmid in ref_sets["pmids"]:
            corpus_ids_from_refs.add(corpus_id)
        if doi and doi in ref_sets["dois"]:
            corpus_ids_from_refs.add(corpus_id)
    found_pmids = {str(e.get("pmid")) for e in src_papers.values() if e.get("pmid")}
    found_dois = {str(e.get("doi")).lower() for e in src_papers.values() if e.get("doi")}
    unresolved_pmids = sorted(ref_sets["pmids"] - found_pmids)
    unresolved_dois = sorted(ref_sets["dois"] - found_dois)

    needed_corpus_ids = sorted(corpus_ids_from_quotes | corpus_ids_from_refs)

    print(f"migrating files       : {len(MIGRATING_FILES)} ({len(NEW_FILES)} new + {len(JUDGMENT_CALL_FILES)} judgment-call)")
    print(f"quote_keys cited      : {len(quote_keys)}")
    print(f"needed corpus_ids     : {len(needed_corpus_ids)}  {needed_corpus_ids}")
    if unresolved_pmids:
        print(f"WARNING unresolved PMIDs (cited but no matching paper in source store): {unresolved_pmids}")
    if unresolved_dois:
        print(f"WARNING unresolved DOIs (cited but no matching paper in source store): {unresolved_dois}")
    missing_papers = [c for c in needed_corpus_ids if c not in src_papers]
    if missing_papers:
        print(f"ERROR: corpus_id(s) referenced by quote_key but absent from source papers/: {missing_papers}", file=sys.stderr)
        return 2

    if args.dry_run:
        print("\nDRY RUN -- nothing written.")
        return 0

    papers_written = papers_skipped = quotes_written = quotes_skipped = 0
    for corpus_id in needed_corpus_ids:
        try:
            save_paper(dst_refs, corpus_id, src_papers[corpus_id])
            papers_written += 1
        except FileExistsError:
            papers_skipped += 1

    for qk in sorted(quote_keys):
        corpus_id = qk.rsplit("_", 1)[0]
        if qk not in src_quotes:
            print(f"ERROR: quote_key {qk} cited in a migrating node but absent from source quotes/", file=sys.stderr)
            return 2
        if append_quote(dst_refs, corpus_id, qk, src_quotes[qk]):
            quotes_written += 1
        else:
            quotes_skipped += 1

    # Verify: reload the destination store and check byte-for-byte equality.
    dst_papers = load_papers(dst_refs)
    dst_quotes = load_quotes(dst_refs)
    for corpus_id in needed_corpus_ids:
        assert dst_papers.get(corpus_id) == src_papers[corpus_id], f"paper mismatch after write: {corpus_id}"
    for qk in quote_keys:
        assert dst_quotes.get(qk) == src_quotes[qk], f"quote mismatch after write: {qk}"

    # sources/ -- ASTA_REPORT quotes cite a source_document id that must have a
    # record under references/{region}/sources/ (qc_content.check_source_documents).
    # Copy any cited source id not yet present in the destination store, verbatim.
    needed_source_ids = {
        src_quotes[qk].get("source_document")
        for qk in quote_keys
        if isinstance(src_quotes[qk], dict) and src_quotes[qk].get("source_document")
    }
    sources_written = sources_skipped = 0
    src_sources_dir = src_refs / "sources"
    dst_sources_dir = dst_refs / "sources"
    for sid in sorted(needed_source_ids):
        src_file = src_sources_dir / f"{sid}.json"
        if not src_file.exists():
            print(f"ERROR: source_document '{sid}' cited by a migrating quote but no record at {src_file}", file=sys.stderr)
            return 2
        dst_file = dst_sources_dir / f"{sid}.json"
        if dst_file.exists():
            sources_skipped += 1
            continue
        _write_json(dst_file, __import__("json").loads(src_file.read_text(encoding="utf-8")))
        sources_written += 1

    for sid in needed_source_ids:
        dst_file = dst_sources_dir / f"{sid}.json"
        src_file = src_sources_dir / f"{sid}.json"
        assert dst_file.read_text(encoding="utf-8") == src_file.read_text(encoding="utf-8"), f"source mismatch after write: {sid}"

    print(f"\npapers: {papers_written} written, {papers_skipped} already present (idempotent re-run)")
    print(f"quotes: {quotes_written} written, {quotes_skipped} already present (idempotent re-run)")
    print(f"sources: {sources_written} written, {sources_skipped} already present (idempotent re-run), {len(needed_source_ids)} needed: {sorted(needed_source_ids)}")
    print(f"Verified: all {len(needed_corpus_ids)} papers, {len(quote_keys)} quotes, {len(needed_source_ids)} sources reload byte-identical to source.")
    print(f"references/{SRC_REGION}/ untouched (additive-only migration).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

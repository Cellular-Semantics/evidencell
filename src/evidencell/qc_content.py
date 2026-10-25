"""Content QC sweep — provenance checks across the whole KB and report corpus.

`just validate-all` checks YAML *shape* (LinkML) and `just validate-terms`
checks ontology term references. Neither looks at whether the content is
*supported*: whether quote_keys, PMIDs, DOIs and AT run_refs actually resolve
against the validated stores. Those checks live in `validate.py` and until now
only ever ran inside the pre-edit hook, i.e. only on interactive Claude Code
edits. Script-based writes, bulk migrations and anything landing via PR were
never swept (issues #81, #86, #133).

This module runs the same checks over every file at once:

  kb/graphs/**/*.yaml   structural integrity, quote_key provenance, ref
                        PMID/DOI provenance, flat citation lists, AT run_ref
                        resolution, rationale currency
  kb/<other>/**/*.yaml  structural integrity + run_refs only (no region, so no
                        references.json to resolve against — see the
                        path-aware-checks tidy-up in
                        planning/dev_requests/2026-04-28_validation-hook-tidy-ups.md)
  reports/**/*.md       blockquote annotation, quote_key / PMID provenance,
                        ontology CURIEs, atlas accessions

Severity
--------
ERROR    the pre-edit hook already blocks this; a sweep hit means the content
         reached disk by a path that bypassed the hook
WARN     known backlog, not yet enforced (flat citation lists — see #133) or
         advisory (stale rationale hashes)

Exit code is 1 when any ERROR is found, 0 otherwise. `--strict` promotes WARN
to ERROR; use it in CI once the flat-citation backlog is remediated.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

from evidencell.paths import at_run_index_path, repo_root
from evidencell.references import load_store, store_exists
from evidencell.validate import (
    _collect_flat_refs,
    _collect_quote_keys,
    _collect_refs,
    check_flat_ref_pmids,
    check_md_ids,
    check_ontology_terms,
    check_quote_key_integrity,
    check_source_documents,
    check_source_methods,
    check_store_records,
    check_quote_keys,
    check_rationale_currency,
    check_ref_pmids,
    check_run_refs,
    parse_md_annotations,
    structural_checks,
)

ERROR = "ERROR"
WARN = "WARN"
# A gap is something this repository cannot currently close by editing content:
# a deepsearch PDF that was never committed cannot be conjured back. Kept out of
# the baseline entirely — mixing it with fixable findings is what made
# "0 new / 0 stale" stop meaning anything, since three quarters of the baseline
# could never clear.
#
# "Cannot currently close" is deliberately weaker than "unfixable". The missing
# artefact is the ASTA *report*; the *paper* it summarises is still reachable,
# and verifying a quote against the paper would make the lost PDF irrelevant —
# a stronger check than the one it replaces, since the report is one remove
# from the source. See issue #143. Until then these are gaps; afterwards most
# of them should become checkable.
GAP = "GAP"

# kb/ subtrees that carry no region and therefore no references.json. Bulk atlas
# content (taxonomy levels) is excluded outright: the files are enormous, are
# machine-generated from taxonomy ingest, and carry no provenance fields.
_NO_REGION_SUBTREES = ("datasets", "correlation_runs", "annotation_transfer_runs")

# Ontology prefixes whose backing data was missing during the current sweep.
# Module-level because the per-file checker discovers it but only the sweep
# summary is the right place to say it, and saying it once beats saying it 53
# times.
_CURIE_COVERAGE: dict[str, dict] = {}

# Atlas accessions per region, cached for the duration of one sweep. Cleared in
# run_sweep() so a caller sweeping twice over changed content sees the change.
_KB_NODES_CACHE: dict[tuple[str, str], dict] = {}
_EXCLUDED_SUBTREES = ("taxonomy",)


@dataclass
class Finding:
    """One QC hit against one file."""

    path: str
    severity: str
    check: str
    message: str


@dataclass
class SweepResult:
    findings: list[Finding] = field(default_factory=list)
    kb_files: int = 0
    report_files: int = 0
    ref_stores: int = 0
    skipped: list[str] = field(default_factory=list)
    unavailable: list[str] = field(default_factory=list)

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == ERROR]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == WARN]

    @property
    def gaps(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == GAP]

    @property
    def trackable(self) -> list[Finding]:
        """Findings the baseline covers — everything that could be fixed."""
        return [f for f in self.findings if f.severity != GAP]


def _region_of(path: Path, root: Path) -> str | None:
    """Return the region for a kb/graphs or reports file, else None.

    kb/graphs/{region}/x.yaml → region;  reports/{region}/x.md → region.
    """
    try:
        parts = path.resolve().relative_to(root.resolve()).parts
    except ValueError:
        return None
    if len(parts) >= 3 and parts[0] == "kb" and parts[1] == "graphs":
        return parts[2]
    if len(parts) >= 2 and parts[0] == "reports":
        return parts[1]
    return None


def _kb_files(root: Path) -> list[Path]:
    kb = root / "kb"
    if not kb.is_dir():
        return []
    out = []
    for p in sorted(kb.rglob("*.yaml")):
        rel = p.relative_to(kb)
        if rel.parts and rel.parts[0] in _EXCLUDED_SUBTREES:
            continue
        out.append(p)
    return out


def _report_files(root: Path) -> list[Path]:
    reports = root / "reports"
    return sorted(reports.rglob("*.md")) if reports.is_dir() else []


def _kb_nodes_for_region(root: Path, region: str) -> dict:
    """Collect {cell_set_accession: node} across a region's graphs.

    Mirrors what the pre-edit hook builds for report accession checks.

    Cached per (root, region) for the duration of a sweep. Without it this
    re-parsed every graph YAML in the region once per report: 1.7 MB of YAML
    read 37 times for hippocampus alone, 41 s of a 52 s sweep. The hook calls
    the equivalent once per edit and does not need the cache; the sweep calls
    it 64 times and does.
    """
    key = (str(root.resolve()), region)
    if key in _KB_NODES_CACHE:
        return _KB_NODES_CACHE[key]

    nodes: dict = {}
    region_dir = root / "kb" / "graphs" / region
    if not region_dir.is_dir():
        return nodes
    for yf in sorted(region_dir.glob("*.yaml")):
        try:
            doc = yaml.safe_load(yf.read_text(encoding="utf-8"))
        except (yaml.YAMLError, OSError):
            # Unreadable sibling graph — the file gets its own parse finding
            # when the sweep reaches it; don't fail accession lookup over it.
            continue
        for node in (doc or {}).get("nodes", []) or []:
            if isinstance(node, dict) and (acc := node.get("cell_set_accession")):
                nodes[acc] = node
    _KB_NODES_CACHE[key] = nodes
    return nodes


def sweep_kb_file(path: Path, root: Path) -> list[Finding]:
    """Run every content check applicable to one KB YAML file."""
    rel = str(path.relative_to(root))
    findings: list[Finding] = []

    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [Finding(rel, ERROR, "yaml-parse", str(exc))]
    except OSError as exc:
        return [Finding(rel, ERROR, "read", str(exc))]

    if not isinstance(doc, dict):
        return findings

    for msg in structural_checks(doc):
        findings.append(Finding(rel, ERROR, "structural", msg))

    for msg in check_run_refs(doc, at_run_index_path()):
        findings.append(Finding(rel, ERROR, "run_ref", msg))

    region = _region_of(path, root)
    if region is not None:
        refs_dir = root / "references" / region
        # Every provenance check in validate.py returns [] when references.json
        # is absent, so a region without a reference store silently passes all
        # of them — in this sweep *and* in the pre-edit hook. A graph with no
        # citations yet is legitimately unbacked; one that cites papers is not.
        if not store_exists(refs_dir):
            cited = len(_collect_refs(doc)) + len(_collect_quote_keys(doc)) + len(
                _collect_flat_refs(doc)
            )
            if cited:
                findings.append(Finding(
                    rel, ERROR, "no_refs_store",
                    f"references/{region}/ has no store (no papers/), but this file "
                    f"carries {cited} citation(s)/quote_key(s). Every provenance check is "
                    f"vacuous for region '{region}' — ingest the references to enable them.",
                ))
        for msg in check_quote_keys(doc, refs_dir):
            findings.append(Finding(rel, ERROR, "quote_key", msg))
        for msg in check_ref_pmids(doc, refs_dir):
            findings.append(Finding(rel, ERROR, "ref_pmid", msg))
        # ERROR, not WARN: #133 proposed warn-only so the 13-entry backlog
        # wouldn't block every subsequent edit, but the baseline file does that
        # job without blunting the check. Leaving these as warnings would let a
        # *newly* hallucinated definition_references PMID pass CI, which is
        # precisely what this sweep exists to stop. The pre-edit hook is
        # unaffected — it does not call check_flat_ref_pmids.
        for msg in check_flat_ref_pmids(doc, refs_dir):
            findings.append(Finding(rel, ERROR, "flat_citation", msg))

    for msg in check_rationale_currency(doc):
        findings.append(Finding(rel, WARN, "rationale_stale", msg))

    return findings


def reset_sweep_state() -> None:
    """Clear state scoped to one sweep.

    `_CURIE_COVERAGE` and `_KB_NODES_CACHE` exist to make a whole-corpus sweep
    affordable, but they are module globals and the per-file functions are
    callable directly. A caller driving `sweep_report_file()` itself would
    otherwise accumulate coverage across unrelated runs and hold a node cache
    that never notices edits under kb/graphs/.
    """
    _CURIE_COVERAGE.clear()
    _KB_NODES_CACHE.clear()


def sweep_report_file(path: Path, root: Path) -> list[Finding]:
    """Run markdown annotation + provenance checks on one report.

    Uses sweep-scoped caches; call `reset_sweep_state()` when invoking this
    outside `run_sweep()`.
    """
    rel = str(path.relative_to(root))
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [Finding(rel, ERROR, "read", str(exc))]

    region = _region_of(path, root)
    if region is None:
        return []

    refs_dir = root / "references" / region
    annotations = parse_md_annotations(text)
    kb_nodes = _kb_nodes_for_region(root, region)

    findings = [
        Finding(rel, ERROR, "markdown", msg)
        for msg in check_md_ids(annotations, refs_dir, kb_nodes)
    ]

    # Ontology CURIEs, resolved against OAK. Unavailable prefixes are returned
    # separately and surfaced as coverage, never as silence.
    errors, unavailable = check_ontology_terms(
        annotations.get("curie_ids") or [], root / "conf" / "oak_config.yaml"
    )
    findings += [Finding(rel, ERROR, "ontology_term", m) for m in errors]
    for prefix, info in unavailable.items():
        seen = _CURIE_COVERAGE.setdefault(
            prefix, {"adapter": info["adapter"], "reason": info["reason"], "terms": set()})
        seen["terms"].update(info["terms"])
    return findings


def _reference_stores(root: Path) -> list[Path]:
    """Region store roots, in either layout."""
    refs = root / "references"
    if not refs.is_dir():
        return []
    return [d for d in sorted(refs.iterdir()) if d.is_dir() and store_exists(d)]


def sweep_reference_store(path: Path, root: Path) -> list[Finding]:
    """Check a reference store's internal integrity.

    Everything else in this sweep validates KB and report content *against* the
    reference store. Nothing validated the store itself — it is the most trusted
    file in the repo and the only one with no write guard, which is how a quote
    whose key attested nothing survived six months.
    """
    rel = str(path.relative_to(root))
    try:
        store = load_store(path)
    except json.JSONDecodeError as exc:
        return [Finding(rel, ERROR, "refs-parse", f"invalid JSON: {exc}")]
    except OSError as exc:
        return [Finding(rel, ERROR, "read", str(exc))]

    if not isinstance(store, dict):
        return [Finding(rel, ERROR, "refs-parse", "store is not a JSON object")]

    findings = [
        Finding(rel, ERROR, "quote_key_integrity", msg)
        for msg in check_quote_key_integrity(store)
    ]
    findings += [
        Finding(rel, ERROR, "store_schema", msg)
        for msg in check_store_records(store)
    ]
    findings += [
        Finding(rel, ERROR, "source_method", msg)
        for msg in check_source_methods(store)
    ]
    sources_dir = path if path.is_dir() else path.parent
    known = {p.stem for p in (sources_dir / "sources").glob("*.json")}
    for msg in check_source_documents(store, known):
        # "paper 'X': N quotes with no source_document" is a gap — the PDF was
        # never committed. "source_document 'Y' has no record" is a broken
        # reference, which is fixable here.
        severity = GAP if msg.startswith("paper '") else ERROR
        findings.append(Finding(rel, severity, "source_document", msg))
    return findings


def _coverage_gaps(root: Path, kb_paths: list[Path], report_paths: list[Path]) -> list[str]:
    """Which checks could not run, and over how much of the corpus.

    Every provenance check returns [] when its backing store is absent, so a
    missing input turns into silence rather than an error. The pre-edit hook
    reports this per file; without the same report here the corpus-wide sweep —
    the one CI runs and the badge reflects — could pass with checks inert
    across the whole repository and say nothing.
    """
    gaps: list[str] = []

    storeless: dict[str, int] = {}
    for p in kb_paths + report_paths:
        region = _region_of(p, root)
        if region and not store_exists(root / "references" / region):
            storeless[region] = storeless.get(region, 0) + 1
    if storeless:
        total = sum(storeless.values())
        where = ", ".join(f"{r} ({n})" for r, n in sorted(storeless.items()))
        gaps.append(
            f"quote_key / PMID / DOI / flat citations — no reference store for "
            f"{where}; {total} file(s) unchecked"
        )

    if kb_paths and not at_run_index_path().exists():
        gaps.append(
            f"AT run_ref — no {at_run_index_path().name} under "
            f"kb/annotation_transfer_runs/; {len(kb_paths)} KB file(s) unchecked"
        )

    return gaps


ATLAS_BASIS = "ATLAS_TRANSCRIPTOMIC"


def sweep_cross_file(root: Path, kb_paths: list[Path]) -> list[Finding]:
    """Checks that no single-file pass can make.

    These are corpus-wide on purpose. `_kb_nodes_for_region` is region-scoped,
    and the duplicates that actually exist span regions -- `dg_neuroblast` and
    its two siblings are defined in both `dentate_gyrus/` and
    `immature_neurons/` -- so a per-region index would never see them.
    """
    findings: list[Finding] = []
    canonical: dict[str, list[str]] = {}
    taxonomy_ids: dict[str, set[str]] = {}
    per_file: list[tuple[str, dict, list[dict], list[dict]]] = []

    for path in kb_paths:
        rel = str(path.relative_to(root))
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue  # the per-file sweep already reported the parse failure
        if not isinstance(doc, dict):
            continue
        nodes = [n for n in doc.get("nodes") or [] if isinstance(n, dict) and n.get("id")]
        edges = [e for e in doc.get("edges") or [] if isinstance(e, dict)]
        per_file.append((rel, doc, nodes, edges))

        for node in nodes:
            node_id = node["id"]
            # A reference stub is a placeholder, never a definition. Bucketing
            # by definition_basis alone counts a lit stub as canonical, which
            # makes duplicate_node_id fire on every type that is referenced
            # from another file and makes dangling_endpoint resolve a stub to
            # itself.
            if (
                node.get("definition_basis") != ATLAS_BASIS
                and not node.get("reference_stub")
            ):
                canonical.setdefault(node_id, []).append(rel)
            tax_id = node.get("taxonomy_id")
            if tax_id:
                taxonomy_ids.setdefault(str(tax_id), set()).add(rel)

    # 1. A node id canonically defined in more than one file. Which copy is
    #    authoritative is a curator decision, so this is an ERROR, not a merge.
    for node_id, files in sorted(canonical.items()):
        if len(files) > 1:
            findings.append(Finding(
                sorted(files)[0], ERROR, "duplicate_node_id",
                f"Node '{node_id}' is canonically defined in {len(files)} files: "
                f"{', '.join(sorted(files))}",
            ))

    # 2. A taxonomy_id with no directory under kb/taxonomy/. Every DB lookup for
    #    such a node fails, and the failures are swallowed (render._node_b_info
    #    catches broadly so a missing DB never blocks a report), so nothing
    #    surfaces without this check.
    tax_root = root / "kb" / "taxonomy"
    for tax_id, files in sorted(taxonomy_ids.items()):
        if not (tax_root / tax_id).is_dir():
            findings.append(Finding(
                sorted(files)[0], ERROR, "unknown_taxonomy_id",
                f"taxonomy_id '{tax_id}' has no directory under kb/taxonomy/ "
                f"(referenced in {len(files)} file(s): {', '.join(sorted(files))})",
            ))

    # 3. A lit stub pointing at nothing. Lit stubs let a lit-to-lit edge span
    #    two files -- each type keeps its own file and the stub satisfies the
    #    in-document endpoint rule. Nothing in that rule checks the stub
    #    resolves to a real definition, so a renamed or deleted node leaves the
    #    stub silently pointing at a type that no longer exists. This is the
    #    only check standing between a lit stub and a dangling reference.
    #
    #    Atlas stubs are out of scope: they resolve against kb/taxonomy/, not
    #    against kb/graphs, and unknown_taxonomy_id covers the directory side.
    for rel, _doc, nodes, _edges in per_file:
        for node in nodes:
            if node.get("reference_stub") != "LIT_TYPE":
                continue
            homes = canonical.get(node["id"]) or []
            if not homes:
                findings.append(Finding(
                    rel, ERROR, "dangling_endpoint",
                    f"Lit stub '{node['id']}' has no canonical definition in any "
                    "KB file. Either the type was renamed or removed, or the "
                    "stub was authored against an id that never existed.",
                ))
            elif len(homes) > 1:
                findings.append(Finding(
                    rel, ERROR, "dangling_endpoint",
                    f"Lit stub '{node['id']}' resolves to {len(homes)} canonical "
                    f"definitions: {', '.join(sorted(homes))}. Ambiguous reference.",
                ))

    # 4. Distinct node ids sharing an identical name. Renaming a duplicate so
    #    each file defines a distinct id unblocks the layout but silences
    #    `duplicate_node_id`, which would lose the signal entirely. The name is
    #    the part that stays identical, so this keeps the pair visible until a
    #    curator actually decides whether to merge them. WARN, not ERROR: two
    #    records of one type is a backlog item, not a broken KB.
    by_name: dict[str, list[tuple[str, str]]] = {}
    for rel, _doc, nodes, _edges in per_file:
        for node in nodes:
            name = node.get("name")
            if name and node.get("definition_basis") != ATLAS_BASIS:
                by_name.setdefault(str(name), []).append((rel, node["id"]))
    for name, entries in sorted(by_name.items()):
        ids = sorted({node_id for _, node_id in entries})
        if len(ids) < 2:
            continue
        findings.append(Finding(
            sorted(rel for rel, _ in entries)[0], WARN, "possible_duplicate_name",
            f"Name '{name}' is held by {len(ids)} distinct node ids: "
            f"{', '.join(ids)}. Same name, different ids -- either one type "
            "recorded twice (merge is a curator decision) or two types needing "
            "distinguishable names.",
        ))

    # 5. A node that no edge *in its own file* references. Scoped per file, not
    #    corpus-wide, because that is what a component split acts on: a node
    #    unreferenced in its own document belongs to no component and is
    #    dropped, regardless of whether some other file's edge names it. Pooling
    #    endpoints across files hides 21 of the 39 such nodes.
    #
    #    Atlas stubs exist only to satisfy edge endpoints, so an unreferenced
    #    one is dead weight. An unreferenced non-atlas node is an unmapped
    #    literature type -- legitimate content that must survive the split.
    for rel, _doc, nodes, edges in per_file:
        endpoints = {
            x for e in edges
            for x in (e.get("lit_type"), e.get("taxonomy_type")) if x
        }
        for node in nodes:
            if node["id"] in endpoints:
                continue
            if node.get("reference_stub"):
                # A placeholder referenced by no edge in its own file has no
                # reason to exist, but dangling_endpoint is the check that
                # speaks about stubs; reporting it here too would double-count.
                continue
            kind = "atlas stub" if node.get("definition_basis") == ATLAS_BASIS else "node"
            findings.append(Finding(
                rel, WARN, "orphan_node",
                f"{kind.capitalize()} '{node['id']}' is referenced by no edge",
            ))

    return findings


def run_sweep(
    root: Path | None = None,
    *,
    kb: bool = True,
    reports: bool = True,
    references: bool = True,
) -> SweepResult:
    """Sweep the corpus and return every finding."""
    root = root or repo_root()
    result = SweepResult()
    reset_sweep_state()

    kb_paths = _kb_files(root) if kb else []
    report_paths = _report_files(root) if reports else []

    if kb:
        for p in kb_paths:
            result.kb_files += 1
            result.findings.extend(sweep_kb_file(p, root))
        result.findings.extend(sweep_cross_file(root, kb_paths))
        for sub in _EXCLUDED_SUBTREES:
            if (root / "kb" / sub).is_dir():
                result.skipped.append(f"kb/{sub}/ (bulk atlas content, no provenance fields)")

    if reports:
        for p in report_paths:
            result.report_files += 1
            result.findings.extend(sweep_report_file(p, root))

    if references:
        for p in _reference_stores(root):
            result.ref_stores += 1
            result.findings.extend(sweep_reference_store(p, root))

    result.unavailable = _coverage_gaps(root, kb_paths, report_paths)
    for prefix, info in sorted(_CURIE_COVERAGE.items()):
        result.unavailable.append(
            f"ontology terms — {prefix} ({len(info['terms'])} distinct term(s) across "
            f"the corpus) — {info['adapter']}: {info['reason']}"
        )
    return result


# What identifies a finding *within* a (path, check), independent of the prose
# around it. Keyed by check name; the pattern's first group is the subject.
#
# Fingerprinting on the whole message means improving wording is
# indistinguishable from "one finding fixed, one new finding appeared". That
# happened three times while removing the compat shim — each needed a manual
# 1-new/1-stale check before re-baselining, and skipping that check once would
# absorb a real regression. The subject is the durable part; the sentence
# built around it is not.
# A check may emit several message shapes; the first pattern that matches wins.
_SUBJECT_PATTERNS: dict[str, tuple[str, ...]] = {
    "quote_key_integrity": (r"quote_key '([^']+)'",),
    "quote_key":           (r"quote_key '([^']+)'",),
    "flat_citation":       (r"'((?:PMID|DOI):[^']+)'",),
    "ref_pmid":            (r"'((?:PMID|DOI):[^']+)'",),
    "run_ref":             (r"run_ref '([^']+)'",),
    "source_method":       (r"quote '([^']+)'",),
    "source_document":     (r"quote '([^']+)'", r"paper '([^']+)'"),
    "store_schema":        (r"(?:paper|quote) '([^']+)'",),
    "rationale_stale":     (r"Edge '([^']+)'",),
    "structural":          (r"'([^']+)'",),
    "ontology_term":       (r"Ontology term '([^']+)'",),
    "duplicate_node_id":   (r"Node '([^']+)'",),
    "unknown_taxonomy_id": (r"taxonomy_id '([^']+)'",),
    "orphan_node":         (r"'([^']+)' is referenced by no edge",),
    "dangling_endpoint":   (r"Lit stub '([^']+)'",),
    "possible_duplicate_name": (r"Name '([^']+)'",),
    "markdown": (
        r"(?:Atlas accession|PMID|quote_key) '([^']+)'",
        # Unannotated blockquote: the quoted line itself is the subject.
        r"annotation\): (.+)$",
    ),
}

# Checks that emit at most one finding per file, so (path, check) already
# identifies them and no subject is needed.
_SUBJECTLESS_CHECKS = frozenset({"no_refs_store", "yaml-parse", "read", "refs-parse"})


def _subject(f: Finding) -> str:
    """The durable identity of a finding within its (path, check)."""
    for pattern in _SUBJECT_PATTERNS.get(f.check, ()):
        m = re.search(pattern, f.message)
        if m:
            return m.group(1)
    if f.check in _SUBJECTLESS_CHECKS:
        return ""
    # No rule for this check: fall back to the full message. Correct, just
    # churn-prone — tests/test_qc_content.py asserts every check the sweep
    # currently emits has a rule, so this is reachable only by a new check.
    return f.message


def _fingerprint(f: Finding) -> str:
    """Stable identity for a finding, used for baseline matching.

    (path, check, subject) — deliberately *not* the rendered message, so the
    wording of a finding can be improved without the baseline treating it as a
    fix plus a new failure.
    """
    return f"{f.path}\t{f.check}\t{_subject(f)}"


def load_baseline(path: Path) -> set[str]:
    """Read a baseline file of accepted-for-now finding fingerprints."""
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    return set(data.get("accepted", []))


def stale_baseline_entries(path: Path, result: SweepResult) -> set[str]:
    """Baseline entries for findings that no longer occur.

    A stale entry is a live regression hole: it keeps granting a fixed finding
    permission to fail, so re-introducing it passes silently. PMID:28646648 —
    a bacteriophage paper cited as a cell-type definition — became stale the
    moment the trilaminar ingest corrected it, and would have been re-accepted
    without complaint. Report these so the baseline shrinks instead of rotting.
    """
    return load_baseline(path) - {_fingerprint(f) for f in result.trackable}


def _write_baseline_file(path: Path, accepted: list[str]) -> int:
    path.write_text(
        json.dumps(
            {
                "_comment": (
                    "Known content-QC findings accepted at baseline time. "
                    "`just qc-content --baseline` fails only on findings absent "
                    "from this list, so CI catches regressions while the backlog "
                    "is worked down. Remove entries as they are fixed (see "
                    "`just qc-content-prune`); the goal is an empty list, at "
                    "which point drop --baseline from CI."
                ),
                "accepted": sorted(accepted),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return len(accepted)


def write_baseline(path: Path, result: SweepResult) -> int:
    """Record every current finding as accepted. Returns the count written."""
    return _write_baseline_file(path, sorted({_fingerprint(f) for f in result.trackable}))


def prune_baseline(path: Path, kept: list[str]) -> int:
    """Rewrite the baseline with `kept` only. Removes; never accepts."""
    return _write_baseline_file(path, kept)


def _render(result: SweepResult, strict: bool) -> str:
    """Human-readable grouped report."""
    lines: list[str] = []
    sev_order = {ERROR: 0, WARN: 1, GAP: 2}
    by_file: dict[str, list[Finding]] = {}
    for f in result.findings:
        by_file.setdefault(f.path, []).append(f)

    for path in sorted(by_file):
        fs = sorted(by_file[path], key=lambda f: (sev_order[f.severity], f.check))
        n_err = sum(1 for f in fs if f.severity == ERROR)
        n_gap = sum(1 for f in fs if f.severity == GAP)
        n_warn = len(fs) - n_err - n_gap
        lines.append(f"\n{path}  ({n_err} error, {n_warn} warn, {n_gap} gap)")
        for f in fs:
            sev = ERROR if (strict and f.severity == WARN) else f.severity
            lines.append(f"  [{sev:5}] {f.check}: {f.message}")

    lines.append("")
    lines.append("=" * 72)
    lines.append(
        f"Swept {result.kb_files} KB YAML + {result.report_files} reports "
        f"+ {result.ref_stores} reference stores — "
        f"{len(result.errors)} errors, {len(result.warnings)} warnings, "
        f"{len(result.gaps)} known gaps"
    )
    for s in result.skipped:
        lines.append(f"  skipped: {s}")
    if result.unavailable:
        lines.append("")
        lines.append("  CHECKS THAT COULD NOT RUN — these pass vacuously:")
        for u in result.unavailable:
            lines.append(f"    - {u}")
    else:
        lines.append("  all checks had their backing stores available")

    by_check: dict[str, int] = {}
    for f in result.findings:
        by_check[f.check] = by_check.get(f.check, 0) + 1
    if by_check:
        lines.append("  by check: " + ", ".join(
            f"{k}={v}" for k, v in sorted(by_check.items(), key=lambda kv: -kv[1])
        ))
    lines.append("=" * 72)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="qc-content",
        description="Sweep KB YAML and reports for unsupported content "
                    "(quote_keys, PMIDs, DOIs, AT run_refs).",
    )
    ap.add_argument("--kb-only", action="store_true", help="skip reports/")
    ap.add_argument("--reports-only", action="store_true", help="skip kb/")
    ap.add_argument("--no-references", action="store_true",
                    help="skip reference-store integrity checks")
    ap.add_argument("--strict", action="store_true",
                    help="treat warnings as errors (exit 1 on any finding)")
    ap.add_argument("--json", dest="as_json", metavar="PATH", nargs="?", const="-",
                    help="emit findings as JSON to PATH (or stdout with no PATH)")
    ap.add_argument("--baseline", metavar="PATH", nargs="?",
                    const="qc_content_baseline.json",
                    help="fail only on findings absent from this baseline file "
                         "(default path: qc_content_baseline.json)")
    ap.add_argument("--write-baseline", metavar="PATH", nargs="?",
                    const="qc_content_baseline.json",
                    help="record all current findings as accepted, then exit 0")
    ap.add_argument("--prune-baseline", metavar="PATH", nargs="?",
                    const="qc_content_baseline.json",
                    help="drop baseline entries whose findings no longer occur "
                         "(removes only; never accepts anything new)")
    args = ap.parse_args(argv)

    result = run_sweep(
        kb=not args.reports_only,
        reports=not args.kb_only,
        references=not args.no_references,
    )

    if args.as_json:
        payload = {
            "kb_files": result.kb_files,
            "report_files": result.report_files,
            "skipped": result.skipped,
            "unavailable": result.unavailable,
            "errors": len(result.errors),
            "warnings": len(result.warnings),
            "gaps": len(result.gaps),
            "findings": [asdict(f) for f in result.findings],
        }
        text = json.dumps(payload, indent=2)
        if args.as_json == "-":
            print(text)
        else:
            Path(args.as_json).write_text(text + "\n", encoding="utf-8")
            print(f"Wrote {args.as_json}", file=sys.stderr)

    if args.write_baseline:
        n = write_baseline(Path(args.write_baseline), result)
        print(f"Wrote {n} accepted finding(s) to {args.write_baseline}")
        return 0

    if args.prune_baseline:
        bl_path = Path(args.prune_baseline)
        stale = stale_baseline_entries(bl_path, result)
        if not stale:
            print(f"{args.prune_baseline}: nothing stale — no change.")
            return 0
        kept = sorted(load_baseline(bl_path) - stale)
        prune_baseline(bl_path, kept)
        print(f"Pruned {len(stale)} fixed finding(s); {len(kept)} remain:")
        for s in sorted(stale):
            path, check, msg = s.split("\t")
            print(f"  - [{check}] {path}: {msg[:72]}")
        return 0

    if not args.as_json or args.as_json != "-":
        print(_render(result, args.strict))

    failing = [f for f in result.findings
               if f.severity == ERROR or (args.strict and f.severity == WARN)]

    if args.baseline:
        bl_path = Path(args.baseline)
        accepted = load_baseline(bl_path)
        known = [f for f in failing if _fingerprint(f) in accepted]
        failing = [f for f in failing if _fingerprint(f) not in accepted]
        stale = stale_baseline_entries(bl_path, result)
        print(
            f"\nBaseline {args.baseline}: {len(accepted)} accepted, "
            f"{len(known)} matched, {len(failing)} new, {len(stale)} stale"
        )
        if failing:
            print("\nNEW findings not in baseline:")
            for f in failing:
                print(f"  [{f.severity:5}] {f.path}: {f.check}: {f.message}")
        if stale:
            # Not a failure — the underlying content got fixed, which is the
            # goal. But each stale entry is a hole until it is removed.
            one = len(stale) == 1
            print(
                f"\n{len(stale)} baseline entr{'y' if one else 'ies'} no longer "
                f"occur{'s' if one else ''} — fixed. Prune with "
                f"`just qc-content-prune` so {'it cannot' if one else 'they cannot'} "
                f"be silently re-accepted:"
            )
            for s in sorted(stale):
                path, check, msg = s.split("\t")
                print(f"  [{check}] {path}: {msg[:72]}")

    return 1 if failing else 0


if __name__ == "__main__":
    raise SystemExit(main())

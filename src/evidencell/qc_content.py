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
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

from evidencell.paths import at_run_index_path, repo_root
from evidencell.validate import (
    _collect_flat_refs,
    _collect_quote_keys,
    _collect_refs,
    check_flat_ref_pmids,
    check_md_ids,
    check_quote_key_integrity,
    check_quote_keys,
    check_rationale_currency,
    check_ref_pmids,
    check_run_refs,
    parse_md_annotations,
    structural_checks,
)

ERROR = "ERROR"
WARN = "WARN"

# kb/ subtrees that carry no region and therefore no references.json. Bulk atlas
# content (taxonomy levels) is excluded outright: the files are enormous, are
# machine-generated from taxonomy ingest, and carry no provenance fields.
_NO_REGION_SUBTREES = ("datasets", "correlation_runs", "annotation_transfer_runs")
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

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == ERROR]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == WARN]


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
    """
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
        refs_path = root / "references" / region / "references.json"
        # Every provenance check in validate.py returns [] when references.json
        # is absent, so a region without a reference store silently passes all
        # of them — in this sweep *and* in the pre-edit hook. A graph with no
        # citations yet is legitimately unbacked; one that cites papers is not.
        if not refs_path.exists():
            cited = len(_collect_refs(doc)) + len(_collect_quote_keys(doc)) + len(
                _collect_flat_refs(doc)
            )
            if cited:
                findings.append(Finding(
                    rel, ERROR, "no_refs_store",
                    f"references/{region}/references.json does not exist, but this file "
                    f"carries {cited} citation(s)/quote_key(s). Every provenance check is "
                    f"vacuous for region '{region}' — ingest the references to enable them.",
                ))
        for msg in check_quote_keys(doc, refs_path):
            findings.append(Finding(rel, ERROR, "quote_key", msg))
        for msg in check_ref_pmids(doc, refs_path):
            findings.append(Finding(rel, ERROR, "ref_pmid", msg))
        # ERROR, not WARN: #133 proposed warn-only so the 13-entry backlog
        # wouldn't block every subsequent edit, but the baseline file does that
        # job without blunting the check. Leaving these as warnings would let a
        # *newly* hallucinated definition_references PMID pass CI, which is
        # precisely what this sweep exists to stop. The pre-edit hook is
        # unaffected — it does not call check_flat_ref_pmids.
        for msg in check_flat_ref_pmids(doc, refs_path):
            findings.append(Finding(rel, ERROR, "flat_citation", msg))

    for msg in check_rationale_currency(doc):
        findings.append(Finding(rel, WARN, "rationale_stale", msg))

    return findings


def sweep_report_file(path: Path, root: Path) -> list[Finding]:
    """Run markdown annotation + provenance checks on one report."""
    rel = str(path.relative_to(root))
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [Finding(rel, ERROR, "read", str(exc))]

    region = _region_of(path, root)
    if region is None:
        return []

    refs_path = root / "references" / region / "references.json"
    annotations = parse_md_annotations(text)
    kb_nodes = _kb_nodes_for_region(root, region)

    return [
        Finding(rel, ERROR, "markdown", msg)
        for msg in check_md_ids(annotations, refs_path, kb_nodes)
    ]


def _reference_stores(root: Path) -> list[Path]:
    refs = root / "references"
    return sorted(refs.rglob("references.json")) if refs.is_dir() else []


def sweep_reference_store(path: Path, root: Path) -> list[Finding]:
    """Check a reference store's internal integrity.

    Everything else in this sweep validates KB and report content *against* the
    reference store. Nothing validated the store itself — it is the most trusted
    file in the repo and the only one with no write guard, which is how a quote
    whose key attested nothing survived six months.
    """
    rel = str(path.relative_to(root))
    try:
        store = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [Finding(rel, ERROR, "refs-parse", f"invalid JSON: {exc}")]
    except OSError as exc:
        return [Finding(rel, ERROR, "read", str(exc))]

    if not isinstance(store, dict):
        return [Finding(rel, ERROR, "refs-parse", "store is not a JSON object")]

    return [
        Finding(rel, ERROR, "quote_key_integrity", msg)
        for msg in check_quote_key_integrity(store)
    ]


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

    if kb:
        for p in _kb_files(root):
            result.kb_files += 1
            result.findings.extend(sweep_kb_file(p, root))
        for sub in _EXCLUDED_SUBTREES:
            if (root / "kb" / sub).is_dir():
                result.skipped.append(f"kb/{sub}/ (bulk atlas content, no provenance fields)")

    if reports:
        for p in _report_files(root):
            result.report_files += 1
            result.findings.extend(sweep_report_file(p, root))

    if references:
        for p in _reference_stores(root):
            result.ref_stores += 1
            result.findings.extend(sweep_reference_store(p, root))

    return result


def _fingerprint(f: Finding) -> str:
    """Stable identity for a finding, used for baseline matching.

    Deliberately excludes nothing — path + check + message together are what
    makes a finding distinct. Line numbers are not part of any finding, so
    reformatting a file does not churn the baseline.
    """
    return f"{f.path}\t{f.check}\t{f.message}"


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
    return load_baseline(path) - {_fingerprint(f) for f in result.findings}


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
    return _write_baseline_file(path, sorted({_fingerprint(f) for f in result.findings}))


def prune_baseline(path: Path, kept: list[str]) -> int:
    """Rewrite the baseline with `kept` only. Removes; never accepts."""
    return _write_baseline_file(path, kept)


def _render(result: SweepResult, strict: bool) -> str:
    """Human-readable grouped report."""
    lines: list[str] = []
    sev_order = {ERROR: 0, WARN: 1}
    by_file: dict[str, list[Finding]] = {}
    for f in result.findings:
        by_file.setdefault(f.path, []).append(f)

    for path in sorted(by_file):
        fs = sorted(by_file[path], key=lambda f: (sev_order[f.severity], f.check))
        n_err = sum(1 for f in fs if f.severity == ERROR)
        n_warn = len(fs) - n_err
        lines.append(f"\n{path}  ({n_err} error, {n_warn} warn)")
        for f in fs:
            sev = ERROR if (strict and f.severity == WARN) else f.severity
            lines.append(f"  [{sev:5}] {f.check}: {f.message}")

    lines.append("")
    lines.append("=" * 72)
    lines.append(
        f"Swept {result.kb_files} KB YAML + {result.report_files} reports "
        f"+ {result.ref_stores} reference stores — "
        f"{len(result.errors)} errors, {len(result.warnings)} warnings"
    )
    for s in result.skipped:
        lines.append(f"  skipped: {s}")

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
            "errors": len(result.errors),
            "warnings": len(result.warnings),
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

#!/usr/bin/env python3
"""
PreToolUse hook: validates kb/**/*.yaml and reports/**/*.md BEFORE edits are applied.

YAML checks (in order):
1. YAML parse validity
2. Structural integrity (duplicate IDs, dangling edges, placeholder snippets, accessions)
3. Quote key provenance: every quote_key must exist in references.json
4. Reference PMID/DOI provenance: every PMID:/DOI: ref must exist in references.json
5. LinkML schema conformance (subprocess; skipped if schema file absent)

Markdown report checks:
1. Unannotated blockquotes (missing <!-- quote_key: X --> annotation)
2. Quote key existence in references.json
3. PMID existence in references.json
4. Ontology CURIE existence in term_index.json (if present)
5. Atlas accession existence in KB nodes (if discoverable)

Returns exit code 2 to BLOCK the edit if any check fails.
https://docs.anthropic.com/en/docs/claude-code/hooks#exit-code-2-behavior
"""

import sys
import json
from pathlib import Path

# Add project src/ to path so we can import evidencell.validate
_project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_project_root / "src"))

import yaml  # noqa: E402
from evidencell.validate import (  # noqa: E402
    simulate_edit,
    structural_checks,
    check_quote_keys,
    check_ref_pmids,
    linkml_validate,
    parse_md_annotations,
    check_md_ids,
)


def main():
    data = json.load(sys.stdin)
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    if tool_name not in ["Write", "Edit", "MultiEdit"]:
        sys.exit(0)

    file_path_str = tool_input.get("file_path", "")
    if not file_path_str:
        sys.exit(0)

    file_path = Path(file_path_str)

    is_yaml = "/kb/" in str(file_path) and file_path.suffix == ".yaml"
    is_report = (
        "/reports/" in str(file_path)
        and file_path.suffix == ".md"
    )

    if not is_yaml and not is_report:
        sys.exit(0)

    schema_path = _project_root / "schema" / "celltype_mapping.yaml"

    # Simulate the post-edit content using validate.py
    simulated = simulate_edit(tool_name, tool_input, file_path)

    print("\n" + "=" * 60, file=sys.stderr)
    print(f"Pre-Edit Validation: {file_path.name}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    errors_found = False

    # Derive refs_path from new directory layout.
    # Infer the repo root from the file path (not __file__) so tests with
    # tmp_path fixtures work correctly.
    def _repo_root_from_path(fp: Path, marker: str) -> Path:
        """Walk up from fp to find the parent directory of marker (e.g. 'kb')."""
        parts = fp.resolve().parts
        for i, part in enumerate(parts):
            if part == marker:
                return Path(*parts[:i]) if i > 0 else Path("/")
        return _project_root  # fallback to hook-relative root

    if is_report:
        # reports/{region}/*.md → references/{region}/references.json
        region = file_path.parent.name
        inferred_root = _repo_root_from_path(file_path, "reports")
        refs_path = inferred_root / "references" / region / "references.json"
    else:
        # kb/draft/{region}/*.yaml → references/{region}/references.json
        region = file_path.parent.name
        inferred_root = _repo_root_from_path(file_path, "kb")
        refs_path = inferred_root / "references" / region / "references.json"

    if is_report:
        # ── Markdown report validation ─────────────────────────────────────
        annotations = parse_md_annotations(simulated)

        # Collect known KB accessions from kb/draft/{region}/ and kb/mappings/{region}/
        kb_nodes: dict | None = None
        try:
            kb_nodes = {}
            for base in ("draft", "mappings"):
                kb_region_dir = inferred_root / "kb" / base / region
                if kb_region_dir.is_dir():
                    for yf in kb_region_dir.glob("*.yaml"):
                        try:
                            import yaml as _yaml
                            y = _yaml.safe_load(yf.read_text(encoding="utf-8"))
                            for node in (y or {}).get("nodes", []):
                                acc = node.get("cell_set_accession")
                                if acc:
                                    kb_nodes[acc] = node
                        except Exception:
                            pass
        except Exception:
            kb_nodes = None

        md_errors = check_md_ids(annotations, refs_path, kb_nodes)
        if md_errors:
            print("Markdown annotation errors:", file=sys.stderr)
            for e in md_errors:
                print(f"  - {e}", file=sys.stderr)
            errors_found = True

    else:
        # ── YAML KB validation ─────────────────────────────────────────────
        doc: dict | None = None

        # 1. YAML parse + structural integrity (fast, no subprocess)
        try:
            doc = yaml.safe_load(simulated)
            if isinstance(doc, dict):
                struct_errors = structural_checks(doc)
                if struct_errors:
                    print("Structural errors:", file=sys.stderr)
                    for e in struct_errors:
                        print(f"  - {e}", file=sys.stderr)
                    errors_found = True
        except yaml.YAMLError as exc:
            print(f"YAML parse error: {exc}", file=sys.stderr)
            errors_found = True

        # 2. Quote key provenance (fast, local references.json lookup)
        if isinstance(doc, dict):
            qk_errors = check_quote_keys(doc, refs_path)
            if qk_errors:
                print("Quote key errors:", file=sys.stderr)
                for e in qk_errors:
                    print(f"  - {e}", file=sys.stderr)
                errors_found = True

        # 3. Reference PMID/DOI provenance (fast, local references.json lookup)
        if isinstance(doc, dict):
            ref_errors = check_ref_pmids(doc, refs_path)
            if ref_errors:
                print("Reference provenance errors:", file=sys.stderr)
                for e in ref_errors:
                    print(f"  - {e}", file=sys.stderr)
                errors_found = True

        # 4. LinkML schema validation (subprocess)
        ok, output = linkml_validate(simulated, schema_path, file_path.name)
        if output.strip():
            print(output.strip(), file=sys.stderr)
        if not ok:
            errors_found = True

    if errors_found:
        print("=" * 60, file=sys.stderr)
        print("BLOCKING EDIT: Validation failed", file=sys.stderr)
        print("Fix the issues above before proceeding.", file=sys.stderr)
        print("=" * 60 + "\n", file=sys.stderr)
        sys.exit(2)

    print("Validation passed - allowing edit", file=sys.stderr)
    print("=" * 60 + "\n", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()

"""Batch LinkML validation — load the schema once, validate many files.

`just validate-all` previously spawned one `linkml-validate` subprocess per
file, so schema compilation (the dominant cost) was repeated per file. That was
tolerable at 14 KB graph files; one file per component takes the corpus to ~64,
where the per-spawn overhead dominates.

Handles `.yaml.gz` transparently, which the `linkml-validate` CLI cannot read.
"""

from __future__ import annotations

import gzip
import sys
from pathlib import Path

import yaml


def _load(path: Path) -> object:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def validate_files(
    schema: Path,
    files: list[Path],
    *,
    target_class: str | None = None,
) -> dict[Path, list[str]]:
    """Validate each file against `schema`. Returns {path: [messages]}.

    A file with no messages passed. A file that could not be read or parsed
    reports that as its message rather than being skipped — a validator that
    silently passes on unreadable input is worse than no validator.
    """
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    # The plugin list MUST be passed explicitly. Validator.iter_results_from_source
    # opens with `if not self._validation_plugins: return []`, so a Validator built
    # without plugins reports every instance as valid -- it validates nothing while
    # looking like it passed. closed=True matches the linkml-validate CLI default
    # (undeclared slots are rejected).
    validator = Validator(
        str(schema),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )
    results: dict[Path, list[str]] = {}
    for path in files:
        try:
            instance = _load(path)
        except Exception as exc:
            results[path] = [f"could not read/parse: {exc}"]
            continue
        if instance is None:
            results[path] = ["file is empty"]
            continue
        try:
            report = validator.validate(instance, target_class=target_class)
        except Exception as exc:
            results[path] = [f"validation error: {exc}"]
            continue
        results[path] = [r.message for r in report.results]
    return results


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m evidencell.validate_batch",
        description="Validate many YAML files against one LinkML schema.",
    )
    parser.add_argument("-s", "--schema", type=Path, required=True)
    parser.add_argument("-C", "--target-class", default=None)
    parser.add_argument("files", type=Path, nargs="+")
    parser.add_argument(
        "-q", "--quiet", action="store_true",
        help="Only print files with problems.",
    )
    args = parser.parse_args(argv)

    results = validate_files(
        args.schema, args.files, target_class=args.target_class
    )
    failed = 0
    for path, messages in results.items():
        if messages:
            failed += 1
            print(f"Validating {path}...")
            for message in messages:
                print(f"  {message}")
        elif not args.quiet:
            print(f"Validating {path}...")
            print("No issues found")

    total = len(results)
    if failed:
        print(f"Validation failed: {failed} of {total} file(s) have problems.")
        return 1
    print(f"All {total} KB files valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

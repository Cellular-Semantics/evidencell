# evidencell justfile
# Thin task runner — all non-trivial logic lives in src/evidencell/

schema    := "schema/celltype_mapping.yaml"
kb_dir    := "kb/mappings"   # canonical, validated entries only
draft_dir := "kb/draft"      # work-in-progress; graduate to kb/mappings/ after just qc

# List all commands (default)
_default:
    @just --list

# ── Setup ──────────────────────────────────────────────────────────────────────

# Install all dependencies
[group('setup')]
install:
    uv sync --all-groups

# Download OAK SQLite databases for CL, UBERON, NCBITaxon
# Run once after install; databases are large and not committed to git
[group('setup')]
fetch-oak-dbs:
    mkdir -p conf/oak_dbs
    uv run python -c "import oaklib; print('oaklib version:', oaklib.__version__)"
    @echo "Run the following to pre-cache OAK SQLite DBs (large download):"
    @echo "  uv run runoak -i sqlite:obo:cl info CL:0000000"
    @echo "  uv run runoak -i sqlite:obo:uberon info UBERON:0000955"
    @echo "  uv run runoak -i sqlite:obo:ncbitaxon info NCBITaxon:9606"
    @echo "OAK caches DBs in ~/.data/oaklib/ automatically on first use."

# ── Validation ─────────────────────────────────────────────────────────────────

# Validate a single KB YAML file against the schema
[group('validation')]
validate FILE:
    uv run linkml-validate -s {{schema}} {{FILE}}

# Validate all canonical KB files (kb/mappings/)
[group('validation')]
validate-all:
    #!/usr/bin/env bash
    set -euo pipefail
    files=$(find {{kb_dir}} -name "*.yaml" 2>/dev/null)
    if [ -z "$files" ]; then echo "No files in {{kb_dir}} yet."; exit 0; fi
    failed=0
    for f in $files; do
        echo "Validating $f..."
        uv run linkml-validate -s {{schema}} "$f" || failed=1
    done
    [ $failed -eq 0 ] && echo "All canonical KB files valid." || { echo "Validation failed."; exit 1; }

# Validate all draft KB files (kb/draft/)
[group('validation')]
validate-draft:
    #!/usr/bin/env bash
    set -euo pipefail
    files=$(find {{draft_dir}} -name "*.yaml" 2>/dev/null)
    if [ -z "$files" ]; then echo "No files in {{draft_dir}} yet."; exit 0; fi
    failed=0
    for f in $files; do
        echo "Validating $f..."
        uv run linkml-validate -s {{schema}} "$f" || failed=1
    done
    [ $failed -eq 0 ] && echo "All draft KB files valid." || { echo "One or more draft files failed validation."; exit 1; }

# Validate ontology terms (CL, UBERON, NCBITaxon) in canonical KB files
# Requires OAK SQLite DBs (run just fetch-oak-dbs first)
[group('validation')]
validate-terms:
    uv run linkml-term-validator --config conf/oak_config.yaml --schema {{schema}} {{kb_dir}}

# Validate ontology terms in draft KB files
[group('validation')]
validate-terms-draft:
    uv run linkml-term-validator --config conf/oak_config.yaml --schema {{schema}} {{draft_dir}}

# Validate ontology terms in a single file
[group('validation')]
validate-terms-file FILE:
    uv run linkml-term-validator --config conf/oak_config.yaml --schema {{schema}} {{FILE}}

# ── QC (full suite) ────────────────────────────────────────────────────────────

# QC gate for canonical KB (kb/mappings/) — must pass before committing
[group('qc')]
qc: validate-all validate-terms
    @echo "All QC checks passed."

# QC run over draft files — informational; failures do not block commits
[group('qc')]
qc-draft: validate-draft validate-terms-draft
    @echo "Draft QC complete."

# ── Tests ──────────────────────────────────────────────────────────────────────

# Run pytest
[group('testing')]
test:
    uv run pytest

# ── Utilities ──────────────────────────────────────────────────────────────────

# Pretty-print a KB file (YAML round-trip sanity check)
[group('utilities')]
inspect FILE:
    uv run python -c "import yaml, sys; yaml.dump(yaml.safe_load(open('{{FILE}}')), sys.stdout, allow_unicode=True, sort_keys=False)"

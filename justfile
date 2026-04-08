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
    uv run linkml-term-validator validate --config conf/oak_config.yaml --schema {{schema}} {{kb_dir}}

# Validate ontology terms in draft KB files
[group('validation')]
validate-terms-draft:
    uv run linkml-term-validator validate --config conf/oak_config.yaml --schema {{schema}} {{draft_dir}}

# Validate ontology terms in a single file
[group('validation')]
validate-terms-file FILE:
    uv run linkml-term-validator validate --config conf/oak_config.yaml --schema {{schema}} {{FILE}}

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

# Run pytest (full suite with coverage)
[group('testing')]
test:
    uv run pytest

# Run only tool-interface smoke tests — fast, no KB data or OAK DBs required
# Use this to verify CLI invocations haven't broken after dependency updates
[group('testing')]
smoke:
    uv run pytest tests/test_tool_interfaces.py -v --no-cov

# Run all tests except those marked integration (OAK DB / network)
[group('testing')]
test-fast:
    uv run pytest -m "not integration" --no-cov

# ── Workflows ──────────────────────────────────────────────────────────────────

# Validate a node exists and show its context before running lit-review
# Usage: just research-celltype <node_id> "<topic>"
# Then tell Claude: "Run workflows/lit-review.md for node_id=<node_id> topic=<topic>"
[group('workflows')]
research-celltype node_id topic:
    #!/usr/bin/env bash
    set -euo pipefail
    kb_file=$(grep -rl "id: {{node_id}}" kb/ --include="*.yaml" 2>/dev/null | head -1 || true)
    if [ -z "$kb_file" ]; then
        echo "ERROR: node '{{node_id}}' not found in kb/"
        echo "Available node IDs:"
        grep -rh "^  - id:" kb/ --include="*.yaml" | sed 's/  - id: /    /' | sort
        exit 1
    fi
    echo ""
    echo "Node:   {{node_id}}  ($kb_file)"
    echo "Topic:  {{topic}}"
    echo ""
    uv run python -m evidencell.show_node "$kb_file" "{{node_id}}"
    echo ""
    echo "Inputs validated. Proceeding with workflows/lit-review.md"

# Validate inputs and show context for asta-report-ingest.md
# Usage: just ingest-report <region> <pdf_file>
# pdf_file relative to repo root, e.g. inputs/deepsearch/OLM_Neurons_asta_report.pdf
# Claude runs this recipe first, then follows workflows/asta-report-ingest.md
[group('workflows')]
ingest-report region pdf_file:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ ! -f "{{pdf_file}}" ]; then
        echo "ERROR: PDF not found at '{{pdf_file}}'"
        echo "Place ASTA deep research PDFs in inputs/deepsearch/"
        exit 1
    fi
    echo "=== ingest-report ==="
    echo "Region: {{region}}"
    echo "PDF:    {{pdf_file}}"
    echo ""
    echo "Existing KB nodes in region (if any):"
    grep -rh "^  - id:" kb/ --include="*.yaml" 2>/dev/null | grep -i "{{region}}" | sed 's/  - id: /    /' | sort || echo "    (none yet)"
    echo ""
    echo "Inputs validated. Proceeding with workflows/asta-report-ingest.md"

# ── Reports ────────────────────────────────────────────────────────────────────

# Extract structured report facts JSON (input to synthesis subagent in gen-report workflow)
[group('reports')]
gen-facts GRAPH_FILE NODE_ID:
    uv run python -m evidencell.render facts {{GRAPH_FILE}} --node {{NODE_ID}}

# Generate summary report for all classical nodes in one graph file (programmatic mode)
# For LLM-assisted synthesis with hallucination guard, use: workflows/gen-report.md
[group('reports')]
gen-report GRAPH_FILE:
    uv run python -m evidencell.render summary {{GRAPH_FILE}}

# Generate summary report for one classical node by id
[group('reports')]
gen-report-node GRAPH_FILE NODE_ID:
    uv run python -m evidencell.render summary {{GRAPH_FILE}} --node {{NODE_ID}}

# Generate all drill-downs for a classical node
[group('reports')]
gen-drilldowns GRAPH_FILE NODE_ID:
    uv run python -m evidencell.render drilldowns {{GRAPH_FILE}} --node {{NODE_ID}}

# Generate a single drill-down by PMID
[group('reports')]
gen-drilldown-pmid GRAPH_FILE NODE_ID PMID:
    uv run python -m evidencell.render drilldowns {{GRAPH_FILE}} --node {{NODE_ID}} --pmid {{PMID}}

# Generate region index listing all classical types with links to summary reports
[group('reports')]
gen-index REGION:
    uv run python -m evidencell.render index {{REGION}}

# Regenerate all reports + indices for canonical KB (programmatic mode, no LLM)
[group('reports')]
gen-report-all:
    #!/usr/bin/env bash
    set -euo pipefail
    files=$(find kb/mappings -name "*.yaml" 2>/dev/null)
    if [ -z "$files" ]; then echo "No files in kb/mappings yet."; exit 0; fi
    for f in $files; do
        uv run python -m evidencell.render summary "$f"
    done
    for region in $(ls kb/mappings 2>/dev/null); do
        uv run python -m evidencell.render index "$region"
    done

# Regenerate all reports + indices for draft KB (programmatic mode, no LLM)
# Use this during active curation before content graduates to kb/mappings/
[group('reports')]
gen-report-draft REGION:
    #!/usr/bin/env bash
    set -euo pipefail
    files=$(find kb/draft/{{REGION}} -maxdepth 1 -name "*.yaml" 2>/dev/null)
    if [ -z "$files" ]; then echo "No YAML files in kb/draft/{{REGION}}."; exit 0; fi
    for f in $files; do
        uv run python -m evidencell.render summary "$f"
    done
    uv run python -m evidencell.render index {{REGION}}

# Generate all drill-downs for a classical node in a draft graph
[group('reports')]
gen-drilldowns-draft GRAPH_FILE NODE_ID:
    uv run python -m evidencell.render drilldowns {{GRAPH_FILE}} --node {{NODE_ID}}

# ── Annotation Transfer ───────────────────────────────────────────────────────

# Run preflight resource check on a dataset file
[group('annotation-transfer')]
at-preflight FILE:
    cd annotation_transfer && uv run annotation-transfer preflight {{FILE}}

# Convert h5ad to MapMyCells-ready format
[group('annotation-transfer')]
at-convert INPUT OUTPUT *ARGS:
    cd annotation_transfer && uv run annotation-transfer convert {{INPUT}} {{OUTPUT}} {{ARGS}}

# Compute F1 matrix from MapMyCells output
[group('annotation-transfer')]
at-score MMC_CSV LABELS OUTPUT *ARGS:
    cd annotation_transfer && uv run annotation-transfer score {{MMC_CSV}} {{LABELS}} {{OUTPUT}} {{ARGS}}

# Run annotation transfer tests
[group('annotation-transfer')]
at-test:
    cd annotation_transfer && uv run pytest -v

# ── Utilities ──────────────────────────────────────────────────────────────────

# Pretty-print a KB file (YAML round-trip sanity check)
[group('utilities')]
inspect FILE:
    uv run python -c "import yaml, sys; yaml.dump(yaml.safe_load(open('{{FILE}}')), sys.stdout, allow_unicode=True, sort_keys=False)"

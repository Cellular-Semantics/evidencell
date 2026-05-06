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

# Install git hooks (pre-commit schema validation)
[group('setup')]
install-hooks:
    cp hooks/pre-commit .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    @echo "Git hooks installed."

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

# Validate a taxonomy YAML file (TaxonomyNodeList root class)
[group('validation')]
validate-taxonomy FILE:
    uv run linkml-validate -s {{schema}} -C TaxonomyNodeList {{FILE}}

# Validate all taxonomy YAML files for a taxonomy ID
[group('validation')]
validate-taxonomy-all TAXONOMY_ID:
    #!/usr/bin/env bash
    set -euo pipefail
    dir="kb/taxonomy/{{TAXONOMY_ID}}"
    files=$(find "$dir" -maxdepth 1 -name "*.yaml" ! -name "taxonomy_meta.yaml" ! -name "field_mapping.yaml" 2>/dev/null)
    if [ -z "$files" ]; then echo "No taxonomy YAML files in $dir."; exit 0; fi
    failed=0
    for f in $files; do
        echo "Validating $f..."
        uv run linkml-validate -s {{schema}} -C TaxonomyNodeList "$f" || failed=1
    done
    [ $failed -eq 0 ] && echo "All taxonomy files valid." || { echo "Validation failed."; exit 1; }

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

# ── Taxonomy reference DB (M8) ─────────────────────────────────────────────────

# Fetch taxonomy JSON from local brain_cell_KG via Cypher query
# Requires: [kg] optional deps — run once: uv sync --extra kg
# Requires: local neo4j KG running at bolt://localhost:7687
# Usage: just fetch-taxonomy-kg inputs/taxonomies/CCN20230722.cypher CCN20230722
[group('workflows')]
fetch-taxonomy-kg cypher_file taxonomy_id *ARGS:
    uv run python -m evidencell.kg_query fetch {{cypher_file}} {{taxonomy_id}} {{ARGS}}

# Ingest taxonomy JSON → compact YAML reference files in kb/taxonomy/{taxonomy_id}/
# Usage: just ingest-taxonomy-yaml inputs/taxonomies/CCN20230722.json CCN20230722
[group('workflows')]
ingest-taxonomy-yaml taxonomy_file taxonomy_id:
    uv run python -m evidencell.taxonomy_db ingest {{taxonomy_file}} {{taxonomy_id}}

# Build SQLite query index from YAML reference files (no source JSON required)
# Usage: just build-taxonomy-db CCN20230722
[group('workflows')]
build-taxonomy-db taxonomy_id:
    uv run python -m evidencell.taxonomy_db build-db {{taxonomy_id}}

# Ingest taxonomy JSON and build SQLite index in one step
# Usage: just ingest-taxonomy-db inputs/taxonomies/wmbv1_full.json CCN20230722
[group('workflows')]
ingest-taxonomy-db taxonomy_file taxonomy_id:
    just ingest-taxonomy-yaml {{taxonomy_file}} {{taxonomy_id}}
    just build-taxonomy-db {{taxonomy_id}}

# Download the latest BICAN Mouse Brain Atlas Ontology (OBO JSON) to conf/mba/mbao-full.json
# Run once; file is not committed to git (.gitignore)
[group('workflows')]
fetch-mba-ontology:
    uv run python -m evidencell.taxonomy_db fetch-mba conf/mba/mbao-full.json

# Build anat hierarchy + transitive closure tables from the downloaded MBA ontology
# Requires: just build-taxonomy-db <taxonomy_id> and just fetch-mba-ontology
# Usage: just build-anat-closure CCN20230722
[group('workflows')]
build-anat-closure taxonomy_id:
    uv run python -m evidencell.taxonomy_db build-closure {{taxonomy_id}} conf/mba/mbao-full.json

# ── Taxonomy update operations ────────────────────────────────────────────────

# Add precomputed expression profiles to taxonomy nodes from HDF5 stats
# Requires: gene mapping TSV (generate with just generate-gene-mapping)
# Usage: just add-expression CCN20230722 path/to/stats.h5 path/to/gene_mapping.tsv Sst Pvalb Cck
[group('workflows')]
add-expression taxonomy_id stats_h5 gene_mapping +GENES:
    uv run python -m evidencell.taxonomy_ops add-expression {{taxonomy_id}} {{stats_h5}} {{gene_mapping}} {{GENES}}

# Add expression to both cluster and supertype levels
# Usage: just add-expression-all CCN20230722 path/to/stats.h5 path/to/gene_mapping.tsv Sst Pvalb
[group('workflows')]
add-expression-all taxonomy_id stats_h5 gene_mapping +GENES:
    uv run python -m evidencell.taxonomy_ops add-expression {{taxonomy_id}} {{stats_h5}} {{gene_mapping}} {{GENES}} --supertype

# Re-ingest taxonomy from source JSON, preserving enrichment fields
# Usage: just reingest CCN20230722 inputs/taxonomies/wmbv1_full_v2.json
[group('workflows')]
reingest taxonomy_id source_json *ARGS:
    uv run python -m evidencell.taxonomy_ops reingest {{taxonomy_id}} {{source_json}} {{ARGS}}

# Re-ingest (dry run) — report changes without writing
# Usage: just reingest-dry CCN20230722 inputs/taxonomies/wmbv1_full_v2.json
[group('workflows')]
reingest-dry taxonomy_id source_json:
    uv run python -m evidencell.taxonomy_ops reingest {{taxonomy_id}} {{source_json}} --dry-run

# Generate gene mapping TSV from HDF5 stats via mygene API
# Run once per stats file; output reusable across add-expression calls
# Requires: uv add mygene
# Usage: just generate-gene-mapping path/to/stats.h5 conf/gene_mapping_CCN20230722.tsv
[group('workflows')]
generate-gene-mapping stats_h5 output:
    uv run python -m evidencell.taxonomy_ops generate-gene-mapping {{stats_h5}} {{output}}

# Find candidate atlas matches for a classical node by querying the taxonomy DB
# Extracts the node's property signature (markers, NT, anatomy) and scores taxonomy entries
# rank: 0 = leaf (cluster in WMBv1), 1 = supertype, 2 = subclass, 3 = class
# Usage: just find-candidates kb/draft/hippocampus/hippocampus_OLM.yaml olm_hippocampus CCN20230722
#        just find-candidates kb/draft/hippocampus/hippocampus_OLM.yaml olm_hippocampus CCN20230722 0 30
[group('workflows')]
find-candidates graph_file node_id taxonomy_id rank="1" top_n="20":
    uv run python -m evidencell.taxonomy_db find-candidates {{graph_file}} {{node_id}} {{taxonomy_id}} {{rank}} {{top_n}}

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

# Generate a taxonomy-indexed contents page for mapping reports
# Usage: just gen-toc CCN20230722
#        just gen-toc CCN20230722 --root CS20230722_CLAS_07
#        just gen-toc CCN20230722 --min-confidence HIGH
# Output: reports/_toc/{taxonomy_id}[_{root}].md
[group('reports')]
gen-toc TAXONOMY_ID *ARGS:
    uv run python -m evidencell.toc {{TAXONOMY_ID}} {{ARGS}}

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
    # Combined taxonomy-indexed TOC (default MODERATE+).
    uv run python -m evidencell.toc --all

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

# ── CL term requests ──────────────────────────────────────────────────────────

# Preview a drafted CL new term request without posting (default — safe).
# Output is rendered from workflows/cl-term-request.md.
[group('reports')]
preview-cl-ntr NTR_FILE:
    uv run python -m evidencell.cl_post {{NTR_FILE}}

# Post a drafted CL new term request as a GitHub issue against
# obophenotype/cell-ontology. Requires CELLSEM_GH_TOKEN in the environment.
# Always preview with `just preview-cl-ntr` first.
[group('reports')]
post-cl-ntr NTR_FILE:
    uv run python -m evidencell.cl_post {{NTR_FILE}} --confirm

# ── Annotation Transfer ───────────────────────────────────────────────────────

# Run preflight resource check on a dataset file
[group('annotation-transfer')]
at-preflight FILE:
    cd annotation_transfer && uv run annotation-transfer preflight {{FILE}}

# Convert h5ad to MapMyCells-ready format
[group('annotation-transfer')]
at-convert INPUT OUTPUT *ARGS:
    cd annotation_transfer && uv run annotation-transfer convert {{INPUT}} {{OUTPUT}} {{ARGS}}

# Run MapMyCells via web API or local (taxonomy-aware)
[group('annotation-transfer')]
at-map INPUT TAXONOMY OUTPUT_DIR *ARGS:
    cd annotation_transfer && uv run annotation-transfer map {{INPUT}} {{TAXONOMY}} {{OUTPUT_DIR}} {{ARGS}}

# Run MapMyCells locally (backward-compatible, requires cell_type_mapper)
[group('annotation-transfer')]
at-map-local INPUT STATS MARKERS OUTPUT_JSON *ARGS:
    cd annotation_transfer && uv run annotation-transfer map-local {{INPUT}} {{STATS}} {{MARKERS}} {{OUTPUT_JSON}} {{ARGS}}

# Compute F1 matrix from MapMyCells output
[group('annotation-transfer')]
at-score MMC_CSV LABELS OUTPUT *ARGS:
    cd annotation_transfer && uv run annotation-transfer score {{MMC_CSV}} {{LABELS}} {{OUTPUT}} {{ARGS}}

# Subsample h5ad for web API limits
[group('annotation-transfer')]
at-subsample INPUT OUTPUT *ARGS:
    cd annotation_transfer && uv run annotation-transfer subsample {{INPUT}} {{OUTPUT}} {{ARGS}}

# Configure a taxonomy for mapping
[group('annotation-transfer')]
at-taxonomy-setup TAXONOMY_ID *ARGS:
    cd annotation_transfer && uv run annotation-transfer taxonomy-setup {{TAXONOMY_ID}} {{ARGS}}

# Download MapMyCells taxonomy files to conf/mapmycells/{taxonomy_id}/ and update
# both the AT taxonomy spec and kb/taxonomy/{taxonomy_id}/taxonomy_meta.yaml
# Usage: just at-download-taxonomy CCN20230722
[group('annotation-transfer')]
at-download-taxonomy TAXONOMY_ID:
    cd annotation_transfer && uv run annotation-transfer taxonomy-setup {{TAXONOMY_ID}} --download
    uv run python -m evidencell.taxonomy_db sync-mapmycells-paths {{TAXONOMY_ID}}

# List known taxonomies
[group('annotation-transfer')]
at-taxonomy-list:
    cd annotation_transfer && uv run annotation-transfer taxonomy-list

# Run annotation transfer tests
[group('annotation-transfer')]
at-test:
    cd annotation_transfer && uv run pytest -v

# Build/rebuild kb/annotation_transfer_runs/index.yaml from manifest files.
# Run after adding a new AT run directory.
[group('annotation-transfer')]
register-at-run:
    uv run python -m evidencell.taxonomy_ops build-at-index

# ── Utilities ──────────────────────────────────────────────────────────────────

# Pretty-print a KB file (YAML round-trip sanity check)
[group('utilities')]
inspect FILE:
    uv run python -c "import yaml, sys; yaml.dump(yaml.safe_load(open('{{FILE}}')), sys.stdout, allow_unicode=True, sort_keys=False)"

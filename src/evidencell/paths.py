"""Single source of truth for evidencell directory conventions.

All path logic that maps between graph YAML, references, research
artefacts, and reports lives here.
"""

from pathlib import Path
import yaml


def repo_root() -> Path:
    """Walk up from this file to find the repo root (contains schema/)."""
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "schema").is_dir():
            return p
        p = p.parent
    raise RuntimeError("Cannot locate repo root (no schema/ directory found)")


def find_node_file(node_id: str) -> Path:
    """Return the YAML file that contains the CellTypeNode with this node_id.

    This is the stable interface between workflows and KB file layout.
    Workflows should always call this rather than constructing paths directly —
    the implementation will change as the KB is restructured:

      Phase 0 (current): scan kb/draft/ and kb/mappings/ for a YAML containing
        the node_id. Slow for large corpora but correct.
      Phase 1 (post-M8): query kb/index.db (SQLite node→file map). Fast O(1).
      Phase 2 (post-M7): direct path kb/nodes/{region}/{node_id}.yaml.

    Raises FileNotFoundError if no YAML in the KB contains the node_id.
    """
    root = repo_root()
    for kb_dir in (root / "kb" / "draft", root / "kb" / "mappings"):
        if not kb_dir.exists():
            continue
        for yaml_file in sorted(kb_dir.rglob("*.yaml")):
            try:
                with yaml_file.open() as fh:
                    data = yaml.safe_load(fh)
            except Exception:
                continue
            nodes = data.get("nodes", []) if isinstance(data, dict) else []
            for node in nodes:
                if isinstance(node, dict) and node.get("id") == node_id:
                    return yaml_file
    raise FileNotFoundError(
        f"Node '{node_id}' not found in any KB YAML under kb/draft/ or kb/mappings/. "
        "Check node_id spelling or run 'just qc' to validate the KB."
    )


def region_from_graph(graph_file: Path) -> str:
    """Extract region name from a KB graph path.

    kb/draft/{region}/foo.yaml  → region
    kb/mappings/{region}/foo.yaml → region
    """
    parts = graph_file.resolve().parts
    for i, part in enumerate(parts):
        if part == "kb" and i + 2 < len(parts):
            # kb / (draft|mappings) / region / ...
            return parts[i + 2]
    raise ValueError(f"Cannot extract region from graph path: {graph_file}")


def refs_path_for_graph(graph_file: Path) -> Path:
    """Return the references.json path for a given graph YAML file."""
    region = region_from_graph(graph_file)
    return repo_root() / "references" / region / "references.json"


def refs_path_for_region(region: str) -> Path:
    """Return the references.json path for a named region."""
    return repo_root() / "references" / region / "references.json"


def reports_dir_for_region(region: str) -> Path:
    """Return the reports directory for a named region."""
    return repo_root() / "reports" / region


def research_dir_for_region(region: str) -> Path:
    """Return the research directory for a named region."""
    return repo_root() / "research" / region

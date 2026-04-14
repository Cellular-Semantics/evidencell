"""Single source of truth for evidencell directory conventions.

All path logic that maps between graph YAML, references, research
artefacts, and reports lives here.
"""

from pathlib import Path


def repo_root() -> Path:
    """Walk up from this file to find the repo root (contains schema/)."""
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "schema").is_dir():
            return p
        p = p.parent
    raise RuntimeError("Cannot locate repo root (no schema/ directory found)")


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

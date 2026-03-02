from __future__ import annotations

from pathlib import Path
import networkx as nx

from ardx.analysis.graph_metrics import compute_metrics
from ardx.utils.io import export_dataframe


def run_analyze(config: dict) -> dict[str, Path]:
    output_dir = Path(config.get("paths", {}).get("output_dir", "outputs"))
    graph_dir = output_dir / "graphs"
    metrics_dir = output_dir / "metrics"

    out = {}
    for name in ["retweet", "mention"]:
        gpath = graph_dir / f"{name}.gexf"
        if not gpath.exists():
            continue
        g = nx.read_gexf(gpath)
        metrics = compute_metrics(g)
        base = metrics_dir / f"{name}_metrics"
        export_dataframe(metrics, base)
        out[name] = base.with_suffix(".csv")
    return out

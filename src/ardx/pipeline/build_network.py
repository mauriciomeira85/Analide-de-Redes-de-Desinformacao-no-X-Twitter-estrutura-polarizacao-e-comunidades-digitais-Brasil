from __future__ import annotations

from pathlib import Path
import pandas as pd

from ardx.analysis.graph_metrics import build_graphs
from ardx.utils.io import export_graph


def run_build_network(config: dict) -> dict[str, Path]:
    output_dir = Path(config.get("paths", {}).get("output_dir", "outputs"))
    input_csv = output_dir / "raw" / "posts.csv"
    if not input_csv.exists():
        raise FileNotFoundError(f"Arquivo de coleta não encontrado: {input_csv}")

    df = pd.read_csv(input_csv)
    graphs = build_graphs(df)

    out = {}
    for name, g in graphs.items():
        path = output_dir / "graphs" / f"{name}.gexf"
        export_graph(g, path)
        out[name] = path
    return out

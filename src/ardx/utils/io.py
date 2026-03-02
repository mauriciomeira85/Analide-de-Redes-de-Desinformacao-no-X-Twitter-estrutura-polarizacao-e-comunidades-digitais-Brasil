from __future__ import annotations

from pathlib import Path
import pandas as pd
import networkx as nx


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def export_dataframe(df: pd.DataFrame, out_base: Path) -> None:
    out_base.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_base.with_suffix(".csv"), index=False)
    try:
        df.to_parquet(out_base.with_suffix(".parquet"), index=False)
    except Exception as exc:
        print(f"[warn] Falha ao exportar parquet ({out_base}): {exc}")


def export_graph(g: nx.DiGraph, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    nx.write_gexf(g, out_path)

from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def run_visualize(config: dict) -> list[Path]:
    output_dir = Path(config.get("paths", {}).get("output_dir", "outputs"))
    metrics_dir = output_dir / "metrics"
    figs_dir = output_dir / "figures"
    figs_dir.mkdir(parents=True, exist_ok=True)

    generated = []
    for name in ["retweet", "mention"]:
        csv_path = metrics_dir / f"{name}_metrics.csv"
        if not csv_path.exists():
            continue
        df = pd.read_csv(csv_path).head(20)
        if df.empty:
            continue

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(df["node"].astype(str), df["pagerank"])
        ax.set_title(f"Top PageRank - {name}")
        ax.set_xlabel("Nó")
        ax.set_ylabel("PageRank")
        ax.tick_params(axis="x", rotation=90)
        fig.tight_layout()
        out = figs_dir / f"{name}_pagerank.png"
        fig.savefig(out, dpi=150)
        plt.close(fig)
        generated.append(out)
    return generated

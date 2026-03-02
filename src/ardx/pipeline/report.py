from __future__ import annotations

from pathlib import Path
import pandas as pd


def run_report(config: dict) -> Path:
    output_dir = Path(config.get("paths", {}).get("output_dir", "outputs"))
    report_path = output_dir / "report.md"
    lines = ["# Relatório de Análise de Redes\n"]

    for name in ["retweet", "mention"]:
        csv_path = output_dir / "metrics" / f"{name}_metrics.csv"
        lines.append(f"## Rede {name}\n")
        if not csv_path.exists():
            lines.append("Sem dados disponíveis.\n")
            continue

        df = pd.read_csv(csv_path)
        lines.append(f"Total de nós analisados: {len(df)}\n")
        if not df.empty:
            top = df.sort_values("pagerank", ascending=False).head(5)
            lines.append("Top 5 por PageRank:\n")
            for _, row in top.iterrows():
                lines.append(f"- {row['node']}: {row['pagerank']:.6f}\n")
        lines.append("\n")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("".join(lines), encoding="utf-8")
    return report_path

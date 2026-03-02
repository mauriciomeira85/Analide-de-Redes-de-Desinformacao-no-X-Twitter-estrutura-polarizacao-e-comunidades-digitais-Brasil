from __future__ import annotations

from pathlib import Path
import pandas as pd

from ardx.collectors import CSVCollector, TwikitCollector, XAPICollector
from ardx.utils.io import export_dataframe


def run_collect(config: dict) -> Path:
    source = config.get("data_source", "csv")
    output_dir = Path(config.get("paths", {}).get("output_dir", "outputs"))
    raw_base = output_dir / "raw" / "posts"

    if source == "csv":
        collector = CSVCollector(config["collect"]["csv"]["input_path"])
    elif source == "x_api":
        opts = config["collect"]["x_api"]
        collector = XAPICollector(query=opts["query"], max_results=opts.get("max_results", 100))
    elif source == "twikit":
        opts = config["collect"]["twikit"]
        collector = TwikitCollector(
            cookies_path=opts["cookies_path"],
            query=opts["query"],
            limit=opts.get("limit", 100),
        )
    else:
        raise ValueError(f"Fonte inválida: {source}")

    df: pd.DataFrame = collector.collect()
    export_dataframe(df, raw_base)
    return raw_base.with_suffix(".csv")

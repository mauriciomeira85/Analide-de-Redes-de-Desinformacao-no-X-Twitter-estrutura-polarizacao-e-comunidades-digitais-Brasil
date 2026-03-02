from __future__ import annotations

from pathlib import Path
import pandas as pd


class CSVCollector:
    def __init__(self, input_path: str):
        self.input_path = Path(input_path)

    def collect(self) -> pd.DataFrame:
        if not self.input_path.exists():
            raise FileNotFoundError(f"CSV de entrada não encontrado: {self.input_path}")
        df = pd.read_csv(self.input_path)
        return df

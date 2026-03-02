from __future__ import annotations

from pathlib import Path
import pandas as pd


class TwikitCollector:
    """Placeholder de coleta via sessão/cookies usando twikit."""

    def __init__(self, cookies_path: str, query: str, limit: int = 100):
        self.cookies_path = Path(cookies_path)
        self.query = query
        self.limit = limit

    def collect(self) -> pd.DataFrame:
        if not self.cookies_path.exists():
            raise FileNotFoundError(
                f"Arquivo de cookies/sessão não encontrado: {self.cookies_path}"
            )
        try:
            from twikit import Client
        except ImportError as exc:
            raise RuntimeError("twikit não instalado. Rode: pip install twikit") from exc

        try:
            # Placeholder: fluxo real depende do formato de sessão/cookies
            client = Client(language="pt-BR")
            _ = client
        except Exception as exc:
            raise RuntimeError(
                "Falha ao inicializar sessão twikit. Verifique cookies, formato e expiração."
            ) from exc

        # Em implementação real: autenticar com cookies e consultar timeline/search
        return pd.DataFrame(
            columns=[
                "tweet_id",
                "author_id",
                "retweeted_user_id",
                "mentioned_user_id",
                "created_at",
                "text",
            ]
        )

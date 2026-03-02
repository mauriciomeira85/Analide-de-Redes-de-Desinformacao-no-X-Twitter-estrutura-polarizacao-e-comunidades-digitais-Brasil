from __future__ import annotations

import os
from typing import Any
import pandas as pd


class XAPICollector:
    """Placeholder de coleta via X API v2 usando Tweepy.

    Necessita variáveis de ambiente:
      - X_BEARER_TOKEN
      - X_API_KEY
      - X_API_SECRET
      - X_ACCESS_TOKEN
      - X_ACCESS_SECRET
    """

    def __init__(self, query: str, max_results: int = 100):
        self.query = query
        self.max_results = max_results

    def _validate_env(self) -> None:
        needed = [
            "X_BEARER_TOKEN",
            "X_API_KEY",
            "X_API_SECRET",
            "X_ACCESS_TOKEN",
            "X_ACCESS_SECRET",
        ]
        missing = [k for k in needed if not os.getenv(k)]
        if missing:
            raise EnvironmentError(
                "Variáveis de ambiente ausentes para X API: " + ", ".join(missing)
            )

    def collect(self) -> pd.DataFrame:
        self._validate_env()
        try:
            import tweepy
        except ImportError as exc:
            raise RuntimeError("tweepy não instalado. Rode: pip install tweepy") from exc

        # Placeholder: estrutura básica de cliente v2
        client = tweepy.Client(bearer_token=os.environ["X_BEARER_TOKEN"])
        _ = client  # evita warning em scaffold

        # Em implementação real: usar client.search_recent_tweets(...) e normalizar campos
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

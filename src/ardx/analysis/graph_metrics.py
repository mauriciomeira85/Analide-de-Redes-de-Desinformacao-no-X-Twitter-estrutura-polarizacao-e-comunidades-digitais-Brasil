from __future__ import annotations

from typing import Any
import pandas as pd
import networkx as nx


def build_graphs(df: pd.DataFrame) -> dict[str, nx.DiGraph]:
    required = {"author_id", "retweeted_user_id", "mentioned_user_id"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Colunas ausentes para construir grafo: {sorted(missing)}")

    retweet_df = df.dropna(subset=["author_id", "retweeted_user_id"])
    mention_df = df.dropna(subset=["author_id", "mentioned_user_id"])

    g_retweet = nx.from_pandas_edgelist(
        retweet_df,
        source="author_id",
        target="retweeted_user_id",
        edge_attr=True,
        create_using=nx.DiGraph,
    )
    g_mention = nx.from_pandas_edgelist(
        mention_df,
        source="author_id",
        target="mentioned_user_id",
        edge_attr=True,
        create_using=nx.DiGraph,
    )
    return {"retweet": g_retweet, "mention": g_mention}


def detect_communities(g: nx.DiGraph) -> dict[Any, int]:
    undirected = g.to_undirected()
    if undirected.number_of_nodes() == 0:
        return {}
    try:
        import community as community_louvain  # python-louvain

        return community_louvain.best_partition(undirected)
    except Exception:
        communities = list(nx.algorithms.community.greedy_modularity_communities(undirected))
        partition: dict[Any, int] = {}
        for idx, comm in enumerate(communities):
            for node in comm:
                partition[node] = idx
        return partition


def compute_metrics(g: nx.DiGraph) -> pd.DataFrame:
    if g.number_of_nodes() == 0:
        return pd.DataFrame(
            columns=[
                "node",
                "in_degree",
                "out_degree",
                "pagerank",
                "betweenness",
                "community",
            ]
        )

    in_degree = dict(g.in_degree())
    out_degree = dict(g.out_degree())
    pagerank = nx.pagerank(g)
    betweenness = nx.betweenness_centrality(g)
    communities = detect_communities(g)

    rows = []
    for node in g.nodes():
        rows.append(
            {
                "node": node,
                "in_degree": in_degree.get(node, 0),
                "out_degree": out_degree.get(node, 0),
                "pagerank": pagerank.get(node, 0.0),
                "betweenness": betweenness.get(node, 0.0),
                "community": communities.get(node, -1),
            }
        )
    return pd.DataFrame(rows).sort_values("pagerank", ascending=False)

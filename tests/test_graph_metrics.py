import pandas as pd

from ardx.analysis.graph_metrics import build_graphs, compute_metrics, detect_communities


def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"author_id": "a", "retweeted_user_id": "b", "mentioned_user_id": "c"},
            {"author_id": "b", "retweeted_user_id": "c", "mentioned_user_id": "a"},
            {"author_id": "c", "retweeted_user_id": "a", "mentioned_user_id": "b"},
            {"author_id": "d", "retweeted_user_id": None, "mentioned_user_id": "a"},
        ]
    )


def test_build_graphs_creates_retweet_and_mention():
    graphs = build_graphs(sample_df())
    assert set(graphs.keys()) == {"retweet", "mention"}
    assert graphs["retweet"].number_of_nodes() >= 3
    assert graphs["mention"].number_of_nodes() >= 4


def test_compute_metrics_has_expected_columns():
    g = build_graphs(sample_df())["retweet"]
    metrics = compute_metrics(g)
    expected = {"node", "in_degree", "out_degree", "pagerank", "betweenness", "community"}
    assert expected.issubset(set(metrics.columns))
    assert len(metrics) == g.number_of_nodes()


def test_detect_communities_returns_partition():
    g = build_graphs(sample_df())["mention"]
    partition = detect_communities(g)
    assert isinstance(partition, dict)
    assert set(g.nodes()).issuperset(set(partition.keys()))


def test_build_graphs_missing_columns_raises():
    bad_df = pd.DataFrame([{"author_id": "x"}])
    try:
        build_graphs(bad_df)
    except ValueError as exc:
        assert "Colunas ausentes" in str(exc)
    else:
        raise AssertionError("Era esperado ValueError para colunas ausentes")

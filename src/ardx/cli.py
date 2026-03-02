from __future__ import annotations

import click

from ardx.pipeline.collect import run_collect
from ardx.pipeline.build_network import run_build_network
from ardx.pipeline.analyze import run_analyze
from ardx.pipeline.visualize import run_visualize
from ardx.pipeline.report import run_report
from ardx.utils.config import load_config


@click.group()
def main() -> None:
    """CLI do pipeline de análise de redes."""


@main.command("collect")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True))
def collect_cmd(config_path: str) -> None:
    cfg = load_config(config_path)
    out = run_collect(cfg)
    click.echo(f"Coleta concluída: {out}")


@main.command("build-network")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True))
def build_network_cmd(config_path: str) -> None:
    cfg = load_config(config_path)
    out = run_build_network(cfg)
    click.echo(f"Grafos exportados: {out}")


@main.command("analyze")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True))
def analyze_cmd(config_path: str) -> None:
    cfg = load_config(config_path)
    out = run_analyze(cfg)
    click.echo(f"Métricas exportadas: {out}")


@main.command("visualize")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True))
def visualize_cmd(config_path: str) -> None:
    cfg = load_config(config_path)
    out = run_visualize(cfg)
    click.echo(f"Figuras geradas: {out}")


@main.command("report")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True))
def report_cmd(config_path: str) -> None:
    cfg = load_config(config_path)
    out = run_report(cfg)
    click.echo(f"Relatório gerado: {out}")


@main.command("run-all")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True))
def run_all_cmd(config_path: str) -> None:
    cfg = load_config(config_path)
    run_collect(cfg)
    run_build_network(cfg)
    run_analyze(cfg)
    run_visualize(cfg)
    out = run_report(cfg)
    click.echo(f"Pipeline completo. Relatório: {out}")


if __name__ == "__main__":
    main()

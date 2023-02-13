import subprocess
import sys
import typer

from oddrn_generator import DbtGenerator
from odd_cli.logger import logger
from odd_dbt.action import ODDAction
from odd_dbt.parser import DbtArtifactParser

from odd_cli.client import Client
from rich.console import Console

app = typer.Typer(short_help="Run dbt tests and inject results to ODD platform")
err_console = Console(stderr=True)


@app.command()
def test(
        project_dir: str = './',
        target: str = typer.Option(None, "--target", "-t"),
        profile_name: str = typer.Option(None, '--profile'),
        platform_host: str = typer.Option(..., "--host", "-h", envvar="ODD_PLATFORM_HOST"),
        platform_token: str = typer.Option(..., "--token", "-t", envvar="ODD_PLATFORM_TOKEN"),
        dbt_host: str = typer.Option("localhost", "--dbt-host"),
):
    client = Client(host=platform_host)
    generator = DbtGenerator(host_settings=dbt_host)
    client.ingest_data_source(generator.get_data_source_oddrn(), platform_token)

    parser = DbtArtifactParser(
        target=target,
        project_dir=project_dir,
        profile_name=profile_name,
    )

    try:
        # Execute dbt in external process
        process = subprocess.Popen(
            ["dbt", "test"],
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        process.wait()
    except Exception as e:
        logger.error(e)

    data_entities = ODDAction(parser).run()
    client.ingest_data_entities(data_entities, platform_token)

    logger.success(f"Ingested {len(data_entities.items)} entities")


if __name__ == "__main__":
    app()

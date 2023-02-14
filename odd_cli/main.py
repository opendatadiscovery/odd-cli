from pathlib import Path

import typer
from oddrn_generator.generators import FilesystemGenerator

from odd_cli.client import Client
from odd_cli.logger import logger
from odd_cli.reader.reader import read
from odd_cli.tokens import app as tokens_app

app = typer.Typer()
app.add_typer(
    tokens_app,
    name="tokens",
)


@app.command()
def collect(
    folder: Path = typer.Argument(..., exists=True, resolve_path=True),
    platform_host: str = typer.Option(..., "--host", "-h", envvar="ODD_PLATFORM_HOST"),
    platform_token: str = typer.Option(
        ..., "--token", "-t", envvar="ODD_PLATFORM_TOKEN"
    ),
):
    "Collect and ingest metadata for local files from folder"
    client = Client(host=platform_host)

    generator = FilesystemGenerator(host_settings="local")

    client.ingest_data_source(generator.get_data_source_oddrn(), platform_token)

    data_entities = read(path=folder, generator=generator)

    client.ingest_data_entities(data_entities, platform_token)

    logger.success(f"Ingested {len(data_entities.items)} datasets")


@app.callback()
def callback():
    ...

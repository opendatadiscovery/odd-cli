from pathlib import Path

import typer
from oddrn_generator.generators import FilesystemGenerator

from odd_cli.client import Client
from odd_cli.reader.reader import read

app = typer.Typer()


@app.command()
def collect(
    folder: Path = typer.Argument(..., exists=True, resolve_path=True),
    platform_host: str = typer.Option(..., "--host", "-h", envvar="ODD_PLATFORM_HOST"),
    platform_token: str = typer.Option(
        ..., "--token", "-t", envvar="ODD_PLATFORM_TOKEN"
    ),
):
    client = Client(host=platform_host, token=platform_token)
    generator = FilesystemGenerator()

    client.ingest_data_source(generator.get_data_source_oddrn())

    data_entities = read(folder)
    client.ingest_data_entities(data_entities)


@app.callback()
def callback():
    ...

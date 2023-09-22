import traceback

import typer

from odd_cli.client import Client
from ..logger import logger
app = typer.Typer(short_help="Manipulate OpenDataDiscovery platform's tokens")


@app.command()
def create(
    name: str,
    description: str = "",
    platform_host: str = typer.Option(..., "--host", "-h", envvar="ODD_PLATFORM_HOST"),
):
    client = Client(platform_host)
    try:
        token = client.create_token(name=name, description=description)
        print(token)
        return token
    except Exception as e:
        logger.debug(traceback.format_exc())
        logger.error(e)
        raise typer.Exit(code=1)

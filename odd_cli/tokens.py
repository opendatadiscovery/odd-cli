from odd_cli.error import CreateTokenError
import typer
from requests import HTTPError

from odd_cli.client import Client


app = typer.Typer(short_help="Manipulate OpenDataDiscovery platform's tokens")


@app.command()
def create(
    name: str,
    description: str = "",
    platform_host: str = typer.Option(..., "--host", "-h", envvar="ODD_PLATFORM_HOST"),
):
    client = Client(platform_host)
    try:
        token = client.create_token(name, description)
        return token
    except HTTPError as e:
        message = e.response.json().get("message")
        raise CreateTokenError(name, message or "unknown")


if __name__ == "__main__":
    app()

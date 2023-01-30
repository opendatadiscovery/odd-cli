import typer
from requests import HTTPError
from rich.console import Console

from odd_cli.client import Client

app = typer.Typer(short_help="Manipulate OpenDataDiscovery platform's tokens")
err_console = Console(stderr=True)


@app.command()
def create(
    name: str,
    description: str = "",
    platform_host: str = typer.Option(..., "--host", "-h", envvar="ODD_PLATFORM_HOST"),
):
    client = Client(platform_host)
    try:
        token = client.create_token(name, description)
        print(f"Token: {token}")
        return token
    except HTTPError as e:
        message = e.response.json().get("message")
        err_console.print(message or "Could not create token.{e}", style="red")


if __name__ == "__main__":
    app()

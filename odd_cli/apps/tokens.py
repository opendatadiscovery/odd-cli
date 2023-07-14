import typer

from odd_cli.client import Client

app = typer.Typer(short_help="Manipulate OpenDataDiscovery platform's tokens")


@app.command()
def create(
    name: str,
    description: str = "",
    platform_host: str = typer.Option(..., "--host", "-h", envvar="ODD_PLATFORM_HOST"),
):
    client = Client(platform_host)
    token = client.create_token(name=name, description=description)

    print(token)
    return token

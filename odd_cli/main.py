
import typer
from odd_dbt.app import app as dbt_test_app

from odd_cli.__version__ import VERSION
from odd_cli.apps.metadata import app as collect_app
from odd_cli.apps.tokens import app as tokens_app

app = typer.Typer(pretty_exceptions_show_locals=False)

app.add_typer(
    collect_app,
)
app.add_typer(
    tokens_app,
    name="tokens",
)
app.add_typer(dbt_test_app, name="dbt")

@app.command()
def version(
    short: bool = typer.Option(False, "--short", "-s", help="Print only version number")
):
    "Print version"
    if short:
        print(VERSION)
    else:
        print(f"odd-cli version: {VERSION}")

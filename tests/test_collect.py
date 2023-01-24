import os
import unittest
from pathlib import Path

import mock
from typer.testing import CliRunner

from odd_cli.main import app

runner = CliRunner()


@mock.patch("odd_cli.main.Client")
class CollectCommandTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.folder_path = str(Path(__file__).parent / "data")

    def test_wrong_folder_path(self, client):
        result = runner.invoke(app, ["collect", "fake_dir"])
        assert result.exit_code == 2

    def test_success_creation(self, client):
        result = runner.invoke(
            app, ["collect", self.folder_path, "-h", "localhost", "-t", "token"]
        )
        assert result.exit_code == 0

    def test_omit_host(self, client):
        result = runner.invoke(
            app,
            [
                "collect",
                "data",
                "--token",
                "token",
            ],
        )
        assert result.exit_code == 2
        os.environ.setdefault("ODD_PLATFORM_HOST", "localhost")
        result = runner.invoke(
            app,
            ["collect", self.folder_path, "-t", "token"],
        )
        assert result.exit_code == 0

    def test_omit_token(self, client):
        result = runner.invoke(
            app,
            ["collect", "data", "-h", "localhost"],
        )
        assert result.exit_code == 2

        os.environ.setdefault("ODD_PLATFORM_TOKEN", "TOKEN")
        result = runner.invoke(
            app,
            ["collect", self.folder_path, "-h", "localhost"],
        )
        assert result.exit_code == 0

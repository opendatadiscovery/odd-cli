from pathlib import Path

from odd_models.models import DataEntity, DataEntityList, DataEntityType
from oddrn_generator import FilesystemGenerator
from oddrn_generator.utils import escape

from odd_cli.reader.reader import read


def test_reader():
    path = Path(__file__).parent / "data"
    generator = FilesystemGenerator(host_settings="local")
    del_ = read(path=path, generator=generator)
    file_target_path = str(path / "some_data.csv")

    assert isinstance(del_, DataEntityList)
    assert len(del_.items) == 1

    dataset = del_.items[0]
    assert isinstance(dataset, DataEntity)
    assert dataset.type == DataEntityType.TABLE
    assert dataset.oddrn == f"//filesystem/host/local/path/{escape(file_target_path)}"

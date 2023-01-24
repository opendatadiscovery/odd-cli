from pathlib import Path
from typing import Callable

from odd_models.models import DataEntityList
from oddrn_generator import FilesystemGenerator

from odd_cli.reader.csv import read_csv
from odd_cli.reader.mapper.table import map_table
from odd_cli.reader.models.table import Table

Reader = Callable[[Path], Table]


def read(path: Path, pattern: str = "*.csv") -> DataEntityList:
    """Read local files

    Args:
        path (str): location of files to fetch
        pattern (str): file match mask
    """
    generator = FilesystemGenerator()
    data_source_oddrn = generator.get_data_source_oddrn()

    tables = (read_file(path) for path in path.rglob(pattern))
    data_entities = [map_table(table, generator) for table in tables]

    return DataEntityList(data_source_oddrn=data_source_oddrn, items=data_entities)


def read_file(path: Path) -> Table:
    if is_csv_file(path):
        return read_csv(path)


def is_csv_file(path: Path):
    return str(path).endswith(".csv")

from pathlib import Path

from odd_models.models import DataEntityList
from oddrn_generator import FilesystemGenerator
from tqdm import tqdm

from odd_cli.reader.csv import read_csv
from odd_cli.reader.mapper.table import map_table
from odd_cli.reader.models.table import Table


def read(
    path: Path, generator: FilesystemGenerator, pattern: str = "*.csv"
) -> DataEntityList:
    """Read local files

    Args:
        path (str): location of files to fetch
        generator (FilesystemGenerator): creating oddrn by context
        pattern (str): file match mask
    """
    if not path.resolve().exists():
        raise ValueError(f"Path {path.resolve()} doesn't exist")

    data_source_oddrn = generator.get_data_source_oddrn()
    tables = (
        read_file(path) for path in tqdm(path.rglob(pattern), desc="Reading files")
    )
    data_entities = [map_table(table, generator) for table in tables]

    return DataEntityList(data_source_oddrn=data_source_oddrn, items=data_entities)


def read_file(path: Path) -> Table:
    if is_csv_file(path):
        return read_csv(path)


def is_csv_file(path: Path):
    return str(path).endswith(".csv")

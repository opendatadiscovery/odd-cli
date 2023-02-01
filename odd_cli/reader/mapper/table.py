from loguru import logger
from odd_models.models import DataEntity, DataEntityType, DataSet
from oddrn_generator.generators import FilesystemGenerator

from odd_cli.reader.mapper.field import map_field
from odd_cli.reader.models.table import Table


def map_table(table: Table, generator: FilesystemGenerator) -> DataEntity:
    generator.set_oddrn_paths(path=table.path)
    fields = [map_field(field, generator) for field in table.fields]

    logger.debug(f"Generated path: {generator.get_oddrn_by_path('path')}")

    return DataEntity(
        oddrn=generator.get_oddrn_by_path("path"),
        name=table.name,
        type=DataEntityType.TABLE,
        dataset=DataSet(field_list=fields, rows_number=table.rows_number),
    )

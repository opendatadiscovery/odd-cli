import csv
from pathlib import Path
from typing import List

import pyarrow as pa
from odd_cli.logger import logger
from pyarrow import csv
from pyarrow.types import (
    is_boolean,
    is_date,
    is_decimal,
    is_floating,
    is_integer,
    is_string,
)

from odd_cli.reader.models.field import Field, FieldType
from odd_cli.reader.models.table import Table


class PyarrowTable(Table):
    TYPE_MAPPINGS = {
        is_floating: FieldType.TYPE_INTEGER,
        is_decimal: FieldType.TYPE_INTEGER,
        is_integer: FieldType.TYPE_INTEGER,
        is_string: FieldType.TYPE_STRING,
        is_boolean: FieldType.TYPE_BOOLEAN,
        is_date: FieldType.TYPE_DATETIME,
    }

    def __init__(self, name: str, path: Path) -> None:
        table: pa.Table = csv.read_csv(path)

        self.name = name
        self.path = str(Path.resolve(path))

        logger.debug(f"Path {path}")
        logger.debug(f"Resolved path: {self.path}")

        self.metadata = {}
        self.rows_number = table.num_rows
        self.fields = self._get_fields(table)

    def _get_fields(self, table) -> List[Field]:
        schema = table.schema
        return [
            Field(
                name=field.name,
                type=self._map_type(field.type),
                nullable=field.nullable,
            )
            for field in schema
        ]

    def _map_type(self, field_type: pa.DataType) -> FieldType:
        return next(
            (self.TYPE_MAPPINGS[fn] for fn in self.TYPE_MAPPINGS if fn(field_type)),
            FieldType.TYPE_UNKNOWN,
        )


def read_csv(file_path: Path) -> Table:
    name = file_path.stem

    return PyarrowTable(name, file_path)

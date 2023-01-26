from odd_models.models import DataSetField, DataSetFieldType, Type
from oddrn_generator.generators import FilesystemGenerator

from odd_cli.reader.models.field import Field, FieldType


def map_type(field_type: FieldType) -> Type:
    mappings = {
        FieldType.TYPE_STRING: Type.TYPE_STRING,
        FieldType.TYPE_NUMBER: Type.TYPE_NUMBER,
        FieldType.TYPE_INTEGER: Type.TYPE_INTEGER,
        FieldType.TYPE_BOOLEAN: Type.TYPE_BOOLEAN,
        FieldType.TYPE_DATETIME: Type.TYPE_DATETIME,
        FieldType.TYPE_TIME: Type.TYPE_TIME,
        FieldType.TYPE_LIST: Type.TYPE_LIST,
        FieldType.TYPE_UNKNOWN: Type.TYPE_UNKNOWN,
    }

    return mappings.get(field_type, Type.TYPE_UNKNOWN)


def map_field(field: Field, generator: FilesystemGenerator) -> DataSetField:
    name = field.name
    generator.set_oddrn_paths(fields=name)

    return DataSetField(
        oddrn=generator.get_oddrn_by_path("fields"),
        name=field.name,
        type=DataSetFieldType(type=map_type(field.type), is_nullable=field.nullable),
    )

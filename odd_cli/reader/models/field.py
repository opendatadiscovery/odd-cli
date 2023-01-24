import dataclasses
from enum import Enum


class FieldType(Enum):
    TYPE_STRING = "TYPE_STRING"
    TYPE_NUMBER = "TYPE_NUMBER"
    TYPE_INTEGER = "TYPE_INTEGER"
    TYPE_BOOLEAN = "TYPE_BOOLEAN"
    TYPE_CHAR = "TYPE_CHAR"
    TYPE_DATETIME = "TYPE_DATETIME"
    TYPE_TIME = "TYPE_TIME"
    TYPE_STRUCT = "TYPE_STRUCT"
    TYPE_BINARY = "TYPE_BINARY"
    TYPE_LIST = "TYPE_LIST"
    TYPE_MAP = "TYPE_MAP"
    TYPE_UNION = "TYPE_UNION"
    TYPE_DURATION = "TYPE_DURATION"
    TYPE_UNKNOWN = "TYPE_UNKNOWN"


@dataclasses.dataclass
class Field:
    name: str
    type: FieldType
    nullable: bool

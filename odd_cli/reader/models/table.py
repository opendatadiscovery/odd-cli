from typing import Any, Dict, List, Optional, Protocol

from .field import Field


class Table(Protocol):
    name: str
    path: str
    fields: List[Field]
    rows_number: Optional[int]
    metadata: Dict[str, Any]

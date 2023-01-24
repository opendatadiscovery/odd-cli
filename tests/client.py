from odd_models.models import DataEntityList

from odd_cli.client import Client


class TestClient(Client):
    def ingest_data_entities(self, data_entities: DataEntityList) -> None:
        return None

    def ingest_data_source(self, data_source_oddrn: str) -> None:
        return None

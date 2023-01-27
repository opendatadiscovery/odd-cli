from typing import Optional

from odd_models.api_client.open_data_discovery_ingestion_api import ODDApiClient
from odd_models.models import DataEntityList, DataSource, DataSourceList


class Client:
    def __init__(self, host: str) -> None:
        self._client = ODDApiClient(host)

    def create_token(self, name: str, description: Optional[str]) -> str:
        path = "/api/collectors"
        data = {"name": name, "description": description}
        response = self._client.post(path, data=data)

        response.raise_for_status()
        return response.json().get("token").get("value")

    def ingest_data_source(self, data_source_oddrn: str, token: str) -> None:
        headers = {"Authorization": f"Bearer {token}"}
        response = self._client.create_data_source(
            DataSourceList(
                items=[DataSource(oddrn=data_source_oddrn, name="local_files")]
            ),
            headers=headers,
        )
        response.raise_for_status()

    def ingest_data_entities(self, data_entities: DataEntityList, token: str) -> None:
        headers = {"Authorization": f"Bearer {token}"}
        response = self._client.post_data_entity_list(data_entities, headers=headers)
        response.raise_for_status()

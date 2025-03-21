from unittest.mock import patch, MagicMock
import pytest

from helpers.bigquery_helper import BigQueryHelper
from google.cloud import bigquery
from google.cloud.exceptions import NotFound  # type: ignore


@pytest.mark.parametrize(
    "schema",
    [
        [{"name": "id", "type": "INTEGER"}, {"name": "name", "type": "STRING"}],
        [{"name": "created_at", "type": "TIMESTAMP"}],
        [],
    ],
)
@patch("helpers.bigquery_helper.bigquery.Client")
def test_create_table_if_not_exists_table_doesnt_exist(MockBigQueryClient, schema):
    """Tests creating a table when it doesn't already exist."""
    mock_client_instance = MockBigQueryClient.return_value
    mock_client_instance.get_table.side_effect = NotFound("Table not found")
    mock_client_instance.create_table = MagicMock()

    helper = BigQueryHelper("project_id", "dataset_id", "table_id")
    helper.create_table_if_not_exists(schema)

    mock_client_instance.create_table.assert_called_once()


@patch("helpers.bigquery_helper.bigquery.Client")
def test_create_table_if_not_exists_table_exists(MockBigQueryClient):
    """Tests creating a table when it already exists."""
    mock_client_instance = MockBigQueryClient.return_value
    mock_client_instance.get_table.return_value = "table_exists"
    mock_client_instance.create_table = MagicMock()

    helper = BigQueryHelper("project_id", "dataset_id", "table_id")
    helper.create_table_if_not_exists([])

    mock_client_instance.create_table.assert_not_called()

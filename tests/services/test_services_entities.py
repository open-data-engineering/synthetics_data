import pytest
from unittest.mock import patch
import logging

from src.services.entities import EntityService

logger = logging.getLogger(__name__)


class TestEntityService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_entities", "zero_entities", "many_entities"],
    )
    @patch("src.services.entities.EntityEvents")
    def test_insert_entities(self, MockEntityEvents, count):
        MockEntityEvents.generate_entities.return_value = [
            {"entity_id": i} for i in range(count)
        ]

        entities = EntityService.insert_entities(count)

        assert len(entities) == count
        MockEntityEvents.generate_entities.assert_called_once_with(count)

    @patch("src.services.entities.EntityEvents.generate_entities")
    def test_insert_entities_exception(self, mock_generate_entities, caplog):
        mock_generate_entities.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            entities = EntityService.insert_entities(5)

        assert entities == []
        assert "Erro ao inserir entidades" in caplog.text

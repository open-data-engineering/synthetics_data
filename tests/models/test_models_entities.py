import pytest
from pydantic import ValidationError
from datetime import datetime, timezone

from models.entities import Entity


class TestEntity:
    @pytest.mark.parametrize(
        "entity_id, name, created_at",
        [
            ("entity123", "Product A", datetime.now(timezone.utc)),
            ("entity456", "Service B", datetime(2024, 1, 1, tzinfo=timezone.utc)),
            (
                "entity789",
                "Customer C",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_entity", "specific_date", "end_of_year_date"],
    )
    def test_valid_entity(self, entity_id, name, created_at):
        entity = Entity(entity_id=entity_id, name=name, created_at=created_at)
        assert entity.entity_id == entity_id
        assert entity.name == name
        assert entity.created_at == created_at

    @pytest.mark.parametrize(
        "entity_id, name, created_at, expected_error",
        [
            (
                123,
                "Product A",
                datetime.now(timezone.utc),
                r"entity_id\s+Input should be a valid string",
            ),
            (
                "entity456",
                123,
                datetime.now(timezone.utc),
                r"name\s+Input should be a valid string",
            ),
            (
                "entity123",
                "Product A",
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=["invalid_entity_id", "invalid_name", "invalid_created_at"],
    )
    def test_invalid_entity(self, entity_id, name, created_at, expected_error):
        with pytest.raises(ValidationError, match=expected_error):
            Entity(entity_id=entity_id, name=name, created_at=created_at)

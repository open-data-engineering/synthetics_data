import pytest
from uuid import UUID
from commons.entities import EntityEvents
from faker import Faker

fake = Faker("pt_BR")


@pytest.mark.parametrize(
    "count",
    [
        (1),
        (10),
        (0),
    ],
)
def test_generate_entities(count):
    """Tests the generate_entities method with various counts."""

    entities = EntityEvents.generate_entities(count)

    assert len(entities) == count
    for entity in entities:
        assert isinstance(UUID(entity["entity_id"]), UUID)
        assert isinstance(entity["name"], str)
        assert isinstance(entity["created_at"], object)

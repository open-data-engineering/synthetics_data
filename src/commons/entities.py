from uuid import uuid4
from faker import Faker
from typing import Any, Dict, List

fake = Faker("pt_BR")


class EntityEvents:
    """Generates synthetic data for entities.

    This class provides methods for generating lists of entity dictionaries.
    """

    @staticmethod
    def generate_entities(count: int) -> List[Dict[str, Any]]:
        """Generates a list of entity dictionaries.

        Each dictionary represents an entity with details like ID, name, and creation timestamp.
        """
        return [
            {
                "entity_id": str(uuid4()),
                "name": fake.company(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

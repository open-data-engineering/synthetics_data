import numpy as np  # type: ignore
from uuid import uuid4
from faker import Faker  # type: ignore
from typing import List

fake = Faker("pt_BR")


class EntityEvents:
    """Generates synthetic data for entities.

    This class provides methods for generating lists of entity dictionaries.
    """

    @staticmethod
    def generate_entities(count: int) -> List[dict]:
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

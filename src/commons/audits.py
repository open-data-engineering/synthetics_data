import numpy as np
from uuid import uuid4
from faker import Faker
from typing import Any, Dict, List

fake = Faker("pt_BR")


class AuditsEvents:
    """Generates synthetic audit data.

    This class provides methods for generating lists of audit dictionaries.
    """

    @staticmethod
    def generate_audits(count: int) -> List[Dict[str, Any]]:
        """Generates a list of audit dictionaries.

        Each dictionary represents an audit with details like ID, entity ID, status, findings, and timestamps.
        """
        return [
            {
                "audit_id": str(uuid4()),
                "entity_id": str(uuid4()),
                "status": np.random.choice(["success", "failure"]),
                "findings": np.random.choice(["no findings", "findings"]),
                "date": fake.date_time_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

import random
from uuid import uuid4
from faker import Faker
from typing import Any, Dict, List

fake = Faker("pt_BR")


class CompliancesEvents:
    """Generates synthetic data for compliance-related events.

    This class provides methods for generating lists of dictionaries representing regulations and user verifications.
    """

    @staticmethod
    def generate_regulations(count: int) -> List[Dict[str, Any]]:
        """Generates a list of regulation dictionaries.

        Each dictionary represents a regulation with details like ID, name, description, jurisdiction, and timestamps.
        """
        return [
            {
                "regulation_id": str(uuid4()),
                "name": fake.sentence(),
                "description": fake.paragraph(),
                "jurisdiction": fake.country(),
                "date": fake.date_time_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_user_verifications(count: int) -> List[Dict[str, Any]]:
        """Generates a list of user verification dictionaries.

        Each dictionary represents a user verification with details like ID, user ID, type, status, and timestamps.
        """
        return [
            {
                "verification_id": str(uuid4()),
                "user_id": str(uuid4()),
                "type": random.choice(["email", "phone", "identity"]),
                "status": random.choice(["approved", "pending", "rejected"]),
                "date": fake.date_time_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

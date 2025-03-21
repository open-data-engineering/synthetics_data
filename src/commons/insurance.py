import numpy as np
from uuid import uuid4
from faker import Faker
from typing import Any, Dict, List

fake = Faker("pt_BR")


class InsuranceEvents:
    """Generates synthetic data for insurance policies, claims, and insured entities.

    This class provides methods for generating synthetic data related to insurance,
    including policies, claims, and insured entities.  The data is generated
    using the Faker library and includes realistic attributes.
    """

    @staticmethod
    def generate_policies(count: int) -> List[Dict[str, Any]]:
        """Gera apólices de seguro como dicionários."""
        return [
            {
                "policy_id": str(uuid4()),
                "type": np.random.choice(["auto", "health", "home"]),
                "coverage_amount": np.random.randint(5000, 50000),
                "premium": np.random.randint(100, 1000),
                "start_date": fake.date_this_year(),
                "end_date": fake.date_this_year(),
                "user_id": str(uuid4()),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_claims(count: int) -> List[Dict[str, Any]]:
        """Generates insurance claims as dictionaries.

        This method generates a list of dictionaries, where each dictionary
        represents an insurance claim with attributes like claim ID, policy ID,
        amount claimed, status, filed date, and creation timestamp. The data is
        generated using the Faker library and includes realistic attributes.
        """
        return [
            {
                "claim_id": str(uuid4()),
                "policy_id": str(uuid4()),
                "amount_claimed": np.random.randint(1000, 20000),
                "status": np.random.choice(["approved", "pending", "denied"]),
                "filed_date": fake.date_time_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_insured_entities(count: int) -> List[Dict[str, Any]]:
        """Generates insured entities as dictionaries.

        This method generates a list of dictionaries, where each dictionary
        represents an insured entity with attributes like entity ID, type,
        description, value, and creation timestamp. The data is generated
        using the Faker library and includes realistic attributes.
        """
        return [
            {
                "entity_id": str(uuid4()),
                "type": np.random.choice(["vehicle", "property", "life"]),
                "description": fake.sentence(),
                "value": np.random.randint(10000, 100000),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

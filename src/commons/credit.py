import numpy as np  # type: ignore
from uuid import uuid4
from faker import Faker  # type: ignore
from typing import List

fake = Faker("pt_BR")


class CreditsEvents:
    """Generates synthetic data for credit-related events.

    This class provides methods for generating lists of dictionaries representing credit scores and risk assessments.
    """

    @staticmethod
    def generate_credit_scores(count: int) -> List[dict]:
        """Generates a list of credit score dictionaries.

        Each dictionary represents a credit score with details like ID, user ID, score, and timestamps.
        """
        return [
            {
                "score_id": str(uuid4()),
                "user_id": str(uuid4()),
                "score": np.random.randint(300, 850),
                "last_updated": fake.date_time_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_risk_assessments(count: int) -> List[dict]:
        """Generates a list of risk assessment dictionaries.

        Each dictionary represents a risk assessment with details like ID, user ID, risk level, details, and timestamps.
        """
        return [
            {
                "assessment_id": str(uuid4()),
                "user_id": str(uuid4()),
                "risk_level": np.random.choice(["low", "medium", "high"]),
                "details": fake.sentence(),
                "date": fake.date_time_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

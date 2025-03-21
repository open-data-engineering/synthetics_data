import numpy as np
from uuid import uuid4
from faker import Faker
from typing import Any, Dict, List


fake = Faker("pt_BR")


class LendingEvents:
    """Generates synthetic data for lending events.

    This class provides methods for generating synthetic data related to lending,
    including loans, payments, credit scores, and risk assessments. The data is
    generated using the Faker library and includes realistic attributes.
    """

    @staticmethod
    def generate_loans(count: int) -> List[Dict[str, Any]]:
        """Generates loan data as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        a loan with attributes like loan ID, user ID, amount, interest rate, term, and
        creation timestamp. The data is generated using the Faker library and includes
        realistic attributes.
        """
        return [
            {
                "loan_id": str(uuid4()),
                "user_id": str(uuid4()),
                "amount": np.random.randint(1000, 50000),
                "interest_rate": np.random.uniform(2.5, 15.0),
                "term": np.random.randint(12, 60),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_payments(count: int) -> List[Dict[str, Any]]:
        """Generates loan payment data as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        a loan payment with attributes like payment ID, loan ID, amount, payment date,
        status, and creation timestamp. The data is generated using the Faker library
        and includes realistic attributes.
        """
        return [
            {
                "payment_id": str(uuid4()),
                "loan_id": str(uuid4()),
                "amount": np.random.randint(100, 2000),
                "date": fake.date_time_this_year(),
                "status": np.random.choice(["completed", "pending", "failed"]),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_credit_score(count: int) -> List[Dict[str, Any]]:
        """Generates credit score data as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        a credit score with attributes like score ID, user ID, score, last updated date,
        and creation timestamp. The data is generated using the Faker library and
        includes realistic attributes.
        """
        return [
            {
                "score_id": str(uuid4()),
                "user_id": str(uuid4()),
                "score": np.random.randint(1, 1000),
                "last_updated": fake.date_time_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_risk_assessment(count: int) -> List[Dict[str, Any]]:
        """Generates risk assessment data as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        a risk assessment with attributes like assessment ID, user ID, risk level,
        details, assessment date, and creation timestamp. The data is generated using
        the Faker library and includes realistic attributes.
        """
        return [
            {
                "assessment_id": str(uuid4()),
                "user_id": str(uuid4()),
                "risk_level": np.random.choice(["low", "medium", "high"]),
                "details": fake.sentence(),
                "date": fake.date_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

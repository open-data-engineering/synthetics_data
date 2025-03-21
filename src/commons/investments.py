import numpy as np
from uuid import uuid4
from faker import Faker
from typing import Any, Dict, List


fake = Faker("pt_BR")


class InvestmentsEvents:
    """Generates synthetic data for investment portfolios.

    This class provides methods for generating synthetic data related to investment portfolios,
    including transactions and portfolio details. The data is generated using the Faker library
    and includes realistic attributes.
    """

    @staticmethod
    def generate_portfolios(count: int) -> List[Dict[str, Any]]:
        """Generates investment portfolios as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        an investment portfolio with attributes like portfolio ID, user ID, total value,
        risk profile, and creation timestamp. The data is generated using the Faker library
        and includes realistic attributes.
        """
        return [
            {
                "portfolio_id": str(uuid4()),
                "user_id": str(uuid4()),
                "total_value": np.random.randint(1000, 100000),
                "risk_profile": np.random.choice(
                    ["conservative", "moderate", "aggressive"]
                ),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_transaction(count: int) -> List[Dict[str, Any]]:
        """Generates investment transactions as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        an investment transaction with attributes like transaction ID, portfolio ID,
        asset ID, amount, price, timestamp, and creation timestamp. The data is generated
        using the Faker library and includes realistic attributes.
        """
        return [
            {
                "transaction_id": str(uuid4()),
                "portfolio_id": str(uuid4()),
                "asset_id": str(uuid4()),
                "amount": np.random.randint(1, 1000),
                "price": np.random.randint(1, 1000),
                "timestamp": fake.date_time_this_year(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_portfolio(count: int) -> List[Dict[str, Any]]:
        """Generates investment portfolios as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        an investment portfolio with attributes like portfolio ID, user ID, total value,
        risk profile, and creation timestamp.  The data is generated using the Faker library
        and includes realistic attributes.
        """
        return [
            {
                "portfolio_id": str(uuid4()),
                "user_id": str(uuid4()),
                "total_value": np.random.randint(1, 1000),
                "risk_profile": np.random.choice(["low", "medium", "high"]),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

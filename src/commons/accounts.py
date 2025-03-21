import random
from uuid import uuid4
from faker import Faker
from typing import Any, Dict, List

fake = Faker("pt_BR")


class AccountEvents:

    @staticmethod
    def generate_accounts(count: int) -> List[Dict[str, Any]]:
        """Generates a list of account dictionaries.

        Each dictionary represents an account with details like ID, user ID, balance, currency, creation date, type, and status.
        """
        return [
            {
                "account_id": str(uuid4()),
                "user_id": str(uuid4()),
                "balance": int(random.uniform(100, 10000)),
                "currency": random.choice(["USD", "BRL", "EUR"]),
                "created_at": fake.date_time_this_year().isoformat(),
                "account_type": random.choice(["personal", "business"]),
                "status": random.choice(["active", "inactive"]),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_subaccounts(count: int) -> List[Dict[str, Any]]:
        """Generates a list of subaccount dictionaries.

        Each dictionary represents a subaccount with details like ID, parent account ID, balance, creation date, and purpose.
        """
        return [
            {
                "subaccount_id": str(uuid4()),
                "parent_account_id": str(uuid4()),
                "balance": int(random.uniform(50, 5000)),
                "created_at": fake.date_time_this_year().isoformat(),
                "purpose": fake.word(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_users(count: int) -> List[Dict[str, Any]]:
        """Generates a list of user dictionaries.

        Each dictionary represents a user with details like ID, name, email, phone, and creation date.
        """
        return [
            {
                "user_id": str(uuid4()),
                "name": fake.name(),
                "email": fake.email(),
                "phone": fake.phone_number(),
                "created_at": fake.date_time_this_year().isoformat(),
            }
            for _ in range(count)
        ]

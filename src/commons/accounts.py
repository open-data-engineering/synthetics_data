import random
from uuid import uuid4
from faker import Faker  # type: ignore
from typing import List

fake = Faker("pt_BR")


class AccountEvents:

    @staticmethod
    def generate_accounts(count: int) -> List[dict]:
        """Gera contas como dicionários."""
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
    def generate_subaccounts(count: int) -> List[dict]:
        """Gera subcontas como dicionários."""
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
    def generate_users(count: int) -> List[dict]:
        """Gera usuários como dicionários.

        Cria uma lista de dicionários, onde cada dicionário representa
        um usuário com detalhes como ID, nome, e-mail, telefone e data de criação.
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

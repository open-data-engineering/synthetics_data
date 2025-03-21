import numpy as np  # type: ignore
from uuid import uuid4
from faker import Faker  # type: ignore
from typing import List

fake = Faker("pt_BR")


class PaymentsEvents:
    """Generates synthetic data for financial transactions.

    This class provides methods for generating synthetic data related to payments,
    including transactions, payment methods, and merchants. The data is generated
    using the Faker library and includes realistic attributes.
    """

    @staticmethod
    def generate_transactions(count: int) -> List[dict]:
        """Generates payment transactions as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        a payment transaction with attributes like transaction ID, amount, currency,
        status, timestamp, sender ID, receiver ID, and creation timestamp. The data
        is generated using the Faker library and includes realistic attributes.
        """
        return [
            {
                "transaction_id": str(uuid4()),
                "amount": np.random.randint(10, 5000),
                "currency": np.random.choice(["BRL", "USD", "EUR"]),
                "status": np.random.choice(["completed", "pending", "failed"]),
                "timestamp": fake.date_time_this_year(),
                "sender_id": str(uuid4()),
                "receiver_id": str(uuid4()),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_payment_methods(count: int) -> List[dict]:
        """Generates payment method data as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        a payment method with attributes like method ID, type, details, user ID,
        and creation timestamp. The data is generated using the Faker library and
        includes realistic attributes.
        """
        return [
            {
                "method_id": str(uuid4()),
                "type": np.random.choice(
                    ["credit_card", "debit_card", "pix", "paypal"]
                ),
                "details": fake.credit_card_number(),
                "user_id": str(uuid4()),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

    @staticmethod
    def generate_merchants(count: int) -> List[dict]:
        """Generates merchant data as dictionaries.

        This method generates a list of dictionaries, where each dictionary represents
        a merchant with attributes like merchant ID, name, category, contact information,
        and creation timestamp. The data is generated using the Faker library and
        includes realistic attributes.
        """
        return [
            {
                "merchant_id": str(uuid4()),
                "name": fake.company(),
                "category": np.random.choice(["retail", "services", "ecommerce"]),
                "contact_info": fake.email(),
                "created_at": fake.date_time_this_year(),
            }
            for _ in range(count)
        ]

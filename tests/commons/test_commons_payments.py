from datetime import date, datetime
import pytest
from faker import Faker

from commons.payments import PaymentsEvents

fake = Faker("pt_BR")


class TestPaymentsEvents:
    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (5, 5),
            (0, 0),
            (1, 1),
            (100, 100),
        ],
        ids=[
            "generate_five_transactions",
            "generate_zero_transactions",
            "generate_one_transaction",
            "generate_many_transactions",
        ],
    )
    def test_generate_transactions(self, count: int, expected_length: int):

        transactions = PaymentsEvents.generate_transactions(count)

        assert len(transactions) == expected_length
        if transactions:
            for transaction in transactions:
                assert isinstance(transaction["transaction_id"], str)
                assert 10 <= transaction["amount"] < 5000
                assert transaction["currency"] in ["BRL", "USD", "EUR"]
                assert transaction["status"] in ["completed", "pending", "failed"]
                assert isinstance(transaction["timestamp"], (str, date, datetime))
                assert isinstance(transaction["sender_id"], str)
                assert isinstance(transaction["receiver_id"], str)
                assert isinstance(transaction["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (5, 5),
            (0, 0),
            (1, 1),
            (50, 50),
        ],
        ids=[
            "generate_five_payment_methods",
            "generate_zero_payment_methods",
            "generate_one_payment_method",
            "generate_many_payment_methods",
        ],
    )
    def test_generate_payment_methods(self, count: int, expected_length: int):

        payment_methods = PaymentsEvents.generate_payment_methods(count)

        assert len(payment_methods) == expected_length
        if payment_methods:
            for payment_method in payment_methods:
                assert isinstance(payment_method["method_id"], str)
                assert payment_method["type"] in [
                    "credit_card",
                    "debit_card",
                    "pix",
                    "paypal",
                ]
                assert isinstance(payment_method["details"], str)
                assert isinstance(payment_method["user_id"], str)
                assert isinstance(payment_method["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (3, 3),
            (0, 0),
            (1, 1),
            (75, 75),
        ],
        ids=[
            "generate_three_merchants",
            "generate_zero_merchants",
            "generate_one_merchant",
            "generate_many_merchants",
        ],
    )
    def test_generate_merchants(self, count: int, expected_length: int):

        merchants = PaymentsEvents.generate_merchants(count)

        assert len(merchants) == expected_length
        if merchants:
            for merchant in merchants:
                assert isinstance(merchant["merchant_id"], str)
                assert isinstance(merchant["name"], str)
                assert merchant["category"] in ["retail", "services", "ecommerce"]
                assert isinstance(merchant["contact_info"], str)
                assert isinstance(merchant["created_at"], (str, date, datetime))

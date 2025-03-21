from datetime import date, datetime
import pytest
from faker import Faker

from commons.investments import InvestmentsEvents

fake = Faker("pt_BR")


class TestInvestmentsEvents:
    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (5, 5),
            (0, 0),
            (1, 1),
            (100, 100),
        ],
        ids=[
            "generate_five_portfolios",
            "generate_zero_portfolios",
            "generate_one_portfolio",
            "generate_many_portfolios",
        ],
    )
    def test_generate_portfolios(self, count: int, expected_length: int):

        portfolios = InvestmentsEvents.generate_portfolios(count)

        assert len(portfolios) == expected_length
        if portfolios:
            for portfolio in portfolios:
                assert isinstance(portfolio["portfolio_id"], str)
                assert isinstance(portfolio["user_id"], str)
                assert 1000 <= portfolio["total_value"] < 100000
                assert portfolio["risk_profile"] in [
                    "conservative",
                    "moderate",
                    "aggressive",
                ]
                assert isinstance(portfolio["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (5, 5),
            (0, 0),
            (1, 1),
            (50, 50),
        ],
        ids=[
            "generate_five_transactions",
            "generate_zero_transactions",
            "generate_one_transaction",
            "generate_many_transactions",
        ],
    )
    def test_generate_transaction(self, count: int, expected_length: int):

        transactions = InvestmentsEvents.generate_transaction(count)

        assert len(transactions) == expected_length
        if transactions:
            for transaction in transactions:
                assert isinstance(transaction["transaction_id"], str)
                assert isinstance(transaction["portfolio_id"], str)
                assert isinstance(transaction["asset_id"], str)
                assert 1 <= transaction["amount"] < 1000
                assert 1 <= transaction["price"] < 1000
                assert isinstance(transaction["timestamp"], (str, date, datetime))
                assert isinstance(transaction["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (3, 3),
            (0, 0),
            (1, 1),
            (75, 75),
        ],
        ids=[
            "generate_three_portfolios",
            "generate_zero_portfolios",
            "generate_one_portfolio",
            "generate_many_portfolios",
        ],
    )
    def test_generate_portfolio(self, count, expected_length):

        portfolios = InvestmentsEvents.generate_portfolio(count)

        assert len(portfolios) == expected_length
        if portfolios:
            for portfolio in portfolios:
                assert isinstance(portfolio["portfolio_id"], str)
                assert isinstance(portfolio["user_id"], str)
                assert 1 <= portfolio["total_value"] < 1000
                assert portfolio["risk_profile"] in ["low", "medium", "high"]
                assert isinstance(portfolio["created_at"], (str, date, datetime))

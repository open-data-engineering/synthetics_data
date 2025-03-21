import pytest
from unittest.mock import patch
import logging

from services.payment import TransactionService

logger = logging.getLogger(__name__)


class TestTransactionService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_transactions", "zero_transactions", "many_transactions"],
    )
    @patch("services.payment.PaymentsEvents")
    def test_insert_transactions(self, MockPaymentsEvents, count):
        MockPaymentsEvents.generate_transactions.return_value = [
            {"transaction_id": i} for i in range(count)
        ]

        transactions = TransactionService.insert_transactions(count)

        assert len(transactions) == count
        MockPaymentsEvents.generate_transactions.assert_called_once_with(count)

    @patch("services.payment.PaymentsEvents.generate_transactions")
    def test_insert_transactions_exception(self, mock_generate_transactions, caplog):
        mock_generate_transactions.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            transactions = TransactionService.insert_transactions(5)

        assert transactions == []
        assert "Erro ao inserir transações" in caplog.text

    @pytest.mark.parametrize(
        "count",
        [
            (3),
            (0),
            (50),
        ],
        ids=["few_payment_methods", "zero_payment_methods", "many_payment_methods"],
    )
    @patch("services.payment.PaymentsEvents")
    def test_insert_payment_methods(self, MockPaymentsEvents, count):
        MockPaymentsEvents.generate_payment_methods.return_value = [
            {"method_id": i} for i in range(count)
        ]

        payment_methods = TransactionService.insert_payment_methods(count)

        assert len(payment_methods) == count
        MockPaymentsEvents.generate_payment_methods.assert_called_once_with(count)

    @patch("services.payment.PaymentsEvents.generate_payment_methods")
    def test_insert_payment_methods_exception(
        self, mock_generate_payment_methods, caplog
    ):
        mock_generate_payment_methods.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            payment_methods = TransactionService.insert_payment_methods(5)

        assert payment_methods == []
        assert "Erro ao inserir métodos de pagamento" in caplog.text

    @pytest.mark.parametrize(
        "count",
        [
            (2),
            (0),
            (25),
        ],
        ids=["few_merchants", "zero_merchants", "many_merchants"],
    )
    @patch("services.payment.PaymentsEvents")
    def test_insert_merchants(self, MockPaymentsEvents, count):
        MockPaymentsEvents.generate_merchants.return_value = [
            {"merchant_id": i} for i in range(count)
        ]

        merchants = TransactionService.insert_merchants(count)

        assert len(merchants) == count
        MockPaymentsEvents.generate_merchants.assert_called_once_with(count)

    @patch("services.payment.PaymentsEvents.generate_merchants")
    def test_insert_merchants_exception(self, mock_generate_merchants, caplog):
        mock_generate_merchants.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            merchants = TransactionService.insert_merchants(5)

        assert merchants == []
        assert "Erro ao inserir comerciantes" in caplog.text

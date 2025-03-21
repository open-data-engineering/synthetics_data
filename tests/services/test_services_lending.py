import pytest
from unittest.mock import patch
import logging

from src.services.lending import LoanService

logger = logging.getLogger(__name__)


class TestLoanService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_loans", "zero_loans", "many_loans"],
    )
    @patch("src.services.lending.LendingEvents")
    def test_insert_loans(self, MockLendingEvents, count):
        MockLendingEvents.generate_loans.return_value = [
            {"loan_id": i} for i in range(count)
        ]

        loans = LoanService.insert_loans(count)

        assert len(loans) == count
        MockLendingEvents.generate_loans.assert_called_once_with(count)

    @patch("src.services.lending.LendingEvents.generate_loans")
    def test_insert_loans_exception(self, mock_generate_loans, caplog):
        mock_generate_loans.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            loans = LoanService.insert_loans(5)

        assert loans == []
        assert "Erro ao inserir empréstimos" in caplog.text

    @pytest.mark.parametrize(
        "count",
        [
            (3),
            (0),
            (50),
        ],
        ids=["few_payments", "zero_payments", "many_payments"],
    )
    @patch("src.services.lending.LendingEvents")
    def test_insert_payments(self, MockLendingEvents, count):
        MockLendingEvents.generate_payments.return_value = [
            {"payment_id": i} for i in range(count)
        ]

        payments = LoanService.insert_payments(count)

        assert len(payments) == count
        MockLendingEvents.generate_payments.assert_called_once_with(count)

    @patch("src.services.lending.LendingEvents.generate_payments")
    def test_insert_payments_exception(self, mock_generate_payments, caplog):
        mock_generate_payments.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            payments = LoanService.insert_payments(5)

        assert payments == []
        assert "Erro ao inserir pagamentos" in caplog.text

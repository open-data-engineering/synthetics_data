import pytest
import logging
from unittest.mock import patch, MagicMock

from generator.core import SyntheticDataGenerator
from src.services.account import AccountService
from src.services.audit import AuditService
from src.services.compliance import ComplianceService
from src.services.credit import CreditService
from src.services.entities import EntityService
from src.services.insurance import InsuranceService
from src.services.investments import PortfolioService
from src.services.lending import LoanService
from src.services.payment import TransactionService


@pytest.mark.parametrize(
    "service, function_name, table_name, count, expected_data",
    [
        (AccountService, "insert_users", "users", 20000, {"users": "mock_data"}),
        (AuditService, "insert_audits", "audits", 1000, {"audits": "mock_data"}),
        (
            ComplianceService,
            "insert_regulations",
            "regulations",
            5000,
            {"regulations": "mock_data"},
        ),
        (
            CreditService,
            "insert_credit_scores",
            "credit_scores",
            100,
            {"credit_scores": "mock_data"},
        ),
        (EntityService, "insert_entities", "entities", 0, {"entities": "mock_data"}),
        (
            InsuranceService,
            "insert_policies",
            "policies",
            10000,
            {"policies": "mock_data"},
        ),
        (
            PortfolioService,
            "insert_portfolios",
            "portfolios",
            500,
            {"portfolios": "mock_data"},
        ),
        (LoanService, "insert_loans", "loans", 200, {"loans": "mock_data"}),
        (
            TransactionService,
            "insert_transactions",
            "transactions",
            1000,
            {"transactions": "mock_data"},
        ),
    ],
)
@patch("generator.core.logging.info")
def test_generate_happy_path(
    mock_logging_info, service, function_name, table_name, count, expected_data
):
    """Tests the generate method with valid service functions and various counts."""

    generator = SyntheticDataGenerator()
    mock_function = MagicMock(return_value="mock_data")

    with patch.object(service, function_name, mock_function):
        generator.operations = [(service, function_name, table_name, count)]
        result = generator.generate(override_counts={table_name: count})

        assert result == expected_data
        mock_function.assert_called_once_with(count)


@patch("generator.core.logging.error")
def test_generate_missing_function(mock_logging_error):
    """Tests the generate method when a service function is missing."""

    generator = SyntheticDataGenerator()
    generator.operations = [
        (AccountService, "missing_function", "missing_table", 20000)
    ]

    result = generator.generate()

    assert result == {}
    mock_logging_error.assert_called_once()


@patch("generator.core.logging.error")
def test_generate_exception_during_insertion(mock_logging_error):
    """Tests the generate method when an exception occurs during data insertion."""

    generator = SyntheticDataGenerator()

    with patch.object(
        AccountService, "insert_users", side_effect=Exception("Mock Exception")
    ):
        result = generator.generate()

        assert result == {}
        mock_logging_error.assert_called_once()

import pytest
from unittest.mock import patch
import logging

from services.account import AccountService

logger = logging.getLogger(__name__)


class TestAccountService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_users", "zero_users", "many_users"],
    )
    @patch("services.account.AccountEvents")
    def test_insert_users(self, MockAccountEvents, count):
        MockAccountEvents.generate_users.return_value = [
            {"user_id": i} for i in range(count)
        ]

        users = AccountService.insert_users(count)

        assert len(users) == count
        MockAccountEvents.generate_users.assert_called_once_with(count)

    @pytest.mark.parametrize(
        "count",
        [
            (3),
            (0),
            (50),
        ],
        ids=["few_accounts", "zero_accounts", "many_accounts"],
    )
    @patch("services.account.AccountEvents")
    def test_insert_accounts(self, MockAccountEvents, count):
        MockAccountEvents.generate_accounts.return_value = [
            {"account_id": i} for i in range(count)
        ]

        accounts = AccountService.insert_accounts(count)

        assert len(accounts) == count
        MockAccountEvents.generate_accounts.assert_called_once_with(count)

    @pytest.mark.parametrize(
        "count",
        [
            (2),
            (0),
            (25),
        ],
        ids=["few_subaccounts", "zero_subaccounts", "many_subaccounts"],
    )
    @patch("services.account.AccountEvents")
    def test_insert_subaccounts(self, MockAccountEvents, count):
        MockAccountEvents.generate_subaccounts.return_value = [
            {"subaccount_id": i} for i in range(count)
        ]

        subaccounts = AccountService.insert_subaccounts(count)

        assert len(subaccounts) == count
        MockAccountEvents.generate_subaccounts.assert_called_once_with(count)

    @pytest.mark.parametrize(
        "method_name, event_method",
        [
            ("insert_users", "generate_users"),
            ("insert_accounts", "generate_accounts"),
            ("insert_subaccounts", "generate_subaccounts"),
        ],
        ids=["users_exception", "accounts_exception", "subaccounts_exception"],
    )
    @patch("services.account.AccountEvents")
    def test_insert_exception(
        self, MockAccountEvents, method_name, event_method, caplog
    ):
        getattr(MockAccountEvents, event_method).side_effect = Exception(
            "Test Exception"
        )

        with caplog.at_level(logging.ERROR):
            result = getattr(AccountService, method_name)(5)

        assert result == []
        assert "Erro ao inserir" in caplog.text

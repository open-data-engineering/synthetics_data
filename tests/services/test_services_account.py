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
        ids=["insert_few_users", "insert_zero_users", "insert_many_users"],
    )
    @patch("src.services.account.AccountEvents")
    def test_insert_users(self, MockAccountEvents, count):
        MockAccountEvents.insert_users.return_value = [
            {"user_id": i} for i in range(count)
        ]

        users = AccountService.insert_users(count)

        assert len(users) == count
        MockAccountEvents.insert_users.assert_called_once_with(count)

    @pytest.mark.parametrize(
        "count",
        [
            (3),
            (0),
            (50),
        ],
        ids=["insert_few_accounts", "insert_zero_accounts", "insert_many_accounts"],
    )
    @patch("src.services.account.AccountEvents")
    def test_insert_accounts(self, MockAccountEvents, count):
        MockAccountEvents.insert_accounts.return_value = [
            {"account_id": i} for i in range(count)
        ]

        accounts = AccountService.insert_accounts(count)

        assert len(accounts) == count
        MockAccountEvents.insert_accounts.assert_called_once_with(count)

    @pytest.mark.parametrize(
        "count",
        [
            (2),
            (0),
            (25),
        ],
        ids=[
            "insert_few_subaccounts",
            "insert_zero_subaccounts",
            "insert_many_subaccounts",
        ],
    )
    @patch("src.services.account.AccountEvents")
    def test_insert_subaccounts(self, MockAccountEvents, count):
        MockAccountEvents.insert_subaccounts.return_value = [
            {"subaccount_id": i} for i in range(count)
        ]

        subaccounts = AccountService.insert_subaccounts(count)

        assert len(subaccounts) == count
        MockAccountEvents.insert_subaccounts.assert_called_once_with(count)

    @pytest.mark.parametrize(
        "method_name",
        [
            ("insert_users"),
            ("insert_accounts"),
            ("insert_subaccounts"),
        ],
        ids=["users_exception", "accounts_exception", "subaccounts_exception"],
    )
    @patch("src.services.account.AccountEvents")
    def test_insert_exception(self, MockAccountEvents, method_name, caplog):
        MockAccountEvents.insert_users.side_effect = Exception("Test Exception")
        MockAccountEvents.insert_accounts.side_effect = Exception("Test Exception")
        MockAccountEvents.insert_subaccounts.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):

            result = getattr(AccountService, method_name)(5)

            assert result == []
            assert "Erro ao inserir" in caplog.text

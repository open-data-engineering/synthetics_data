import pytest
from pydantic import ValidationError
from datetime import datetime, timezone

from models.account import Account, Subaccount, User


class TestAccount:
    @pytest.mark.parametrize(
        "account_id, account_type, balance, currency, status, user_id, created_at",
        [
            (
                "123",
                "checking",
                1000,
                "USD",
                "active",
                "user123",
                datetime.now(timezone.utc),
            ),
            (
                "456",
                "savings",
                0,
                "EUR",
                "inactive",
                "user456",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "789",
                "investment",
                1000000,
                "BRL",
                "pending",
                "user789",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_account", "zero_balance_inactive", "large_balance_pending"],
    )
    def test_valid_account(
        self, account_id, account_type, balance, currency, status, user_id, created_at
    ):
        account = Account(
            account_id=account_id,
            account_type=account_type,
            balance=balance,
            currency=currency,
            status=status,
            user_id=user_id,
            created_at=created_at,
        )
        assert account.account_id == account_id
        assert account.account_type == account_type
        assert account.balance == balance
        assert account.currency == currency
        assert account.status == status
        assert account.user_id == user_id
        assert account.created_at == created_at

    @pytest.mark.parametrize(
        "account_id, account_type, balance, currency, status, user_id, created_at, expected_error",
        [
            (
                123,
                "checking",
                1000,
                "USD",
                "active",
                "user123",
                datetime.now(timezone.utc),
                r"account_id\n\s+Input should be a valid string",
            ),
            (
                "456",
                123,
                1000,
                "USD",
                "active",
                "user123",
                datetime.now(timezone.utc),
                r"account_type\n\s+Input should be a valid string",
            ),
            (
                "123",
                "checking",
                1000,
                123,
                "active",
                "user123",
                datetime.now(timezone.utc),
                r"currency\n\s+Input should be a valid string",
            ),
            (
                "456",
                "checking",
                1000,
                "USD",
                123,
                "user123",
                datetime.now(timezone.utc),
                r"status\n\s+Input should be a valid string",
            ),
            (
                "789",
                "checking",
                1000,
                "USD",
                "active",
                456,
                datetime.now(timezone.utc),
                r"user_id\n\s+Input should be a valid string",
            ),
            (
                "123",
                "checking",
                1000,
                "USD",
                "active",
                "user123",
                "now",
                r"created_at\n\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_account_id",
            "invalid_account_type",
            "invalid_currency",
            "invalid_status",
            "invalid_user_id",
            "invalid_created_at",
        ],
    )
    def test_invalid_account(
        self,
        account_id,
        account_type,
        balance,
        currency,
        status,
        user_id,
        created_at,
        expected_error,
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Account(
                account_id=account_id,
                account_type=account_type,
                balance=balance,
                currency=currency,
                status=status,
                user_id=user_id,
                created_at=created_at,
            )


class TestSubaccount:
    @pytest.mark.parametrize(
        "subaccount_id, parent_account_id, purpose, balance, created_at",
        [
            ("sub123", "acc456", "savings", 500, datetime.now(timezone.utc)),
            (
                "sub789",
                "acc012",
                "emergency fund",
                0,
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "sub456",
                "acc789",
                "investment",
                10000,
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_subaccount", "zero_balance", "large_balance"],
    )
    def test_valid_subaccount(
        self, subaccount_id, parent_account_id, purpose, balance, created_at
    ):

        subaccount = Subaccount(
            subaccount_id=subaccount_id,
            parent_account_id=parent_account_id,
            purpose=purpose,
            balance=balance,
            created_at=created_at,
        )

        assert subaccount.subaccount_id == subaccount_id
        assert subaccount.parent_account_id == parent_account_id
        assert subaccount.purpose == purpose
        assert subaccount.balance == balance
        assert subaccount.created_at == created_at

    @pytest.mark.parametrize(
        "subaccount_id, parent_account_id, purpose, balance, created_at, expected_error",
        [
            (
                123,
                "acc456",
                "savings",
                500,
                datetime.now(timezone.utc),
                r"subaccount_id\n\s+Input should be a valid string",
            ),
            (
                "sub789",
                456,
                "savings",
                500,
                datetime.now(timezone.utc),
                r"parent_account_id\n\s+Input should be a valid string",
            ),
            (
                "sub123",
                "acc789",
                123,
                500,
                datetime.now(timezone.utc),
                r"purpose\n\s+Input should be a valid string",
            ),
            (
                "sub456",
                "acc012",
                "savings",
                "500",
                datetime.now(timezone.utc),
                r"balance\n\s+Input should be a valid integer",
            ),
            (
                "sub789",
                "acc456",
                "savings",
                500,
                "now",
                r"created_at\n\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_subaccount_id",
            "invalid_parent_account_id",
            "invalid_purpose",
            "invalid_balance",
            "invalid_created_at",
        ],
    )
    def test_invalid_subaccount(
        self,
        subaccount_id,
        parent_account_id,
        purpose,
        balance,
        created_at,
        expected_error,
    ):

        with pytest.raises(ValidationError, match=expected_error):
            Subaccount(
                subaccount_id=subaccount_id,
                parent_account_id=parent_account_id,
                purpose=purpose,
                balance=balance,
                created_at=created_at,
            )


class TestUser:
    @pytest.mark.parametrize(
        "user_id, name, email, phone, created_at",
        [
            (
                "user123",
                "John Doe",
                "john.doe@example.com",
                "+15551234567",
                datetime.now(timezone.utc),
            ),
            (
                "user456",
                "Jane Doe",
                "jane.doe@example.com",
                "+447700900123",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "user789",
                "Peter Pan",
                "peter.pan@example.com",
                "",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_user", "different_phone", "empty_phone"],
    )
    def test_valid_user(self, user_id, name, email, phone, created_at):

        user = User(
            user_id=user_id, name=name, email=email, phone=phone, created_at=created_at
        )

        assert user.user_id == user_id
        assert user.name == name
        assert user.email == email
        assert user.phone == phone
        assert user.created_at == created_at

    @pytest.mark.parametrize(
        "user_id, name, email, phone, created_at, expected_error",
        [
            (
                123,
                "John Doe",
                "john.doe@example.com",
                "+15551234567",
                datetime.now(timezone.utc),
                r"user_id\n\s+Input should be a valid string",
            ),
            (
                "user456",
                123,
                "john.doe@example.com",
                "+15551234567",
                datetime.now(timezone.utc),
                r"name\n\s+Input should be a valid string",
            ),
            (
                "user123",
                "John Doe",
                "invalid_email",
                "+15551234567",
                datetime.now(timezone.utc),
                r"email\n\s+value is not a valid email address",
            ),
            (
                "user789",
                "John Doe",
                "john.doe@example.com",
                123,
                datetime.now(timezone.utc),
                r"phone\n\s+Input should be a valid string",
            ),
            (
                "user456",
                "John Doe",
                "john.doe@example.com",
                "+15551234567",
                "now",
                r"created_at\n\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_user_id",
            "invalid_name",
            "invalid_email",
            "invalid_phone",
            "invalid_created_at",
        ],
    )
    def test_invalid_user(
        self, user_id, name, email, phone, created_at, expected_error
    ):

        with pytest.raises(ValidationError, match=expected_error):
            User(
                user_id=user_id,
                name=name,
                email=email,
                phone=phone,
                created_at=created_at,
            )

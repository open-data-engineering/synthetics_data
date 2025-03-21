import pytest
from uuid import UUID
from src.commons.accounts import AccountEvents
from faker import Faker

fake = Faker("pt_BR")


@pytest.mark.parametrize(
    "count",
    [
        (1),
        (10),
        (0),
    ],
)
def test_generate_accounts(count):
    """Tests the generate_accounts method with various counts."""

    accounts = AccountEvents.generate_accounts(count)

    assert len(accounts) == count
    for account in accounts:
        assert isinstance(UUID(account["account_id"]), UUID)
        assert isinstance(UUID(account["user_id"]), UUID)
        assert 100 <= account["balance"] <= 10000
        assert account["currency"] in ["USD", "BRL", "EUR"]
        assert isinstance(account["created_at"], str)
        assert account["account_type"] in ["personal", "business"]
        assert account["status"] in ["active", "inactive"]


@pytest.mark.parametrize(
    "count",
    [
        (1),
        (5),
        (0),
    ],
)
def test_generate_subaccounts(count):
    """Tests the generate_subaccounts method with various counts."""

    subaccounts = AccountEvents.generate_subaccounts(count)

    assert len(subaccounts) == count
    for subaccount in subaccounts:
        assert isinstance(UUID(subaccount["subaccount_id"]), UUID)
        assert isinstance(UUID(subaccount["parent_account_id"]), UUID)
        assert 50 <= subaccount["balance"] <= 5000
        assert isinstance(subaccount["created_at"], str)
        assert isinstance(subaccount["purpose"], str)


@pytest.mark.parametrize(
    "count",
    [
        (1),
        (100),
        (0),
    ],
)
def test_generate_users(count):
    """Tests the generate_users method with various counts."""

    users = AccountEvents.generate_users(count)

    assert len(users) == count
    for user in users:
        assert isinstance(UUID(user["user_id"]), UUID)
        assert isinstance(user["name"], str)
        assert isinstance(user["email"], str)
        assert isinstance(user["phone"], str)
        assert isinstance(user["created_at"], str)

import pytest
from pydantic import ValidationError
from datetime import datetime, timezone

from src.models.payment import Transaction, PaymentMethod, Merchant


class TestTransaction:
    @pytest.mark.parametrize(
        "transaction_id, amount, currency, status, timestamp, sender_id, receiver_id, created_at",
        [
            (
                "transaction123",
                100,
                "USD",
                "completed",
                datetime.now(timezone.utc),
                "sender456",
                "receiver789",
                datetime.now(timezone.utc),
            ),
            (
                "transaction456",
                10000,
                "EUR",
                "pending",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                "sender012",
                "receiver123",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "transaction789",
                1,
                "BRL",
                "failed",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                "sender789",
                "receiver456",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_transaction", "pending_transaction", "failed_small_amount"],
    )
    def test_valid_transaction(
        self,
        transaction_id,
        amount,
        currency,
        status,
        timestamp,
        sender_id,
        receiver_id,
        created_at,
    ):
        transaction = Transaction(
            transaction_id=transaction_id,
            amount=amount,
            currency=currency,
            status=status,
            timestamp=timestamp,
            sender_id=sender_id,
            receiver_id=receiver_id,
            created_at=created_at,
        )

        assert transaction.transaction_id == transaction_id
        assert transaction.amount == amount
        assert transaction.currency == currency
        assert transaction.status == status
        assert transaction.timestamp == timestamp
        assert transaction.sender_id == sender_id
        assert transaction.receiver_id == receiver_id
        assert transaction.created_at == created_at

    @pytest.mark.parametrize(
        "transaction_id, amount, currency, status, timestamp, sender_id, receiver_id, created_at, expected_error",
        [
            (
                123,
                100,
                "USD",
                "completed",
                datetime.now(timezone.utc),
                "sender456",
                "receiver789",
                datetime.now(timezone.utc),
                r"transaction_id\s+Input should be a valid string",
            ),
            (
                "transaction123",
                "100",
                "USD",
                "completed",
                datetime.now(timezone.utc),
                "sender456",
                "receiver789",
                datetime.now(timezone.utc),
                r"amount\s+Input should be a valid integer",
            ),
            (
                "transaction456",
                100,
                456,
                "completed",
                datetime.now(timezone.utc),
                "sender012",
                "receiver123",
                datetime.now(timezone.utc),
                r"currency\s+Input should be a valid string",
            ),
            (
                "transaction789",
                100,
                "BRL",
                789,
                datetime.now(timezone.utc),
                "sender789",
                "receiver456",
                datetime.now(timezone.utc),
                r"status\s+Input should be a valid string",
            ),
            (
                "transaction123",
                100,
                "USD",
                "completed",
                "now",
                "sender456",
                "receiver789",
                datetime.now(timezone.utc),
                r"timestamp\s+Input should be a valid datetime or date",
            ),
            (
                "transaction456",
                10000,
                "EUR",
                "pending",
                datetime.now(timezone.utc),
                12,
                "receiver123",
                datetime.now(timezone.utc),
                r"sender_id\s+Input should be a valid string",
            ),
            (
                "transaction789",
                1,
                "BRL",
                "failed",
                datetime.now(timezone.utc),
                "sender789",
                46,
                datetime.now(timezone.utc),
                r"receiver_id\s+Input should be a valid string",
            ),
            (
                "transaction123",
                100,
                "USD",
                "completed",
                datetime.now(timezone.utc),
                "sender456",
                "receiver789",
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_transaction_id",
            "invalid_amount",
            "invalid_currency",
            "invalid_status",
            "invalid_timestamp",
            "invalid_sender_id",
            "invalid_receiver_id",
            "invalid_created_at",
        ],
    )
    def test_invalid_transaction(
        self,
        transaction_id,
        amount,
        currency,
        status,
        timestamp,
        sender_id,
        receiver_id,
        created_at,
        expected_error,
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Transaction(
                transaction_id=transaction_id,
                amount=amount,
                currency=currency,
                status=status,
                timestamp=timestamp,
                sender_id=sender_id,
                receiver_id=receiver_id,
                created_at=created_at,
            )


class TestPayment:
    @pytest.mark.parametrize(
        "method_id, type, details, user_id, created_at",
        [
            (
                "method123",
                "credit_card",
                "1234567890123456",
                "user456",
                datetime.now(timezone.utc),
            ),
            (
                "method456",
                "debit_card",
                "6543210987654321",
                "user789",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "method789",
                "paypal",
                "9876543210123456",
                "user012",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["credit_card", "debit_card", "paypal"],
    )
    def test_valid_payment_method(self, method_id, type, details, user_id, created_at):
        payment_method = PaymentMethod(
            method_id=method_id,
            type=type,
            details=details,
            user_id=user_id,
            created_at=created_at,
        )

        assert payment_method.method_id == method_id
        assert payment_method.type == type
        assert payment_method.details == details
        assert payment_method.user_id == user_id
        assert payment_method.created_at == created_at

    @pytest.mark.parametrize(
        "method_id, type, details, user_id, created_at, expected_error",
        [
            (
                123,
                "credit_card",
                "1234567890123456",
                "user456",
                datetime.now(timezone.utc),
                r"method_id\s+Input should be a valid string",
            ),
            (
                "method123",
                123,
                "1234567890123456",
                "user456",
                datetime.now(timezone.utc),
                r"type\s+Input should be a valid string",
            ),
            (
                "method123",
                "credit_card",
                1234567890123456,
                "user456",
                datetime.now(timezone.utc),
                r"details\s+Input should be a valid string",
            ),
            (
                "method123",
                "credit_card",
                "1234567890123456",
                456,
                datetime.now(timezone.utc),
                r"user_id\s+Input should be a valid string",
            ),
            (
                "method123",
                "credit_card",
                "1234567890123456",
                "user456",
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_method_id",
            "invalid_type",
            "invalid_details",
            "invalid_user_id",
            "invalid_created_at",
        ],
    )
    def test_invalid_payment_method(
        self, method_id, type, details, user_id, created_at, expected_error
    ):
        with pytest.raises(ValidationError, match=expected_error):
            PaymentMethod(
                method_id=method_id,
                type=type,
                details=details,
                user_id=user_id,
                created_at=created_at,
            )


class TestMerchant:
    @pytest.mark.parametrize(
        "merchant_id, name, category, contact_info, created_at",
        [
            (
                "merchant123",
                "Merchant One",
                "retail",
                "1234567890",
                datetime.now(timezone.utc),
            ),
            (
                "merchant456",
                "Merchant Two",
                "online",
                "0987654321",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "merchant789",
                "Merchant Three",
                "grocery",
                "5432109876",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["retail", "online", "grocery"],
    )
    def test_valid_merchant(
        self, merchant_id, name, category, contact_info, created_at
    ):
        merchant = Merchant(
            merchant_id=merchant_id,
            name=name,
            category=category,
            contact_info=contact_info,
            created_at=created_at,
        )

        assert merchant.merchant_id == merchant_id
        assert merchant.name == name
        assert merchant.category == category
        assert merchant.contact_info == contact_info
        assert merchant.created_at == created_at

    @pytest.mark.parametrize(
        "merchant_id, name, category, contact_info, created_at, expected_error",
        [
            (
                123,
                "Merchant One",
                "retail",
                "1234567890",
                datetime.now(timezone.utc),
                r"merchant_id\s+Input should be a valid string",
            ),
            (
                "merchant123",
                123,
                "retail",
                "1234567890",
                datetime.now(timezone.utc),
                r"name\s+Input should be a valid string",
            ),
            (
                "merchant123",
                "Merchant One",
                123,
                "1234567890",
                datetime.now(timezone.utc),
                r"category\s+Input should be a valid string",
            ),
            (
                "merchant123",
                "Merchant One",
                "retail",
                1234567890,
                datetime.now(timezone.utc),
                r"contact_info\s+Input should be a valid string",
            ),
            (
                "merchant123",
                "Merchant One",
                "retail",
                "1234567890",
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_merchant_id",
            "invalid_name",
            "invalid_category",
            "invalid_contact_info",
            "invalid_created_at",
        ],
    )
    def test_invalid_merchant(
        self, merchant_id, name, category, contact_info, created_at, expected_error
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Merchant(
                merchant_id=merchant_id,
                name=name,
                category=category,
                contact_info=contact_info,
                created_at=created_at,
            )

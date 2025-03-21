import pytest
from pydantic import ValidationError
from datetime import datetime, timezone

from src.models.lending import Loan, Payment


class TestLoan:
    @pytest.mark.parametrize(
        "loan_id, user_id, amount, interest_rate, term, created_at",
        [
            ("loan123", "user456", 10000, 5.0, 36, datetime.now(timezone.utc)),
            (
                "loan789",
                "user012",
                100000,
                2.5,
                60,
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "loan456",
                "user789",
                1000,
                10.0,
                12,
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_loan", "large_amount", "small_amount_short_term"],
    )
    def test_valid_loan(
        self, loan_id, user_id, amount, interest_rate, term, created_at
    ):
        loan = Loan(
            loan_id=loan_id,
            user_id=user_id,
            amount=amount,
            interest_rate=interest_rate,
            term=term,
            created_at=created_at,
        )

        assert loan.loan_id == loan_id
        assert loan.user_id == user_id
        assert loan.amount == amount
        assert loan.interest_rate == interest_rate
        assert loan.term == term
        assert loan.created_at == created_at

    @pytest.mark.parametrize(
        "loan_id, user_id, amount, interest_rate, term, created_at, expected_error",
        [
            (
                123,
                "user456",
                10000,
                5.0,
                36,
                datetime.now(timezone.utc),
                r"loan_id\s+Input should be a valid string",
            ),
            (
                "loan789",
                456,
                10000,
                5.0,
                36,
                datetime.now(timezone.utc),
                r"user_id\s+Input should be a valid string",
            ),
            (
                "loan123",
                "user012",
                "10000",
                5.0,
                36,
                datetime.now(timezone.utc),
                r"amount\s+Input should be a valid integer",
            ),
            (
                "loan456",
                "user789",
                10000,
                "5.0",
                36,
                datetime.now(timezone.utc),
                r"interest_rate\s+Input should be a valid number",
            ),
            (
                "loan789",
                "user456",
                10000,
                5.0,
                "36",
                datetime.now(timezone.utc),
                r"term\s+Input should be a valid integer",
            ),
            (
                "loan123",
                "user012",
                10000,
                5.0,
                36,
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_loan_id",
            "invalid_user_id",
            "invalid_amount",
            "invalid_interest_rate",
            "invalid_term",
            "invalid_created_at",
        ],
    )
    def test_invalid_loan(
        self, loan_id, user_id, amount, interest_rate, term, created_at, expected_error
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Loan(
                loan_id=loan_id,
                user_id=user_id,
                amount=amount,
                interest_rate=interest_rate,
                term=term,
                created_at=created_at,
            )


class TestPayment:
    @pytest.mark.parametrize(
        "payment_id, loan_id, amount, date, status, created_at",
        [
            (
                "payment123",
                "loan456",
                1000,
                datetime.now(timezone.utc),
                "paid",
                datetime.now(timezone.utc),
            ),
            (
                "payment789",
                "loan012",
                10000,
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                "pending",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "payment456",
                "loan789",
                100,
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                "overdue",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_payment", "large_amount", "small_amount_short_term"],
    )
    def test_valid_payment(self, payment_id, loan_id, amount, date, status, created_at):
        payment = Payment(
            payment_id=payment_id,
            loan_id=loan_id,
            amount=amount,
            date=date,
            status=status,
            created_at=created_at,
        )

        assert payment.payment_id == payment_id
        assert payment.loan_id == loan_id
        assert payment.amount == amount
        assert payment.date == date
        assert payment.status == status
        assert payment.created_at == created_at

    @pytest.mark.parametrize(
        "payment_id, loan_id, amount, date, status, created_at, expected_error",
        [
            (
                123,
                "loan456",
                1000,
                datetime.now(timezone.utc),
                "paid",
                datetime.now(timezone.utc),
                r"payment_id\s+Input should be a valid string",
            ),
            (
                "payment789",
                456,
                1000,
                datetime.now(timezone.utc),
                "paid",
                datetime.now(timezone.utc),
                r"loan_id\s+Input should be a valid string",
            ),
            (
                "payment123",
                "loan012",
                "1000",
                datetime.now(timezone.utc),
                "paid",
                datetime.now(timezone.utc),
                r"amount\s+Input should be a valid integer",
            ),
            (
                "payment456",
                "loan789",
                1000,
                "now",
                "paid",
                datetime.now(timezone.utc),
                r"date\s+Input should be a valid datetime or date",
            ),
            (
                "payment789",
                "loan456",
                1000,
                datetime.now(timezone.utc),
                "paid",
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_payment_id",
            "invalid_loan_id",
            "invalid_amount",
            "invalid_date",
            "invalid_created_at",
        ],
    )
    def test_invalid_payment(
        self, payment_id, loan_id, amount, date, status, created_at, expected_error
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Payment(
                payment_id=payment_id,
                loan_id=loan_id,
                amount=amount,
                date=date,
                status=status,
                created_at=created_at,
            )

import pytest
from pydantic import ValidationError
from datetime import datetime, timezone

from models.investments import Portfolio


class TestPortfolio:
    @pytest.mark.parametrize(
        "portfolio_id, user_id, total_value, risk_profile, created_at",
        [
            (
                "portfolio123",
                "user456",
                10000,
                "conservative",
                datetime.now(timezone.utc),
            ),
            (
                "portfolio789",
                "user012",
                0,
                "aggressive",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "portfolio456",
                "user789",
                1000000,
                "moderate",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_portfolio", "zero_value", "large_value"],
    )
    def test_valid_portfolio(
        self, portfolio_id, user_id, total_value, risk_profile, created_at
    ):
        portfolio = Portfolio(
            portfolio_id=portfolio_id,
            user_id=user_id,
            total_value=total_value,
            risk_profile=risk_profile,
            created_at=created_at,
        )

        assert portfolio.portfolio_id == portfolio_id
        assert portfolio.user_id == user_id
        assert portfolio.total_value == total_value
        assert portfolio.risk_profile == risk_profile
        assert portfolio.created_at == created_at

    @pytest.mark.parametrize(
        "portfolio_id, user_id, total_value, risk_profile, created_at, expected_error",
        [
            (
                123,
                "user456",
                10000,
                "conservative",
                datetime.now(timezone.utc),
                r"portfolio_id\s+Input should be a valid string",
            ),
            (
                "portfolio789",
                456,
                10000,
                "conservative",
                datetime.now(timezone.utc),
                r"user_id\s+Input should be a valid string",
            ),
            (
                "portfolio123",
                "user012",
                "10000",
                "conservative",
                datetime.now(timezone.utc),
                r"total_value\s+Input should be a valid integer",
            ),
            (
                "portfolio456",
                "user789",
                10000,
                123,
                datetime.now(timezone.utc),
                r"risk_profile\s+Input should be a valid string",
            ),
            (
                "portfolio789",
                "user456",
                10000,
                "conservative",
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_portfolio_id",
            "invalid_user_id",
            "invalid_total_value",
            "invalid_risk_profile",
            "invalid_created_at",
        ],
    )
    def test_invalid_portfolio(
        self,
        portfolio_id,
        user_id,
        total_value,
        risk_profile,
        created_at,
        expected_error,
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Portfolio(
                portfolio_id=portfolio_id,
                user_id=user_id,
                total_value=total_value,
                risk_profile=risk_profile,
                created_at=created_at,
            )

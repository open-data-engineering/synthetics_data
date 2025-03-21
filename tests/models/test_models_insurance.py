import pytest
from pydantic import ValidationError
from datetime import datetime, timezone

from src.models.insurance import Policy, Claim, InsuredEntity


class TestPolicy:
    @pytest.mark.parametrize(
        "policy_id, type, coverage_amount, premium, start_date, end_date, user_id, created_at",
        [
            (
                "policy123",
                "health",
                50000,
                200,
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                datetime(2024, 12, 31, tzinfo=timezone.utc),
                "user456",
                datetime.now(timezone.utc),
            ),
            (
                "policy789",
                "auto",
                100000,
                500,
                datetime(2025, 1, 1, tzinfo=timezone.utc),
                datetime(2025, 12, 31, tzinfo=timezone.utc),
                "user012",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "policy456",
                "home",
                250000,
                1000,
                datetime.now(timezone.utc),
                datetime(2026, 12, 31, tzinfo=timezone.utc),
                "user789",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_policy", "future_dates", "past_created_at"],
    )
    def test_valid_policy(
        self,
        policy_id,
        type,
        coverage_amount,
        premium,
        start_date,
        end_date,
        user_id,
        created_at,
    ):
        policy = Policy(
            policy_id=policy_id,
            type=type,
            coverage_amount=coverage_amount,
            premium=premium,
            start_date=start_date,
            end_date=end_date,
            user_id=user_id,
            created_at=created_at,
        )

        assert policy.policy_id == policy_id
        assert policy.type == type
        assert policy.coverage_amount == coverage_amount
        assert policy.premium == premium
        assert policy.start_date == start_date
        assert policy.end_date == end_date
        assert policy.user_id == user_id
        assert policy.created_at == created_at

    @pytest.mark.parametrize(
        "policy_id, coverage_amount, premium, start_date, end_date, created_at, expected_error, type, user_id",
        [
            (
                "POL123",
                100000,
                1200,
                "not-a-date",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                datetime.now(timezone.utc),
                r"start_date\s+Input should be a valid datetime",
                "health",
                "user001",
            ),
            (
                "POL123",
                100000,
                1200,
                datetime.now(timezone.utc),
                "invalid-end",
                datetime.now(timezone.utc),
                r"end_date\s+Input should be a valid datetime",
                "health",
                "user001",
            ),
            (
                "POL123",
                100000,
                1200,
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"user_id\s+Input should be a valid string",
                "auto",
                123,
            ),
        ],
        ids=[
            "invalid_start_date",
            "invalid_end_date",
            "invalid_user_id",
        ],
    )
    def test_invalid_policy(
        self,
        policy_id,
        coverage_amount,
        premium,
        start_date,
        end_date,
        created_at,
        expected_error,
        type,
        user_id,
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Policy(
                policy_id=policy_id,
                type=type,
                coverage_amount=coverage_amount,
                premium=premium,
                start_date=start_date,
                end_date=end_date,
                user_id=user_id,
                created_at=created_at,
            )


class TestClaim:
    @pytest.mark.parametrize(
        "claim_id, policy_id, amount_claimed, status, filed_date, created_at",
        [
            (
                "claim123",
                "policy456",
                10000,
                "approved",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
            ),
            (
                "claim789",
                "policy012",
                500,
                "denied",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "claim456",
                "policy789",
                100000,
                "pending",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_claim", "denied_status", "pending_large_amount"],
    )
    def test_valid_claim(
        self, claim_id, policy_id, amount_claimed, status, filed_date, created_at
    ):
        claim = Claim(
            claim_id=claim_id,
            policy_id=policy_id,
            amount_claimed=amount_claimed,
            status=status,
            filed_date=filed_date,
            created_at=created_at,
        )

        assert claim.claim_id == claim_id
        assert claim.policy_id == policy_id
        assert claim.amount_claimed == amount_claimed
        assert claim.status == status
        assert claim.filed_date == filed_date
        assert claim.created_at == created_at

    @pytest.mark.parametrize(
        "claim_id, policy_id, amount_claimed, status, filed_date, created_at, expected_error",
        [
            (
                123,
                "policy456",
                10000,
                "approved",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"claim_id\s+Input should be a valid string",
            ),
            (
                "claim789",
                456,
                10000,
                "approved",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"policy_id\s+Input should be a valid string",
            ),
            (
                "claim123",
                "policy012",
                "10000",
                "approved",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"amount_claimed\s+Input should be a valid integer",
            ),
            (
                "claim456",
                "policy789",
                10000,
                123,
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"status\s+Input should be a valid string",
            ),
            (
                "claim789",
                "policy456",
                10000,
                "approved",
                "now",
                datetime.now(timezone.utc),
                r"filed_date\s+Input should be a valid datetime or date",
            ),
            (
                "claim123",
                "policy012",
                10000,
                "approved",
                datetime.now(timezone.utc),
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_claim_id",
            "invalid_policy_id",
            "invalid_amount_claimed",
            "invalid_status",
            "invalid_filed_date",
            "invalid_created_at",
        ],
    )
    def test_invalid_claim(
        self,
        claim_id,
        policy_id,
        amount_claimed,
        status,
        filed_date,
        created_at,
        expected_error,
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Claim(
                claim_id=claim_id,
                policy_id=policy_id,
                amount_claimed=amount_claimed,
                status=status,
                filed_date=filed_date,
                created_at=created_at,
            )


class TestInsuredEntity:
    @pytest.mark.parametrize(
        "entity_id, type, description, value, created_at",
        [
            ("entity123", "vehicle", "Car", 25000, datetime.now(timezone.utc)),
            (
                "entity456",
                "property",
                "House",
                500000,
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "entity789",
                "jewelry",
                "Necklace",
                10000,
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_insured_entity", "property_type", "jewelry_end_of_year"],
    )
    def test_valid_insured_entity(
        self, entity_id, type, description, value, created_at
    ):
        insured_entity = InsuredEntity(
            entity_id=entity_id,
            type=type,
            description=description,
            value=value,
            created_at=created_at,
        )

        assert insured_entity.entity_id == entity_id
        assert insured_entity.type == type
        assert insured_entity.description == description
        assert insured_entity.value == value
        assert insured_entity.created_at == created_at

    @pytest.mark.parametrize(
        "entity_id, type, description, value, created_at, expected_error",
        [
            (
                123,
                "vehicle",
                "Car",
                25000,
                datetime.now(timezone.utc),
                r"entity_id\s+Input should be a valid string",
            ),
            (
                "entity456",
                456,
                "House",
                500000,
                datetime.now(timezone.utc),
                r"type\s+Input should be a valid string",
            ),
            (
                "entity123",
                "property",
                123,
                500000,
                datetime.now(timezone.utc),
                r"description\s+Input should be a valid string",
            ),
            (
                "entity789",
                "jewelry",
                "Necklace",
                "10000",
                datetime.now(timezone.utc),
                r"value\s+Input should be a valid integer",
            ),
            (
                "entity456",
                "vehicle",
                "Car",
                25000,
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_entity_id",
            "invalid_type",
            "invalid_description",
            "invalid_value",
            "invalid_created_at",
        ],
    )
    def test_invalid_insured_entity(
        self, entity_id, type, description, value, created_at, expected_error
    ):
        with pytest.raises(ValidationError, match=expected_error):
            InsuredEntity(
                entity_id=entity_id,
                type=type,
                description=description,
                value=value,
                created_at=created_at,
            )

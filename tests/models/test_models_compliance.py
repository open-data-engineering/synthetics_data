import pytest
from pydantic import ValidationError, StrictStr
from datetime import datetime, timezone

from src.models.compliance import Regulation


class TestRegulation:
    @pytest.mark.parametrize(
        "regulation_id, name, description, jurisdiction, date, created_at",
        [
            (
                "reg123",
                "GDPR",
                "General Data Protection Regulation",
                "EU",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
            ),
            (
                "reg456",
                "CCPA",
                "California Consumer Privacy Act",
                "US-CA",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "reg789",
                "LGPD",
                "Lei Geral de Proteção de Dados Pessoais",
                "BR",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=[
            "valid_regulation",
            "different_jurisdiction",
            "different_jurisdiction_end_of_year",
        ],
    )
    def test_valid_regulation(
        self, regulation_id, name, description, jurisdiction, date, created_at
    ):

        regulation = Regulation(
            regulation_id=regulation_id,
            name=name,
            description=description,
            jurisdiction=jurisdiction,
            date=date,
            created_at=created_at,
        )

        assert regulation.regulation_id == regulation_id
        assert regulation.name == name
        assert regulation.description == description
        assert regulation.jurisdiction == jurisdiction
        assert regulation.date == date
        assert regulation.created_at == created_at

    @pytest.mark.parametrize(
        "regulation_id, name, description, jurisdiction, date, created_at, expected_error",
        [
            (
                123,
                "GDPR",
                "General Data Protection Regulation",
                "EU",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"regulation_id\n\s+Input should be a valid string",
            ),
            (
                "reg456",
                123,
                "General Data Protection Regulation",
                "EU",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"name\n\s+Input should be a valid string",
            ),
            (
                "reg123",
                "GDPR",
                123,
                "EU",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"description\n\s+Input should be a valid string",
            ),
            (
                "reg789",
                "GDPR",
                "General Data Protection Regulation",
                123,
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"jurisdiction\n\s+Input should be a valid string",
            ),
            (
                "reg456",
                "GDPR",
                "General Data Protection Regulation",
                "EU",
                "now",
                datetime.now(timezone.utc),
                r"date\n\s+Input should be a valid datetime or date",
            ),
            (
                "reg123",
                "GDPR",
                "General Data Protection Regulation",
                "EU",
                datetime.now(timezone.utc),
                "now",
                r"created_at\n\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_regulation_id",
            "invalid_name",
            "invalid_description",
            "invalid_jurisdiction",
            "invalid_date",
            "invalid_created_at",
        ],
    )
    def test_invalid_regulation(
        self,
        regulation_id,
        name,
        description,
        jurisdiction,
        date,
        created_at,
        expected_error,
    ):

        with pytest.raises(ValidationError, match=expected_error):
            Regulation(
                regulation_id=regulation_id,
                name=name,
                description=description,
                jurisdiction=jurisdiction,
                date=date,
                created_at=created_at,
            )

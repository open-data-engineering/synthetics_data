import pytest
from pydantic import ValidationError
from datetime import datetime, timezone

from models.audit import Audit


class TestAudit:
    @pytest.mark.parametrize(
        "audit_id, entity_id, status, findings, date, created_at",
        [
            (
                "audit123",
                "entity456",
                "passed",
                "No issues found.",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
            ),
            (
                "audit789",
                "entity012",
                "failed",
                "Critical issues found.",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "audit456",
                "entity789",
                "pending",
                "",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_audit", "failed_status", "empty_findings"],
    )
    def test_valid_audit(self, audit_id, entity_id, status, findings, date, created_at):

        audit = Audit(
            audit_id=audit_id,
            entity_id=entity_id,
            status=status,
            findings=findings,
            date=date,
            created_at=created_at,
        )

        assert audit.audit_id == audit_id
        assert audit.entity_id == entity_id
        assert audit.status == status
        assert audit.findings == findings
        assert audit.date == date
        assert audit.created_at == created_at

    @pytest.mark.parametrize(
        "audit_id, entity_id, status, findings, date, created_at, expected_error",
        [
            (
                123,
                "entity456",
                "passed",
                "No issues found.",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"audit_id\n\s+Input should be a valid string",
            ),
            (
                "audit789",
                456,
                "passed",
                "No issues found.",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"entity_id\n\s+Input should be a valid string",
            ),
            (
                "audit123",
                "entity012",
                123,
                "No issues found.",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"status\n\s+Input should be a valid string",
            ),
            (
                "audit456",
                "entity789",
                "passed",
                123,
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"findings\n\s+Input should be a valid string",
            ),
            (
                "audit789",
                "entity456",
                "passed",
                "No issues found.",
                "now",
                datetime.now(timezone.utc),
                r"date\n\s+Input should be a valid datetime or date",
            ),
            (
                "audit123",
                "entity012",
                "passed",
                "No issues found.",
                datetime.now(timezone.utc),
                "now",
                r"created_at\n\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_audit_id",
            "invalid_entity_id",
            "invalid_status",
            "invalid_findings",
            "invalid_date",
            "invalid_created_at",
        ],
    )
    def test_invalid_audit(
        self, audit_id, entity_id, status, findings, date, created_at, expected_error
    ):
        with pytest.raises(ValidationError, match=expected_error):
            Audit(
                audit_id=audit_id,
                entity_id=entity_id,
                status=status,
                findings=findings,
                date=date,
                created_at=created_at,
            )

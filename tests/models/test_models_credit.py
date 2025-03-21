import pytest
from pydantic import ValidationError
from datetime import datetime, timezone

from models.credit import CreditScore, RiskAssessment


class TestCreditScore:
    @pytest.mark.parametrize(
        "score_id, user_id, score, last_updated, created_at",
        [
            (
                "score123",
                "user456",
                750,
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
            ),
            (
                "score789",
                "user012",
                300,
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "score456",
                "user789",
                850,
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_credit_score", "low_score", "high_score"],
    )
    def test_valid_credit_score(
        self, score_id, user_id, score, last_updated, created_at
    ):

        credit_score = CreditScore(
            score_id=score_id,
            user_id=user_id,
            score=score,
            last_updated=last_updated,
            created_at=created_at,
        )

        assert credit_score.score_id == score_id
        assert credit_score.user_id == user_id
        assert credit_score.score == score
        assert credit_score.last_updated == last_updated
        assert credit_score.created_at == created_at

    @pytest.mark.parametrize(
        "score_id, user_id, score, last_updated, created_at, expected_error",
        [
            (
                123,
                "user456",
                750,
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"score_id\s+Input should be a valid string",
            ),
            (
                "score789",
                456,
                750,
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"user_id\s+Input should be a valid string",
            ),
            (
                "score123",
                "user012",
                "750",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"score\s+Input should be a valid integer",
            ),
            (
                "score456",
                "user789",
                750,
                "now",
                datetime.now(timezone.utc),
                r"last_updated\s+Input should be a valid datetime or date",
            ),
            (
                "score789",
                "user456",
                750,
                datetime.now(timezone.utc),
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_score_id",
            "invalid_user_id",
            "invalid_score",
            "invalid_last_updated",
            "invalid_created_at",
        ],
    )
    def test_invalid_credit_score(
        self, score_id, user_id, score, last_updated, created_at, expected_error
    ):

        with pytest.raises(ValidationError, match=expected_error):
            CreditScore(
                score_id=score_id,
                user_id=user_id,
                score=score,
                last_updated=last_updated,
                created_at=created_at,
            )


class TestRiskAssessment:
    @pytest.mark.parametrize(
        "assessment_id, user_id, risk_level, details, date, created_at",
        [
            (
                "assess123",
                "user456",
                "low",
                "No significant risks identified.",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
            ),
            (
                "assess789",
                "user012",
                "high",
                "Multiple red flags raised.",
                datetime(2024, 1, 1, tzinfo=timezone.utc),
                datetime(2024, 1, 1, tzinfo=timezone.utc),
            ),
            (
                "assess456",
                "user789",
                "medium",
                "",
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
            ),
        ],
        ids=["valid_risk_assessment", "high_risk", "empty_details"],
    )
    def test_valid_risk_assessment(
        self, assessment_id, user_id, risk_level, details, date, created_at
    ):

        risk_assessment = RiskAssessment(
            assessment_id=assessment_id,
            user_id=user_id,
            risk_level=risk_level,
            details=details,
            date=date,
            created_at=created_at,
        )

        assert risk_assessment.assessment_id == assessment_id
        assert risk_assessment.user_id == user_id
        assert risk_assessment.risk_level == risk_level
        assert risk_assessment.details == details
        assert risk_assessment.date == date
        assert risk_assessment.created_at == created_at

    @pytest.mark.parametrize(
        "assessment_id, user_id, risk_level, details, date, created_at, expected_error",
        [
            (
                123,
                "user456",
                "low",
                "No significant risks identified.",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"assessment_id\s+Input should be a valid string",
            ),
            (
                "assess789",
                456,
                "low",
                "No significant risks identified.",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"user_id\s+Input should be a valid string",
            ),
            (
                "assess123",
                "user012",
                123,
                "No significant risks identified.",
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"risk_level\s+Input should be a valid string",
            ),
            (
                "assess456",
                "user789",
                "low",
                123,
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                r"details\s+Input should be a valid string",
            ),
            (
                "assess789",
                "user456",
                "low",
                "No significant risks identified.",
                "now",
                datetime.now(timezone.utc),
                r"date\s+Input should be a valid datetime or date",
            ),
            (
                "assess123",
                "user012",
                "low",
                "No significant risks identified.",
                datetime.now(timezone.utc),
                "now",
                r"created_at\s+Input should be a valid datetime or date",
            ),
        ],
        ids=[
            "invalid_assessment_id",
            "invalid_user_id",
            "invalid_risk_level",
            "invalid_details",
            "invalid_date",
            "invalid_created_at",
        ],
    )
    def test_invalid_risk_assessment(
        self,
        assessment_id,
        user_id,
        risk_level,
        details,
        date,
        created_at,
        expected_error,
    ):

        with pytest.raises(ValidationError, match=expected_error):
            RiskAssessment(
                assessment_id=assessment_id,
                user_id=user_id,
                risk_level=risk_level,
                details=details,
                date=date,
                created_at=created_at,
            )

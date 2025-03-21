import pytest
from uuid import UUID
import numpy as np
from src.commons.credit import CreditsEvents
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
def test_generate_credit_scores(count):
    """Tests the generate_credit_scores method with various counts."""

    scores = CreditsEvents.generate_credit_scores(count)

    assert len(scores) == count
    for score in scores:
        assert isinstance(UUID(score["score_id"]), UUID)
        assert isinstance(UUID(score["user_id"]), UUID)
        assert 300 <= score["score"] <= 850
        assert isinstance(score["last_updated"], object)
        assert isinstance(score["created_at"], object)


@pytest.mark.parametrize(
    "count",
    [
        (1),
        (5),
        (0),
    ],
)
def test_generate_risk_assessments(count):
    """Tests the generate_risk_assessments method with various counts."""

    assessments = CreditsEvents.generate_risk_assessments(count)

    assert len(assessments) == count
    for assessment in assessments:
        assert isinstance(UUID(assessment["assessment_id"]), UUID)
        assert isinstance(UUID(assessment["user_id"]), UUID)
        assert assessment["risk_level"] in ["low", "medium", "high"]
        assert isinstance(assessment["details"], str)
        assert isinstance(assessment["date"], object)
        assert isinstance(assessment["created_at"], object)

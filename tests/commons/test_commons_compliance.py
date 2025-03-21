import pytest
from uuid import UUID
import random
from src.commons.compliance import CompliancesEvents
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
def test_generate_regulations(count):
    """Tests the generate_regulations method with various counts."""

    regulations = CompliancesEvents.generate_regulations(count)

    assert len(regulations) == count
    for regulation in regulations:
        assert isinstance(UUID(regulation["regulation_id"]), UUID)
        assert isinstance(regulation["name"], str)
        assert isinstance(regulation["description"], str)
        assert isinstance(regulation["jurisdiction"], str)
        assert isinstance(regulation["date"], object)
        assert isinstance(regulation["created_at"], object)


@pytest.mark.parametrize(
    "count",
    [
        (1),
        (5),
        (0),
    ],
)
def test_generate_user_verifications(count):
    """Tests the generate_user_verifications method with various counts."""

    verifications = CompliancesEvents.generate_user_verifications(count)

    assert len(verifications) == count
    for verification in verifications:
        assert isinstance(UUID(verification["verification_id"]), UUID)
        assert isinstance(UUID(verification["user_id"]), UUID)
        assert verification["type"] in ["email", "phone", "identity"]
        assert verification["status"] in ["approved", "pending", "rejected"]
        assert isinstance(verification["date"], object)
        assert isinstance(verification["created_at"], object)

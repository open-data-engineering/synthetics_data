import pytest
from uuid import UUID
import numpy as np
from src.commons.audits import AuditsEvents
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
def test_generate_audits(count):
    """Tests the generate_audits method with various counts."""

    audits = AuditsEvents.generate_audits(count)

    assert len(audits) == count
    for audit in audits:
        assert isinstance(UUID(audit["audit_id"]), UUID)
        assert isinstance(UUID(audit["entity_id"]), UUID)
        assert audit["status"] in ["success", "failure"]
        assert audit["findings"] in ["no findings", "findings"]
        assert isinstance(audit["date"], object)
        assert isinstance(audit["created_at"], object)

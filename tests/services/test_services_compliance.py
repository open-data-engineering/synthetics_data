import pytest
from unittest.mock import patch
import logging

from services.compliance import ComplianceService

logger = logging.getLogger(__name__)


class TestComplianceService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_regulations", "zero_regulations", "many_regulations"],
    )
    @patch("services.compliance.CompliancesEvents")
    def test_insert_regulations(self, MockCompliancesEvents, count):
        MockCompliancesEvents.generate_regulations.return_value = [
            {"regulation_id": i} for i in range(count)
        ]

        regulations = ComplianceService.insert_regulations(count)

        assert len(regulations) == count
        MockCompliancesEvents.generate_regulations.assert_called_once_with(count)

    @patch("services.compliance.CompliancesEvents.generate_regulations")
    def test_insert_regulations_exception(self, mock_generate_regulations, caplog):
        mock_generate_regulations.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            regulations = ComplianceService.insert_regulations(5)

        assert regulations == []
        assert "Erro ao inserir regulamentações" in caplog.text

    @pytest.mark.parametrize(
        "count",
        [
            (3),
            (0),
            (50),
        ],
        ids=[
            "few_user_verifications",
            "zero_user_verifications",
            "many_user_verifications",
        ],
    )
    @patch("services.compliance.CompliancesEvents")
    def test_insert_user_verification(self, MockCompliancesEvents, count):
        MockCompliancesEvents.generate_user_verifications.return_value = [
            {"verification_id": i} for i in range(count)
        ]

        user_verifications = ComplianceService.insert_user_verification(count)

        assert len(user_verifications) == count
        MockCompliancesEvents.generate_user_verifications.assert_called_once_with(count)

    @patch("services.compliance.CompliancesEvents.generate_user_verifications")
    def test_insert_user_verification_exception(
        self, mock_generate_user_verifications, caplog
    ):
        mock_generate_user_verifications.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            user_verifications = ComplianceService.insert_user_verification(5)

        assert user_verifications == []
        assert "Erro ao inserir verificações de usuário" in caplog.text

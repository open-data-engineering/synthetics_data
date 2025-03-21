import pytest
from unittest.mock import patch
import logging

from services.audit import AuditService

logger = logging.getLogger(__name__)


class TestAuditService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_audits", "zero_audits", "many_audits"],
    )
    @patch("src.services.audit.AuditsEvents")
    def test_insert_audits(self, MockAuditsEvents, count):
        MockAuditsEvents.generate_audits.return_value = [
            {"audit_id": i} for i in range(count)
        ]

        audits = AuditService.insert_audits(count)

        assert len(audits) == count
        MockAuditsEvents.generate_audits.assert_called_once_with(count)

    @patch("src.services.audit.AuditsEvents.generate_audits")
    def test_insert_audits_exception(self, mock_generate_audits, caplog):
        mock_generate_audits.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            audits = AuditService.insert_audits(5)

        assert audits == []
        assert "Erro ao inserir auditorias" in caplog.text

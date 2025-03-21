import pytest
from unittest.mock import patch
import logging

from services.credit import CreditService

logger = logging.getLogger(__name__)


class TestCreditService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_credit_scores", "zero_credit_scores", "many_credit_scores"],
    )
    @patch("src.services.credit.CreditsEvents")
    def test_insert_credit_scores(self, MockCreditsEvents, count):
        MockCreditsEvents.generate_credit_scores.return_value = [
            {"score_id": i} for i in range(count)
        ]

        credit_scores = CreditService.insert_credit_scores(count)

        assert len(credit_scores) == count
        MockCreditsEvents.generate_credit_scores.assert_called_once_with(count)

    @patch("src.services.credit.CreditsEvents.generate_credit_scores")
    def test_insert_credit_scores_exception(self, mock_generate_credit_scores, caplog):
        mock_generate_credit_scores.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            credit_scores = CreditService.insert_credit_scores(5)

        assert credit_scores == []
        assert "Erro ao inserir pontuações de crédito" in caplog.text

    @pytest.mark.parametrize(
        "count",
        [
            (3),
            (0),
            (50),
        ],
        ids=["few_risk_assessments", "zero_risk_assessments", "many_risk_assessments"],
    )
    @patch("src.services.credit.CreditsEvents")
    def test_insert_risk_assessments(self, MockCreditsEvents, count):
        MockCreditsEvents.generate_risk_assessments.return_value = [
            {"assessment_id": i} for i in range(count)
        ]

        risk_assessments = CreditService.insert_risk_assessments(count)

        assert len(risk_assessments) == count
        MockCreditsEvents.generate_risk_assessments.assert_called_once_with(count)

    @patch("src.services.credit.CreditsEvents.generate_risk_assessments")
    def test_insert_risk_assessments_exception(
        self, mock_generate_risk_assessments, caplog
    ):
        mock_generate_risk_assessments.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            risk_assessments = CreditService.insert_risk_assessments(5)

        assert risk_assessments == []
        assert "Erro ao inserir avaliações de risco" in caplog.text

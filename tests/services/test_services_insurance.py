import pytest
from unittest.mock import patch
import logging

from src.services.insurance import InsuranceService

logger = logging.getLogger(__name__)


class TestInsuranceService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_policies", "zero_policies", "many_policies"],
    )
    @patch("src.services.insurance.InsuranceEvents")
    def test_insert_policies(self, MockInsuranceEvents, count):
        MockInsuranceEvents.generate_policies.return_value = [
            {"policy_id": i} for i in range(count)
        ]

        policies = InsuranceService.insert_policies(count)

        assert len(policies) == count
        MockInsuranceEvents.generate_policies.assert_called_once_with(count)

    @patch("src.services.insurance.InsuranceEvents.generate_policies")
    def test_insert_policies_exception(self, mock_generate_policies, caplog):
        mock_generate_policies.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            policies = InsuranceService.insert_policies(5)

        assert policies == []
        assert "Erro ao inserir apólices" in caplog.text

    @pytest.mark.parametrize(
        "count",
        [
            (3),
            (0),
            (50),
        ],
        ids=["few_claims", "zero_claims", "many_claims"],
    )
    @patch("src.services.insurance.InsuranceEvents")
    def test_insert_claims(self, MockInsuranceEvents, count):
        MockInsuranceEvents.generate_claims.return_value = [
            {"claim_id": i} for i in range(count)
        ]

        claims = InsuranceService.insert_claims(count)

        assert len(claims) == count
        MockInsuranceEvents.generate_claims.assert_called_once_with(count)

    @patch("src.services.insurance.InsuranceEvents.generate_claims")
    def test_insert_claims_exception(self, mock_generate_claims, caplog):
        mock_generate_claims.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            claims = InsuranceService.insert_claims(5)

        assert claims == []
        assert "Erro ao inserir reivindicações" in caplog.text

    @pytest.mark.parametrize(
        "count",
        [
            (2),
            (0),
            (25),
        ],
        ids=["few_insured_entities", "zero_insured_entities", "many_insured_entities"],
    )
    @patch("src.services.insurance.InsuranceEvents")
    def test_insert_insured_entities(self, MockInsuranceEvents, count):
        MockInsuranceEvents.generate_insured_entities.return_value = [
            {"entity_id": i} for i in range(count)
        ]

        insured_entities = InsuranceService.insert_insured_entities(count)

        assert len(insured_entities) == count
        MockInsuranceEvents.generate_insured_entities.assert_called_once_with(count)

    @patch("src.services.insurance.InsuranceEvents.generate_insured_entities")
    def test_insert_insured_entities_exception(
        self, mock_generate_insured_entities, caplog
    ):
        mock_generate_insured_entities.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            insured_entities = InsuranceService.insert_insured_entities(5)

        assert insured_entities == []
        assert "Erro ao inserir entidades seguradas" in caplog.text

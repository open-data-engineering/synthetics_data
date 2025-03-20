import logging
from src.models.insurance import Policy, Claim, InsuredEntity
from src.commons.insurance import InsuranceEvents

logger = logging.getLogger(__name__)


class InsuranceService:
    @staticmethod
    def insert_policies(count: int):
        """Insere apólices de seguro no banco de dados."""
        try:
            policies_dicts = InsuranceEvents.generate_policies(count)
            return [Policy(**policy_dict) for policy_dict in policies_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir apólices: {e}")
            return []


    @staticmethod
    def insert_claims(count: int):
        """Insere reivindicações de seguro no banco de dados."""
        try:
            claims_dicts = InsuranceEvents.generate_claims(count)
            return [Claim(**claim_dict) for claim_dict in claims_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir reivindicações: {e}")
            return []


    @staticmethod
    def insert_insured_entities(count: int):
        """Insere entidades seguradas no banco de dados."""
        try:
            entities_dicts = InsuranceEvents.generate_insured_entities(count)
            return [InsuredEntity(**entity_dict) for entity_dict in entities_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir entidades seguradas: {e}")
            return []

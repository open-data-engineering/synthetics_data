import logging
from src.models.insurance import Policy, Claim, InsuredEntity
from src.commons.insurance import InsuranceEvents

logger = logging.getLogger(__name__)


class InsuranceService:
    @staticmethod
    def insert_policies(count: int):
        """Insere apólices de seguro no banco de dados."""
        try:
            return InsuranceEvents.generate_policies(count)
        except Exception as e:
            logger.error(f"Erro ao inserir apólices: {e}")
            return []

    @staticmethod
    def insert_claims(count: int):
        """Insere reivindicações de seguro no banco de dados."""
        try:
            return InsuranceEvents.generate_claims(count)
        except Exception as e:
            logger.error(f"Erro ao inserir reivindicações: {e}")
            return []

    @staticmethod
    def insert_insured_entities(count: int):
        """Insere entidades seguradas no banco de dados."""
        try:
            return InsuranceEvents.generate_insured_entities(count)
        except Exception as e:
            logger.error(f"Erro ao inserir entidades seguradas: {e}")
            return []

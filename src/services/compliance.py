import logging
from src.models.compliance import Regulation, UserVerification
from src.commons.compliance import CompliancesEvents

logger = logging.getLogger(__name__)


class ComplianceService:
    @staticmethod
    def insert_regulations(count: int):
        """Insere regulamentações no banco de dados."""
        try:
            regulations_dicts = CompliancesEvents.generate_regulations(count)
            return [Regulation(**reg_dict) for reg_dict in regulations_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir regulamentações: {e}")
            return []


    @staticmethod
    def insert_user_verification(count: int):
        """Insere verificações de usuário no banco de dados."""
        try:
            verifications_dicts = CompliancesEvents.generate_user_verifications(count)
            return [UserVerification(**ver_dict) for ver_dict in verifications_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir verificações de usuário: {e}")
            return []

import logging
from src.models.credit import CreditScore, RiskAssessment
from src.commons.credit import CreditsEvents

logger = logging.getLogger(__name__)


class CreditService:
    @staticmethod
    def insert_credit_scores(count: int):
        """Insere pontuações de crédito no banco de dados."""
        try:
            return CreditsEvents.generate_credit_scores(count)
        except Exception as e:
            logger.error(f"Erro ao inserir pontuações de crédito: {e}")
            return []

    @staticmethod
    def insert_risk_assessments(count: int):
        """Insere avaliações de risco no banco de dados."""
        try:
            return CreditsEvents.generate_risk_assessments(count)
        except Exception as e:
            logger.error(f"Erro ao inserir avaliações de risco: {e}")
            return []

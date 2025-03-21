import logging
from commons.credit import CreditsEvents

logger = logging.getLogger(__name__)


class CreditService:
    """Provides services for managing credit data.

    This class offers methods for inserting credit scores and risk assessments,
    handling potential errors during data generation.
    """

    @staticmethod
    def insert_credit_scores(count: int) -> list:
        """Inserts credit score data.

        Generates and returns a list of credit score data dictionaries. Logs an error
        and returns an empty list if data generation fails.
        """
        try:
            return CreditsEvents.generate_credit_scores(count)
        except Exception as e:
            logger.error(f"Erro ao inserir pontuações de crédito: {e}")
            return []

    @staticmethod
    def insert_risk_assessments(count: int) -> list:
        """Inserts risk assessment data.

        Generates and returns a list of risk assessment data dictionaries. Logs an
        error and returns an empty list if data generation fails.
        """
        try:
            return CreditsEvents.generate_risk_assessments(count)
        except Exception as e:
            logger.error(f"Erro ao inserir avaliações de risco: {e}")
            return []

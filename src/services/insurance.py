import logging
from commons.insurance import InsuranceEvents

logger = logging.getLogger(__name__)


class InsuranceService:
    """Provides services for managing insurance data.

    This class offers methods for inserting insurance policies, claims, and
    insured entities, handling potential errors during data generation.
    """

    @staticmethod
    def insert_policies(count: int) -> list:
        """Inserts insurance policy data.

        Generates and returns a list of insurance policy data dictionaries. Logs an
        error and returns an empty list if data generation fails.
        """
        try:
            return InsuranceEvents.generate_policies(count)
        except Exception as e:
            logger.error(f"Erro ao inserir apólices: {e}")
            return []

    @staticmethod
    def insert_claims(count: int) -> list:
        """Inserts insurance claim data.

        Generates and returns a list of insurance claim data dictionaries. Logs an error
        and returns an empty list if data generation fails.
        """
        try:
            return InsuranceEvents.generate_claims(count)
        except Exception as e:
            logger.error(f"Erro ao inserir reivindicações: {e}")
            return []

    @staticmethod
    def insert_insured_entities(count: int) -> list:
        """Inserts insured entity data.

        Generates and returns a list of insured entity data dictionaries. Logs an error
        and returns an empty list if data generation fails.
        """
        try:
            return InsuranceEvents.generate_insured_entities(count)
        except Exception as e:
            logger.error(f"Erro ao inserir entidades seguradas: {e}")
            return []

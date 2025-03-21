import logging
from src.commons.compliance import CompliancesEvents

logger = logging.getLogger(__name__)


class ComplianceService:
    """Provides services for managing compliance data.

    This class offers methods for inserting regulations and user verifications,
    handling potential errors during data generation.
    """

    @staticmethod
    def insert_regulations(count: int) -> list:
        """Inserts regulation data.

        Generates and returns a list of regulation data dictionaries. Logs an error and
        returns an empty list if data generation fails.
        """
        try:
            return CompliancesEvents.generate_regulations(count)
        except Exception as e:
            logger.error(f"Erro ao inserir regulamentações: {e}")
            return []

    @staticmethod
    def insert_user_verification(count: int) -> list:
        """Inserts user verification data.

        Generates and returns a list of user verification data dictionaries. Logs an
        error and returns an empty list if data generation fails.
        """
        try:
            return CompliancesEvents.generate_user_verifications(count)
        except Exception as e:
            logger.error(f"Erro ao inserir verificações de usuário: {e}")
            return []

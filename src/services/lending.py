import logging
from typing import Any, Dict, List
from commons.lending import LendingEvents

logger = logging.getLogger(__name__)


class LoanService:
    """Provides services for managing loan data.

    This class offers methods for inserting loan and payment records,
    handling potential errors during data generation.
    """

    @staticmethod
    def insert_loans(count: int) -> List[Dict[str, Any]]:
        """Inserts loan data.

        Generates and returns a list of loan data dictionaries. Logs an error and
        returns an empty list if data generation fails.
        """
        try:
            return LendingEvents.generate_loans(count)
        except Exception as e:
            logger.error(f"Erro ao inserir empréstimos: {e}")
            return []

    @staticmethod
    def insert_payments(count: int) -> List[Dict[str, Any]]:
        """Inserts payment data.

        Generates and returns a list of payment data dictionaries. Logs an error and
        returns an empty list if data generation fails.
        """
        try:
            return LendingEvents.generate_payments(count)
        except Exception as e:
            logger.error(f"Erro ao inserir pagamentos: {e}")
            return []

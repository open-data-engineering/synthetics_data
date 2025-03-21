import logging
from typing import Any, Dict, List
from commons.payments import PaymentsEvents

logger = logging.getLogger(__name__)


class TransactionService:
    """Provides services for managing payment data.

    This class offers methods for inserting transactions, payment methods,
    and merchants, handling potential errors during data generation.
    """

    @staticmethod
    def insert_transactions(count: int) -> List[Dict[str, Any]]:
        """Inserts transaction data.

        Generates and returns a list of transaction data dictionaries. Logs an error
        and returns an empty list if data generation fails.
        """
        try:
            return PaymentsEvents.generate_transactions(count)
        except Exception as e:
            logger.error(f"Erro ao inserir transações: {e}")
            return []

    @staticmethod
    def insert_payment_methods(count: int) -> List[Dict[str, Any]]:
        """Inserts payment method data.

        Generates and returns a list of payment method data dictionaries. Logs an error
        and returns an empty list if data generation fails.
        """
        try:
            return PaymentsEvents.generate_payment_methods(count)
        except Exception as e:
            logger.error(f"Erro ao inserir métodos de pagamento: {e}")
            return []

    @staticmethod
    def insert_merchants(count: int) -> List[Dict[str, Any]]:
        """Inserts merchant data.

        Generates and returns a list of merchant data dictionaries. Logs an error and
        returns an empty list if data generation fails.
        """
        try:
            return PaymentsEvents.generate_merchants(count)
        except Exception as e:
            logger.error(f"Erro ao inserir comerciantes: {e}")
            return []

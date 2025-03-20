import logging
from src.models.payment import Transaction, PaymentMethod, Merchant
from src.commons.payments import PaymentsEvents

logger = logging.getLogger(__name__)


class TransactionService:
    @staticmethod
    def insert_transactions(count: int):
        """Insere transações no banco de dados."""
        try:
            return PaymentsEvents.generate_transactions(count)
        except Exception as e:
            logger.error(f"Erro ao inserir transações: {e}")
            return []

    @staticmethod
    def insert_payment_methods(count: int):
        """Insere métodos de pagamento no banco de dados."""
        try:
            return PaymentsEvents.generate_payment_methods(count)
        except Exception as e:
            logger.error(f"Erro ao inserir métodos de pagamento: {e}")
            return []

    @staticmethod
    def insert_merchants(count: int):
        """Insere comerciantes no banco de dados."""
        try:
            return PaymentsEvents.generate_merchants(count)
        except Exception as e:
            logger.error(f"Erro ao inserir comerciantes: {e}")
            return []

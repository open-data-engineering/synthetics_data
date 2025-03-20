import logging
from src.models.payment import Transaction, PaymentMethod, Merchant
from src.commons.payments import PaymentsEvents

logger = logging.getLogger(__name__)


class TransactionService:
    @staticmethod
    def insert_transactions(count: int):
        """Insere transações no banco de dados."""
        try:
            transactions_dicts = PaymentsEvents.generate_transactions(count)
            return [Transaction(**txn_dict) for txn_dict in transactions_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir transações: {e}")
            return []


    @staticmethod
    def insert_payment_methods(count: int):
        """Insere métodos de pagamento no banco de dados."""
        try:
            payment_methods_dicts = PaymentsEvents.generate_payment_methods(count)
            return [PaymentMethod(**pm_dict) for pm_dict in payment_methods_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir métodos de pagamento: {e}")
            return []


    @staticmethod
    def insert_merchants(count: int):
        """Insere comerciantes no banco de dados."""
        try:
            merchants_dicts = PaymentsEvents.generate_merchants(count)
            return [Merchant(**merchant_dict) for merchant_dict in merchants_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir comerciantes: {e}")
            return []

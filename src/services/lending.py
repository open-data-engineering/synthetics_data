import logging
from src.models.lending import Loan, Payment
from src.commons.lending import LendingEvents

logger = logging.getLogger(__name__)


class LoanService:
    @staticmethod
    def insert_loans(count: int):
        """Insere empréstimos no banco de dados."""
        try:
            loans_dicts = LendingEvents.generate_loans(count)
            return [Loan(**loan_dict) for loan_dict in loans_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir empréstimos: {e}")
            return []


    @staticmethod
    def insert_payments(count: int):
        """Insere pagamentos no banco de dados."""
        try:
            payments_dicts = LendingEvents.generate_payments(count)
            return [Payment(**payment_dict) for payment_dict in payments_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir pagamentos: {e}")
            return []

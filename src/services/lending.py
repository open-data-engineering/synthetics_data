import logging
from src.models.lending import Loan, Payment
from src.commons.lending import LendingEvents

logger = logging.getLogger(__name__)


class LoanService:
    @staticmethod
    def insert_loans(count: int):
        """Insere empréstimos no banco de dados."""
        try:
            return LendingEvents.generate_loans(count)
        except Exception as e:
            logger.error(f"Erro ao inserir empréstimos: {e}")
            return []

    @staticmethod
    def insert_payments(count: int):
        """Insere pagamentos no banco de dados."""
        try:
            return LendingEvents.generate_payments(count)
        except Exception as e:
            logger.error(f"Erro ao inserir pagamentos: {e}")
            return []

import logging
from src.models.investments import Portfolio
from src.commons.investments import InvestmentsEvents

logger = logging.getLogger(__name__)


class PortfolioService:
    @staticmethod
    def insert_portfolios(count: int):
        """Insere portfólios no banco de dados."""
        try:
            return InvestmentsEvents.generate_portfolios(count)
        except Exception as e:
            logger.error(f"Erro ao inserir portfólios: {e}")
            return []

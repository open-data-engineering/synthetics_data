import logging
from commons.investments import InvestmentsEvents

logger = logging.getLogger(__name__)


class PortfolioService:
    """Provides services for managing investment portfolios.

    This class offers a method for inserting portfolios, handling
    potential errors during data generation.
    """

    @staticmethod
    def insert_portfolios(count: int) -> list:
        """Inserts portfolio data.

        Generates and returns a list of investment portfolio data dictionaries.
        Logs an error and returns an empty list if data generation fails.
        """
        try:
            return InvestmentsEvents.generate_portfolios(count)
        except Exception as e:
            logger.error(f"Erro ao inserir portfólios: {e}")
            return []

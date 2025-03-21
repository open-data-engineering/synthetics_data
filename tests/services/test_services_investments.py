import pytest
from unittest.mock import patch
import logging

from src.services.investments import PortfolioService

logger = logging.getLogger(__name__)


class TestPortfolioService:
    @pytest.mark.parametrize(
        "count",
        [
            (5),
            (0),
            (100),
        ],
        ids=["few_portfolios", "zero_portfolios", "many_portfolios"],
    )
    @patch("src.services.investments.InvestmentsEvents")
    def test_insert_portfolios(self, MockInvestmentsEvents, count):
        MockInvestmentsEvents.generate_portfolios.return_value = [
            {"portfolio_id": i} for i in range(count)
        ]

        portfolios = PortfolioService.insert_portfolios(count)

        assert len(portfolios) == count
        MockInvestmentsEvents.generate_portfolios.assert_called_once_with(count)

    @patch("src.services.investments.InvestmentsEvents.generate_portfolios")
    def test_insert_portfolios_exception(self, mock_generate_portfolios, caplog):
        mock_generate_portfolios.side_effect = Exception("Test Exception")

        with caplog.at_level(logging.ERROR):
            portfolios = PortfolioService.insert_portfolios(5)

        assert portfolios == []
        assert "Erro ao inserir portfólios" in caplog.text

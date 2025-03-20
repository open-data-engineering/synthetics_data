import logging
from src.models.account import Account, Subaccount, User
from src.commons.accounts import AccountEvents

logger = logging.getLogger(__name__)


class AccountService:
    @staticmethod
    def insert_users(count):
        try:
            return AccountEvents.generate_users(count)
        except Exception as e:
            logger.error(f"Erro ao inserir usuários: {e}")
            return []

    @staticmethod
    def insert_accounts(count):
        """Insere contas no banco de dados."""
        try:
            return AccountEvents.generate_accounts(count)
        except Exception as e:
            logger.error(f"Erro ao inserir contas: {e}")
            return []

    @staticmethod
    def insert_subaccounts(count):
        """Insere subcontas no banco de dados."""
        try:
            return AccountEvents.generate_subaccounts(count)
        except Exception as e:
            logger.error(f"Erro ao inserir subcontas: {e}")
            return []

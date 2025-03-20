import logging
from src.models.account import Account, Subaccount, User
from src.commons.accounts import AccountEvents

logger = logging.getLogger(__name__)


class AccountService:
    @staticmethod
    def insert_users(count):
        try:
            users_dicts = AccountEvents.generate_users(count)
            return [User(**users_dict) for users_dict in users_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir usuários: {e}")
            return []

    @staticmethod
    def insert_accounts(count):
        """Insere contas no banco de dados."""
        try:
            account_dicts = AccountEvents.generate_accounts(count)
            return [Account(**account_dict) for account_dict in account_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir contas: {e}")
            return []

    @staticmethod
    def insert_subaccounts(count):
        """Insere subcontas no banco de dados."""
        try:
            subaccount_dicts = AccountEvents.generate_subaccounts(count)
            return [Subaccount(**subaccount_dict) for subaccount_dict in subaccount_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir subcontas: {e}")
            return []

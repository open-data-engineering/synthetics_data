import logging
from typing import Any, Dict, List
from commons.accounts import AccountEvents

logger = logging.getLogger(__name__)


class AccountService:
    """Provides services for managing accounts.

    This class offers methods for inserting users, accounts, and subaccounts,
    handling potential errors during data generation.
    """

    @staticmethod
    def insert_users(count: int) -> List[Dict[str, Any]]:
        """Inserts user data.

        Inserts and returns a list of user data dictionaries. Logs an error and
        returns an empty list if data generation fails.
        """
        try:
            return AccountEvents.generate_users(count)
        except Exception as e:
            logger.error(f"Erro ao inserir usuários: {e}")
            return []

    @staticmethod
    def insert_accounts(count: int) -> List[Dict[str, Any]]:
        """Inserts account data.

        Inserts and returns a list of account data dictionaries. Logs an error and
        returns an empty list if data generation fails.
        """
        try:
            return AccountEvents.generate_accounts(count)
        except Exception as e:
            logger.error(f"Erro ao inserir contas: {e}")
            return []

    @staticmethod
    def insert_subaccounts(count: int) -> List[Dict[str, Any]]:
        """Inserts subaccount data.

        Inserts and returns a list of subaccount data dictionaries. Logs an error
        and returns an empty list if data generation fails.
        """
        try:
            return AccountEvents.generate_subaccounts(count)
        except Exception as e:
            logger.error(f"Erro ao inserir subcontas: {e}")
            return []

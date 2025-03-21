import logging
from typing import Any, Dict, List
from commons.audits import AuditsEvents

logger = logging.getLogger(__name__)


class AuditService:
    """Provides services for managing audit records.

    This class offers a method for inserting audit records, handling
    potential errors during data generation.
    """

    @staticmethod
    def insert_audits(count: int) -> List[Dict[str, Any]]:
        """Inserts audit records.

        Generates and returns a list of audit data dictionaries. Logs an error and
        returns an empty list if data generation fails.
        """
        try:
            return AuditsEvents.generate_audits(count)
        except Exception as e:
            logger.error(f"Erro ao inserir auditorias: {e}")
            return []

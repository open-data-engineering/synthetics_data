import logging
from src.commons.entities import EntityEvents

logger = logging.getLogger(__name__)


class EntityService:
    """Provides services for managing entities.

    This class offers a method for inserting entities, handling potential
    errors during data generation.
    """

    @staticmethod
    def insert_entities(count: int) -> list:
        """Inserts entity data.

        Generates and returns a list of entity data dictionaries. Logs an error and
        returns an empty list if data generation fails.
        """
        try:
            return EntityEvents.generate_entities(count)
        except Exception as e:
            logger.error(f"Erro ao inserir entidades: {e}")
            return []

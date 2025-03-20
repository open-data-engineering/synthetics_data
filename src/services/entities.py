import logging
from src.models.entities import Entity
from src.commons.entities import EntityEvents

logger = logging.getLogger(__name__)


class EntityService:
    @staticmethod
    def insert_entities(count: int):
        """Insere entidades no banco de dados."""
        try:
            return EntityEvents.generate_entities(count)
        except Exception as e:
            logger.error(f"Erro ao inserir entidades: {e}")
            return []

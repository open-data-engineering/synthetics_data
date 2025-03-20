import logging
from src.models.entities import Entity
from src.commons.entities import EntityEvents

logger = logging.getLogger(__name__)


class EntityService:
    @staticmethod
    def insert_entities(count: int):
        """Insere entidades no banco de dados."""
        try:
            entities_dicts = EntityEvents.generate_entities(count)
            return [Entity(**entity_dict) for entity_dict in entities_dicts]
        except Exception as e:
            logger.error(f"Erro ao inserir entidades: {e}")
            return []

import logging
from src.models.audit import Audit
from src.commons.audits import AuditsEvents

logger = logging.getLogger(__name__)


class AuditService:
    @staticmethod
    def insert_audits(count: int):
        """Insere auditorias no banco de dados e retorna os objetos inseridos"""
        try:
            return AuditsEvents.generate_audits(count)
        except Exception as e:
            logger.error(f"Erro ao inserir auditorias: {e}")
            return []

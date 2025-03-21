from pydantic import BaseModel, StrictStr  # type: ignore
from datetime import datetime


class Entity(BaseModel):
    """Represents a generic entity.

    This model defines the basic attributes of an entity, including entity ID,
    name, and creation timestamp.
    """

    entity_id: StrictStr
    name: StrictStr
    created_at: datetime

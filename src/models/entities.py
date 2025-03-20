from pydantic import BaseModel  # type: ignore
from datetime import datetime


class Entity(BaseModel):
    entity_id: str
    name: str
    created_at: datetime

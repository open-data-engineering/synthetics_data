from pydantic import BaseModel  # type: ignore
from datetime import datetime


class Audit(BaseModel):
    audit_id: str
    entity_id: str
    status: str
    findings: str
    date: datetime
    created_at: datetime

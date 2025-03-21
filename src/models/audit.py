from pydantic import BaseModel, StrictStr
from datetime import datetime


class Audit(BaseModel):
    """Represents an audit record.

    This model defines the attributes of an audit, including audit ID, entity ID,
    status, findings, audit date, and creation timestamp.
    """

    audit_id: StrictStr
    entity_id: StrictStr
    status: StrictStr
    findings: StrictStr
    date: datetime
    created_at: datetime

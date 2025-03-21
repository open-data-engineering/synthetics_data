from pydantic import BaseModel, StrictStr  # type: ignore
from datetime import datetime


class Regulation(BaseModel):
    """Represents a regulation.

    This model defines the attributes of a regulation, including regulation ID, name,
    description, jurisdiction, effective date, and creation timestamp.
    """

    regulation_id: StrictStr
    name: StrictStr
    description: StrictStr
    jurisdiction: StrictStr
    date: datetime
    created_at: datetime


class UserVerification(BaseModel):
    """Represents a user verification record.

    This model defines the attributes of a user verification, including verification ID,
    user ID, verification type, status, verification date, and creation timestamp.
    """

    verification_id: StrictStr
    user_id: StrictStr
    type: StrictStr
    status: StrictStr
    date: datetime
    created_at: datetime

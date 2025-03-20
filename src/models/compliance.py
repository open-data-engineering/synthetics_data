from pydantic import BaseModel # type: ignore
from datetime import datetime


class Regulation(BaseModel):
    regulation_id: str
    name: str
    description: str
    jurisdiction: str
    date: datetime
    created_at: datetime


class UserVerification(BaseModel):
    verification_id: str
    user_id: str
    type: str
    status: str
    date: datetime
    created_at: datetime

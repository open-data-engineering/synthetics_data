from pydantic import BaseModel # type: ignore
from datetime import datetime


class Policy(BaseModel):
    policy_id: str
    type: str
    coverage_amount: int
    premium: int
    start_date: datetime
    end_date: datetime
    user_id: str
    created_at: datetime


class Claim(BaseModel):
    claim_id: str
    policy_id: str
    amount_claimed: int
    status: str
    filed_date: datetime
    created_at: datetime


class InsuredEntity(BaseModel):
    entity_id: str
    type: str
    description: str
    value: int
    created_at: datetime

from pydantic import BaseModel, StrictStr, StrictInt  # type: ignore
from datetime import datetime


class Policy(BaseModel):
    """Represents an insurance policy.

    This model defines the attributes of an insurance policy, including policy ID, type,
    coverage amount, premium, start and end dates, user ID, and creation timestamp.
    """

    policy_id: StrictStr
    type: StrictStr
    coverage_amount: int
    premium: StrictInt
    start_date: datetime
    end_date: datetime
    user_id: StrictStr
    created_at: datetime


class Claim(BaseModel):
    """Represents an insurance claim.

    This model defines the attributes of an insurance claim, including claim ID,
    policy ID, amount claimed, status, filed date, and creation timestamp.
    """

    claim_id: StrictStr
    policy_id: StrictStr
    amount_claimed: StrictInt
    status: StrictStr
    filed_date: datetime
    created_at: datetime


class InsuredEntity(BaseModel):
    """Represents an insured entity.

    This model defines the attributes of an insured entity, including entity ID,
    type, description, value, and creation timestamp.
    """

    entity_id: StrictStr
    type: StrictStr
    description: StrictStr
    value: StrictInt
    created_at: datetime

from pydantic import BaseModel # type: ignore
from datetime import datetime


class Portfolio(BaseModel):
    portfolio_id: str
    user_id: str
    total_value: int
    risk_profile: str
    created_at: datetime

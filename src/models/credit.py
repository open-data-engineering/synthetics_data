from pydantic import BaseModel # type: ignore
from datetime import datetime


class CreditScore(BaseModel):
    score_id: str
    user_id: str
    score: int
    last_updated: datetime
    created_at: datetime


class RiskAssessment(BaseModel):
    assessment_id: str
    user_id: str
    risk_level: str
    details: str
    date: datetime
    created_at: datetime

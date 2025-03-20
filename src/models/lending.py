from pydantic import BaseModel # type: ignore
from datetime import datetime


class Loan(BaseModel):
    loan_id: str
    user_id: str
    amount: int
    interest_rate: float
    term: int
    created_at: datetime


class Payment(BaseModel):
    payment_id: str
    loan_id: str
    amount: int
    date: datetime
    status: str
    created_at: datetime

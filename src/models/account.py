from pydantic import BaseModel, EmailStr  # type: ignore
from datetime import datetime


class Account(BaseModel):
    account_id: str
    account_type: str
    balance: int
    currency: str
    status: str
    user_id: str
    created_at: datetime


class Subaccount(BaseModel):
    subaccount_id: str
    parent_account_id: str
    purpose: str
    balance: int
    created_at: datetime


class User(BaseModel):
    user_id: str
    name: str
    email: EmailStr
    phone: str
    created_at: datetime

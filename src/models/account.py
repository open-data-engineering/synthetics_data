from pydantic import BaseModel, EmailStr, StrictStr, StrictInt  # type: ignore
from datetime import datetime


class Account(BaseModel):
    """Represents a bank account.

    This model defines the attributes of a bank account, including account ID, type,
    balance, currency, status, associated user ID, and creation timestamp.
    """

    account_id: StrictStr
    account_type: StrictStr
    balance: StrictInt
    currency: StrictStr
    status: StrictStr
    user_id: StrictStr
    created_at: datetime


class Subaccount(BaseModel):
    """Represents a subaccount within a bank account.

    This model defines the attributes of a subaccount, including subaccount ID,
    parent account ID, purpose, balance, and creation timestamp.
    """

    subaccount_id: StrictStr
    parent_account_id: StrictStr
    purpose: StrictStr
    balance: StrictInt
    created_at: datetime


class User(BaseModel):
    """Represents a user.

    This model defines the attributes of a user, including user ID, name,
    email, phone number, and creation timestamp.
    """

    user_id: StrictStr
    name: StrictStr
    email: EmailStr
    phone: StrictStr
    created_at: datetime

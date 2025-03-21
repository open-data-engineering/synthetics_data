from pydantic import BaseModel, StrictStr, StrictInt, StrictFloat  # type: ignore
from datetime import datetime


class Loan(BaseModel):
    """Represents a loan.

    This model defines the attributes of a loan, including loan ID, user ID,
    amount, interest rate, term, and creation timestamp.
    """

    loan_id: StrictStr
    user_id: StrictStr
    amount: StrictInt
    interest_rate: StrictFloat
    term: StrictInt
    created_at: datetime


class Payment(BaseModel):
    """Represents a loan payment.

    This model defines the attributes of a loan payment, including payment ID,
    loan ID, amount, payment date, status, and creation timestamp.
    """

    payment_id: StrictStr
    loan_id: StrictStr
    amount: StrictInt
    date: datetime
    status: StrictStr
    created_at: datetime

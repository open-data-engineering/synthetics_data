from pydantic import BaseModel, StrictInt, StrictStr
from datetime import datetime


class Transaction(BaseModel):
    """Represents a financial transaction.

    This model defines the attributes of a transaction, including transaction ID, amount,
    currency, status, timestamp, sender ID, receiver ID, and creation timestamp.
    """

    transaction_id: StrictStr
    amount: StrictInt
    currency: StrictStr
    status: StrictStr
    timestamp: datetime
    sender_id: StrictStr
    receiver_id: StrictStr
    created_at: datetime


class PaymentMethod(BaseModel):
    """Represents a payment method.

    This model defines the attributes of a payment method, including method ID,
    type, details, user ID, and creation timestamp.
    """

    method_id: StrictStr
    type: StrictStr
    details: StrictStr
    user_id: StrictStr
    created_at: datetime


class Merchant(BaseModel):
    """Represents a merchant.

    This model defines the attributes of a merchant, including merchant ID, name,
    category, contact information, and creation timestamp.
    """

    merchant_id: StrictStr
    name: StrictStr
    category: StrictStr
    contact_info: StrictStr
    created_at: datetime

from pydantic import BaseModel, StrictInt, StrictStr  # type: ignore
from datetime import datetime


class Portfolio(BaseModel):
    """Represents an investment portfolio.

    This model defines the attributes of an investment portfolio, including portfolio ID,
    user ID, total value, risk profile, and creation timestamp.
    """

    portfolio_id: StrictStr
    user_id: StrictStr
    total_value: StrictInt
    risk_profile: StrictStr
    created_at: datetime

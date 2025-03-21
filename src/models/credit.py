from pydantic import BaseModel, StrictInt, StrictStr  # type: ignore
from datetime import datetime


class CreditScore(BaseModel):
    """Represents a credit score.

    This model defines the attributes of a credit score, including score ID, user ID,
    score value, last updated date, and creation timestamp.
    """

    score_id: StrictStr
    user_id: StrictStr
    score: StrictInt
    last_updated: datetime
    created_at: datetime


class RiskAssessment(BaseModel):
    """Represents a risk assessment.

    This model defines the attributes of a risk assessment, including assessment ID,
    user ID, risk level, details, assessment date, and creation timestamp.
    """

    assessment_id: StrictStr
    user_id: StrictStr
    risk_level: StrictStr
    details: StrictStr
    date: datetime
    created_at: datetime

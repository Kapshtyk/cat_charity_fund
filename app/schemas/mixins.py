from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DonationAndCharityProjectCommonFields(BaseModel):
    id: int
    fully_invested: Optional[bool] = Field(default=False)
    invested_amount: Optional[int] = Field(default=0, ge=0)
    create_date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    close_date: Optional[datetime]

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

from app.schemas.mixins import DonationAndCharityProjectCommonFields


class DonationCreate(BaseModel):
    comment: Optional[str]
    full_amount: PositiveInt = Field(None, example=1)


class DonationDbCommonUser(DonationCreate):
    id: int
    create_date: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True


class DonationDbSuperuser(
    DonationAndCharityProjectCommonFields, DonationDbCommonUser
):
    user_id: int

    class Config:
        orm_mode = True

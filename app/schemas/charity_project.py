from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt, ValidationError, validator

from app.schemas.mixins import DonationAndCharityProjectCommonFields


class CharityProjectCreate(BaseModel):
    name: str = Field(None, min_length=1, max_length=100)
    description: str = Field(None, min_length=1)
    full_amount: PositiveInt = Field(None, example=1)

    @validator("name")
    def validate_name(cls, value):
        print(value)
        if not value or len(value) > 100:
            return ValidationError(
                "Имя проекта не может быть пустым и не может быть длиннее 100 символов!"
            )
        return value

    @validator("description")
    def validate_description(cls, value):
        if not value:
            return ValidationError("Описание проекта не может быть пустым!")
        return value

    @validator("full_amount")
    def validate_full_amount(cls, value):
        if not value or value < 0:
            return ValidationError(
                "Сумма не может быть пустой и не может быть меньше 0!"
            )
        return value


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt] = Field(None)

    class Config:
        extra = Extra.forbid

    @validator("name")
    def validate_name(cls, value):
        if not value or len(value) > 100:
            return ValidationError(
                "Имя проекта не может быть пустым и не может быть длиннее 100 символов!"
            )
        return value

    @validator("description")
    def validate_description(cls, value):
        if not value:
            return ValidationError("Описание проекта не может быть пустым!")
        return value


class CharityProjectDb(DonationAndCharityProjectCommonFields, CharityProjectCreate):
    class Config:
        orm_mode = True

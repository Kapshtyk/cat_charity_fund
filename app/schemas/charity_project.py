from typing import Optional

from pydantic import (
    BaseModel,
    Extra,
    Field,
    PositiveInt,
    ValidationError,
    validator,
)

from app.core.constants import (
    CHARITY_PROJECT_DESCRIPTION_MIN_LENGTH,
    CHARITY_PROJECT_NAME_MAX_LENGTH,
    CHARITY_PROJECT_NAME_MIN_LENGTH,
)
from app.schemas.mixins import DonationAndCharityProjectCommonFields


class CharityProjectCreate(BaseModel):
    name: str = Field(
        None,
        min_length=CHARITY_PROJECT_NAME_MIN_LENGTH,
        max_length=CHARITY_PROJECT_NAME_MAX_LENGTH,
    )
    description: str = Field(
        None, min_length=CHARITY_PROJECT_DESCRIPTION_MIN_LENGTH
    )
    full_amount: PositiveInt = Field(None, example=1)

    @validator("name")
    def validate_name(cls, value):
        if not value or len(value) > CHARITY_PROJECT_NAME_MAX_LENGTH:
            return ValidationError(
                f"""Имя проекта не может быть пустым и не может быть длиннее {CHARITY_PROJECT_NAME_MAX_LENGTH} символов!"""  # noqa E501
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
    name: Optional[str] = Field(
        None,
        min_length=CHARITY_PROJECT_NAME_MIN_LENGTH,
        max_length=CHARITY_PROJECT_NAME_MAX_LENGTH,
    )
    description: Optional[str] = Field(
        None, min_length=CHARITY_PROJECT_DESCRIPTION_MIN_LENGTH
    )
    full_amount: Optional[PositiveInt] = Field(None)

    class Config:
        extra = Extra.forbid

    @validator("name")
    def validate_name(cls, value):
        if not value or len(value) > CHARITY_PROJECT_NAME_MAX_LENGTH:
            return ValidationError(
                f"""Имя проекта не может быть пустым и не может быть длиннее {CHARITY_PROJECT_NAME_MAX_LENGTH} символов!"""  # noqa E501
            )
        return value

    @validator("description")
    def validate_description(cls, value):
        if not value:
            return ValidationError("Описание проекта не может быть пустым!")
        return value


class CharityProjectDb(
    DonationAndCharityProjectCommonFields, CharityProjectCreate
):
    class Config:
        orm_mode = True

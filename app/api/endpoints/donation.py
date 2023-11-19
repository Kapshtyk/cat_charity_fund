from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.models import User
from app.schemas.donation import (
    DonationCreate,
    DonationDbCommonUser,
    DonationDbSuperuser,
)
from app.schemas.errors import Error

router = APIRouter()

from app.services.donation_service import DonationService


@router.post(
    "/",
    response_model=Union[DonationDbCommonUser, Error],
    response_model_exclude_none=True,
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    service = DonationService(session=session)
    return await service.create_donation(donation, user)


@router.get(
    "/",
    response_model=list[DonationDbSuperuser],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    service = DonationService(session=session)
    return await service.get_all_donations()


@router.get("/my", response_model=Union[list[DonationDbCommonUser], Error])
async def get_all_donations_of_user(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    service = DonationService(session=session)
    return await service.get_all_donations_of_user(user)

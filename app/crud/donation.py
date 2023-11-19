from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.donation import Donation
from app.models.user import User


class CRUDDonation(CRUDBase):
    async def check_available_funds(
        self,
        session: AsyncSession,
    ) -> list[Donation]:
        statement = select(Donation).where(Donation.fully_invested == False)
        donations = await session.execute(statement)
        return donations.scalars().all()

    async def get_all_donations_of_user(
        self,
        session: AsyncSession,
        user: User,
    ) -> list[Donation]:
        statement = select(Donation).where(Donation.user_id == user.id)
        donations = await session.execute(statement)
        return donations.scalars().all()


donation_crud = CRUDDonation(Donation)

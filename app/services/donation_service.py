from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import DonationCreate
from app.services.base_service import BaseService


class DonationService(BaseService):
    CRUD = donation_crud

    async def create_donation(
        self,
        donation: DonationCreate,
        user: User,
    ):
        donation = await super().create(donation, user=user)
        available_projects = await self.investing_service.check_charity_projects()
        if available_projects:
            donation = await self.investing_service.invest(donation, available_projects)
        return donation

    async def get_all_donations_of_user(self, user: User):
        return await self.CRUD.get_all_donations_of_user(
            session=self.session,
            user=user,
        )

    async def get_all_donations(self):
        return await super().get_multi()

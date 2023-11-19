from datetime import datetime
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models.charity_project import CharityProject
from app.models.donation import Donation


class InvestingService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def check_funds(self):
        result = await donation_crud.check_available_funds(self.session)
        return result

    async def check_charity_projects(self):
        result = await charity_project_crud.check_charity_projects(
            self.session
        )
        return result

    async def invest(
        self,
        obj: Union[CharityProject, Donation],
        obj_list: Union[list[Donation], list[CharityProject]],
    ):
        async def process(
            donation: Donation, charity_project: CharityProject, session
        ):
            required_amount = (
                charity_project.full_amount - charity_project.invested_amount
            )
            donation_amount = donation.full_amount - donation.invested_amount
            if donation_amount < required_amount:
                charity_project.invested_amount += donation_amount
                donation.invested_amount += donation_amount
                donation.fully_invested = True
                donation.close_date = datetime.now()

            elif donation_amount == required_amount:
                charity_project.invested_amount += donation_amount
                donation.invested_amount += donation_amount
                charity_project.fully_invested = True
                charity_project.close_date = datetime.now()
                donation.fully_invested = True
                donation.close_date = datetime.now()

            else:
                charity_project.invested_amount += required_amount
                donation.invested_amount += required_amount
                charity_project.fully_invested = True
                charity_project.close_date = datetime.now()
            self.session.add(charity_project)
            self.session.add(donation)

        if isinstance(obj, CharityProject):
            for donation in obj_list:
                await process(donation, obj, self.session)
        elif isinstance(obj, Donation):
            for charity_project in obj_list:
                await process(obj, charity_project, self.session)

        await self.session.commit()
        await self.session.refresh(obj)
        return obj

from datetime import datetime

from fastapi import HTTPException

from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import CharityProjectCreate
from app.services.base_service import BaseService


class CharityProjectService(BaseService):
    CRUD = charity_project_crud

    async def create_charity_project(
        self,
        charity_project: CharityProjectCreate,
    ):
        charity_project = await super().create(charity_project)
        available_funds = await self.investing_service.check_funds()
        if available_funds:
            charity_project = await self.investing_service.invest(
                charity_project,
                available_funds,
            )
        return charity_project

    async def get_all_charity_projects(self):
        charity_projects = await super().get_multi()
        return charity_projects

    async def delete_charity_project(self, charity_project_id: int):
        charity_project = await super().get(charity_project_id)
        if charity_project.invested_amount > 0:
            raise HTTPException(
                status_code=400,
                detail="В проект были внесены средства, не подлежит удалению!",
            )
        charity_project = await super().remove(charity_project)
        return charity_project

    async def update_charity_project(
        self, charity_project_id: int, updated_charity_project
    ):
        charity_project = await super().get(charity_project_id)
        if charity_project.close_date:
            raise HTTPException(
                status_code=400,
                detail="Закрытый проект нельзя редактировать!",
            )
        new_full_amount = updated_charity_project.full_amount
        if (
            new_full_amount
            and new_full_amount < charity_project.invested_amount
        ):
            raise HTTPException(
                status_code=400,
                detail="Количество средств не может быть меньше уже внесенных средств!",
            )
        if updated_charity_project.name:
            projects = await self.CRUD.get_project_by_name(
                updated_charity_project.name, self.session, charity_project.id
            )
            if projects is not None:
                raise HTTPException(
                    status_code=400,
                    detail="Проект с таким именем уже существует!",
                )
        charity_project = await super().update(
            charity_project, updated_charity_project
        )
        if charity_project.invested_amount == charity_project.full_amount:
            charity_project.close_date = datetime.now()
            charity_project.fully_invested = True
            self.session.commit()

        return charity_project

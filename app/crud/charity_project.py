from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    async def check_charity_projects(
        self,
        session: AsyncSession,
    ) -> list[CharityProject]:
        statement = select(CharityProject).where(
            CharityProject.fully_invested == 0
        )
        charity_projects = await session.execute(statement)
        return charity_projects.scalars().all()

    async def get_project_by_name(
        self,
        name: str,
        session: AsyncSession,
        project_id: Optional[int] = None,
    ) -> int:
        statement = select(CharityProject.id).where(
            CharityProject.name == name
        )
        if project_id:
            statement = statement.where(CharityProject.id != project_id)
        project = await session.execute(statement)
        return project.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)

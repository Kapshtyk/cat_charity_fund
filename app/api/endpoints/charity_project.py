from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_name_duplicate
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDb,
    CharityProjectUpdate,
)
from app.schemas.errors import Error
from app.services.charity_project_service import CharityProjectService

router = APIRouter()


@router.post(
    "/",
    response_model=Union[CharityProjectDb, Error],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(charity_project.name, session)
    service = CharityProjectService(session=session)
    return await service.create_charity_project(charity_project)


@router.get(
    "/",
    response_model=list[CharityProjectDb],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    service = CharityProjectService(session=session)
    return await service.get_all_charity_projects()


@router.delete(
    "/{charity_project_id}",
    response_model=Union[CharityProjectDb, Error],
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
    charity_project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    service = CharityProjectService(session=session)
    return await service.delete_charity_project(charity_project_id)


@router.patch(
    "/{charity_project_id}",
    response_model=Union[CharityProjectDb, Error],
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    charity_project_id: int,
    updated_charity_project: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    service = CharityProjectService(session=session)
    return await service.update_charity_project(
        charity_project_id, updated_charity_project
    )

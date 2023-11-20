from http import HTTPStatus
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.services.investing_service import InvestingService


class BaseService:
    def __init__(
        self,
        session: AsyncSession,
        user: Optional[User] = None,
    ):
        self.session = session
        self.user = user
        self.investing_service = InvestingService(self.session)

    async def create(self, obj_in, user: Optional[User] = None):
        try:
            return await self.CRUD.create(obj_in, self.session, user=user)
        except IntegrityError:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail="Something went wrong!",
            )

    async def get(self, obj_id):
        return await self.CRUD.get(obj_id, self.session)

    async def get_multi(self):
        return await self.CRUD.get_multi(self.session)

    async def update(self, obj_id, obj_in):
        return await self.CRUD.update(obj_id, obj_in, self.session)

    async def remove(self, obj_id):
        return await self.CRUD.remove(obj_id, self.session)

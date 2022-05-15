from typing import List

from db import get_session, models, schemas
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .get_api import api


@api.get("/users", response_model=List[schemas.User])
async def users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(models.User))
    users = result.scalars().all()
    return users


@api.post("/users")
async def add_user(user: schemas.User, session: AsyncSession = Depends(get_session)):
    user = models.User(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

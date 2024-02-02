from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session

from . import crud
from .schemas import PostRead

router = APIRouter(tags=['Posts'])

@router.get("/")
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_posts(session=session)
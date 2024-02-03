from typing import Annotated
from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.post import Post

from core.database import get_async_session

from . import crud


async def get_post_by_id(
    post_id: Annotated[int, Path],
    session: AsyncSession = Depends(get_async_session)
) -> Post:
    post = await crud.get_post(session=session, post_id=post_id)
    if post:
        return post

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id} not found:("
    )

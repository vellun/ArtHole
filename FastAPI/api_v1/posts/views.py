from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.post import Post

from core.database import get_async_session

from . import crud
from .schemas import PostCreate, PostRead, PostUpdate
from .dependencies import get_post_by_id

router = APIRouter(tags=["Posts"])


@router.get("/", response_model=list[PostRead])
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_posts(session=session)


@router.get("/{post_id}/", response_model=PostRead)
async def get_post(post: Post = Depends(get_post_by_id)):
    return post


@router.post(
    "/",
    response_model=PostCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_post(
    post_in: PostCreate, session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_post(session=session, post_in=post_in)


@router.patch("/{post_id}/")
async def update_post(
    post_update: PostUpdate,
    post: Post = Depends(get_post_by_id),
    session: AsyncSession = Depends(get_async_session),
):
    return await crud.update_post(post=post, session=session, post_update=post_update)


@router.delete("/{post_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(session: AsyncSession = Depends(get_async_session),
                      post: Post = Depends(get_post_by_id)) -> None:
    await crud.delete_post(post=post, session=session)

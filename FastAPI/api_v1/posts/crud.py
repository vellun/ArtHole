"""
Create
Read
Update
Delete
"""

from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import PostCreate, PostUpdate
from core.models import Post


#Read
async def get_posts(session: AsyncSession) -> list[Post]:
    stmt = select(Post).order_by(Post.id)
    result = await session.execute(stmt)
    posts = result.scalars().all()
    return list(posts)


async def get_post(session: AsyncSession, post_id: int) -> Optional[Post]:
    return await session.get(Post, post_id)


#Create
async def create_post(session: AsyncSession, post_in: PostCreate) -> Post:
    post = Post(**post_in.model_dump())
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


#Update
async def update_post(
        session: AsyncSession,
        post: Post,
        post_update: PostUpdate
        ):
    for name, value in post_update.model_dump(exclude_unset=True).items():
        setattr(post, name, value)
    await session.commit()
    return post


#Delete
async def delete_post(
        session: AsyncSession,
        post: Post
) -> None:
    await session.delete(post)
    await session.commit()


"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Post


async def get_posts(session: AsyncSession) -> list[Post]:
    stmt = select(Post.id).order_by(Post.id)
    result = await session.execute(stmt)
    posts = result.scalars().all()
    return list(posts)
from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

Base = declarative_base()

metadata = MetaData()

engine = create_async_engine(settings.db_url)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, autocommit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
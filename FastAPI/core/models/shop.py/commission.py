from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
)

from ...database import Base
from ..post import Post


class Commission(Base, Post):
    __tablename__ = "commissions"

    price = Column(Integer, nullable=False)
    
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
)

from ...database import Base
from ..post import Post


class Adopt(Base, Post):
    __tablename__ = "adopts"

    is_auction = Column(Boolean, default=True)
    fix_price = Column(Integer)
    start_bit = Column(Integer)
    min_bit = Column(Integer)
    auto_buy = Column(Integer)
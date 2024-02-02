from sqlalchemy import (
    Boolean,
    Column,
    Integer,
)

from ...database import Base
from ..post import Post


class Ych(Base, Post):
    __tablename__ = "ychs"

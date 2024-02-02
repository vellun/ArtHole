from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    TIMESTAMP,
)

from ..database import Base


""" Модель пользователя """

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    
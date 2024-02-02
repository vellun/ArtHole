from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
)

from ..database import Base


""" Общий класс для всех постов, от которого наследуются 
разные виды постов на продажу """

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    picture_url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    posted_at = Column(TIMESTAMP, default=datetime.utcnow)
    mature_content = Column(Boolean, default=False)
    likes = Column(Integer)

from typing import Optional
from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    picture_url: str
    title: str
    description: str
    mature_content: bool = False


class PostCreate(PostBase):
    pass


class PostUpdate(PostCreate):
    picture_url: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None


class PostRead(PostBase):
    # Чтобы возвращать объекты pydantic вместо sqlalchemy
    model_config = ConfigDict(from_attributes=True)

    id: int

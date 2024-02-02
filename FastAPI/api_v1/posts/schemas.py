from pydantic import BaseModel


class PostBase(BaseModel):
    picture_url: str
    title: str
    description: str
    mature_content: bool = False


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int

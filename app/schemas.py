from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    text: str
    owner_id: int


class PostCreate(PostBase):
    pass


class Post(PostBase):
    number_of_views: int
    created_at: datetime

    class Config:
        from_attributes = True


class CommentBase(BaseModel):
    owner_id: int
    text: str
    post_id: int


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int

    class Config:
        from_attributes = True

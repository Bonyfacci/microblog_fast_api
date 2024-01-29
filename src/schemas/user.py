import datetime

from pydantic import BaseModel

from .post import PostDetails


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    nickname: str

    posts_count: int
    created_at: datetime.datetime

    is_active: bool

    all_posts: list[PostDetails]

    class Config:
        from_attributes = True


# При детальном профиля пользователя должна быть информация:
# никнейм,
# кол-во постов,
# дата регистрации
# все посты пользователя c
# текст поста
# дата создания
# просмотры

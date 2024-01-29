import datetime

from pydantic import BaseModel

from .comment import CommentDetails


class PostBase(BaseModel):
    text: str
    owner_id: int


class PostCreate(PostBase):
    pass


class Post(PostBase):
    number_of_views: int
    created_at: datetime.datetime

    view_count: int

    all_comments: list[CommentDetails]

    class Config:
        from_attributes = True


class PostDetails(PostBase):
    created_at: datetime.datetime


# При детальном просмотре поста должна быть информация:
# автор поста,
# текст поста,
# кол-во просмотров,
# все комментарии к посту с
# автор
# текст комментария,
# дата создания поста.
